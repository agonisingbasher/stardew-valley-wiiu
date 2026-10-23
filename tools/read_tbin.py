"""Strict tBIN10 reader; format reference: colinvella/tIDE xTile TbinFormat.cs."""
import struct
from pathlib import Path


class Reader:
    def __init__(self, data):
        self.data, self.pos = data, 0

    def take(self, size):
        if size < 0 or self.pos + size > len(self.data):
            raise ValueError(f'Truncated tBIN at {self.pos}, requested {size}')
        value = self.data[self.pos:self.pos+size]
        self.pos += size
        return value

    def byte(self): return self.take(1)[0]
    def integer(self): return struct.unpack('<i', self.take(4))[0]
    def string(self): return self.take(self.integer()).decode('utf-8')
    def size(self): return [self.integer(), self.integer()]

    def count(self):
        n = self.integer()
        if not 0 <= n <= 1000000: raise ValueError(f'Invalid count {n}')
        return n

    def props(self):
        out = {}
        for _ in range(self.count()):
            key, kind = self.string(), self.byte()
            if kind == 0: value = bool(self.byte())
            elif kind == 1: value = self.integer()
            elif kind == 2: value = struct.unpack('<f', self.take(4))[0]
            elif kind == 3: value = self.string()
            else: raise ValueError(f'Unknown property type {kind}')
            out[key] = value
        return out

    def static(self, sheet):
        if sheet is None: raise ValueError('Tile without tilesheet')
        index, blend = self.integer(), self.byte()
        return dict(sheet=sheet, index=index, blend=blend, properties=self.props())

    def animated(self):
        interval, count = self.integer(), self.count()
        sheet, frames = None, []
        while len(frames) < count:
            tag = chr(self.byte())
            if tag == 'T': sheet = self.string()
            elif tag == 'S': frames.append(self.static(sheet))
            else: raise ValueError(f'Invalid animation command {tag}')
        if not frames: raise ValueError('Empty animation')
        return dict(frames=frames, interval=interval, properties=self.props())

    def read(self):
        if self.take(6) != b'tBIN10': raise ValueError('Expected tBIN10')
        result = dict(id=self.string(), description=self.string(), properties=self.props())
        sheets = []
        for _ in range(self.count()):
            sheets.append(dict(id=self.string(), description=self.string(), image=self.string(),
                size=self.size(), tileSize=self.size(), margin=self.size(), spacing=self.size(), properties=self.props()))
        result['sheets'] = sheets
        known = {s['id']: s for s in sheets}
        layers = []
        for _ in range(self.count()):
            layer = dict(id=self.string(), visible=bool(self.byte()), description=self.string(),
                size=self.size(), tileSize=self.size(), properties=self.props())
            w, h = layer['size']
            if not 0 < w*h <= 1000000: raise ValueError('Invalid layer size')
            tiles, sheet = [], None
            for y in range(h):
                row = []
                while len(row) < w:
                    tag = chr(self.byte())
                    if tag == 'T':
                        sheet = self.string()
                        if sheet not in known: raise ValueError(f'Unknown sheet {sheet}')
                    elif tag == 'N':
                        count = self.count()
                        if count == 0 or len(row)+count > w: raise ValueError('Invalid null run')
                        row.extend([None]*count)
                    elif tag == 'S': row.append(self.static(sheet))
                    elif tag == 'A': row.append(self.animated())
                    else: raise ValueError(f'Invalid layer command {tag!r} at {self.pos-1}')
                tiles.extend(row)
            layer['tiles'] = tiles
            layers.append(layer)
        result['layers'] = layers
        if self.pos != len(self.data): raise ValueError(f'{len(self.data)-self.pos} trailing bytes')
        return result


def read(path):
    return Reader(Path(path).read_bytes()).read()


if __name__ == '__main__':
    import json, sys
    result = read(sys.argv[1])
    if len(sys.argv) > 2: Path(sys.argv[2]).write_text(json.dumps(result, ensure_ascii=False), encoding='utf-8')
    print('Sheets:', [(s['id'], s['image'], s['size']) for s in result['sheets']])
    print('Layers:', [(l['id'], l['size']) for l in result['layers']])
