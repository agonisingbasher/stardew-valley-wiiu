"""Build inspectable assets for an exploration proof of concept, not full gameplay."""
import json
import base64
from pathlib import Path
from PIL import Image
from read_tbin import read

ROOT = Path(__file__).resolve().parents[1]


def build():
    source = ROOT/'work/unpacked'
    target = ROOT/'assets'
    target.mkdir(exist_ok=True)
    m = read(source/'Maps/Farm.tbin')
    w, h = m['layers'][0]['size']
    sheets = {s['id']: s for s in m['sheets']}
    images = {s['id']: Image.open(source/'Maps'/f"{s['image']}.png").convert('RGBA') for s in m['sheets']}
    layers = {l['id']: l for l in m['layers']}
    ground = Image.new('RGBA', (w*16, h*16), (0,0,0,255))
    front = Image.new('RGBA', ground.size)

    def first(t): return t['frames'][0] if 'frames' in t else t

    def props(tile):
        if not tile: return {}
        t = first(tile)
        prefix = f"@TileIndex@{t['index']}@"
        result = {k[len(prefix):]:v for k,v in sheets[t['sheet']]['properties'].items() if k.startswith(prefix)}
        result.update(t.get('properties', {}))
        result.update(tile.get('properties', {}))
        return result

    for l in m['layers']:
        if l['id'] == 'Paths' or not l['visible']: continue
        canvas = ground if l['id'] in ('Back', 'Buildings') else front
        for i, tile in enumerate(l['tiles']):
            if not tile: continue
            t = first(tile)
            s = sheets[t['sheet']]
            tw, th = s['tileSize']
            mx, my = s['margin']; sx, sy = s['spacing']
            tx = mx + (t['index'] % s['size'][0])*(tw+sx)
            ty = my + (t['index'] // s['size'][0])*(th+sy)
            image = images[t['sheet']]
            if tx+tw > image.width or ty+th > image.height:
                raise ValueError(f'Tile outside image: {t}')
            canvas.alpha_composite(image.crop((tx,ty,tx+tw,ty+th)), ((i%w)*16,(i//w)*16))

    collision = []
    for i in range(w*h):
        b = layers['Back']['tiles'][i]
        wall = layers['Buildings']['tiles'][i]
        bp, wp = props(b), props(wall)
        # Deliberately limited rule set. Dynamic objects, warps and building overrides are not simulated.
        blocked = b is None or 'Water' in bp or 'Impassable' in bp or (wall is not None and 'Passable' not in wp)
        collision.append(int(blocked))

    spawn = [64*16+8, 15*16+8]
    if collision[15*w+64]:
        candidates = [i for i,v in enumerate(collision) if not v]
        i = min(candidates,key=lambda i:(i%w-64)**2+(i//w-15)**2)
        spawn = [(i%w)*16+8,(i//w)*16+8]
    ground.save(target/'farm_ground.png')
    front.save(target/'farm_front.png')
    combined = Image.alpha_composite(ground,front)
    combined.save(target/'farm_overview.png')
    # Complete NPC sheet used only as a clearly labelled temporary controllable avatar.
    avatar = Image.open(source/'Characters/Abigail.png').convert('RGBA').crop((0,0,64,128))
    avatar.save(target/'avatar_reference.png')
    scene = dict(width=w,height=h,tileSize=16,spawn=spawn,collision=collision,
        avatar='Abigail (temporary exploration avatar)',
        limitations=['Static first animation frames','Approximate map collision','No dynamic farm objects or map overrides','No warps, farming, save or audio'])
    (target/'scene.json').write_text(json.dumps(scene,ensure_ascii=False), encoding='utf-8')
    (target/'farm_map.json').write_text(json.dumps(m,ensure_ascii=False), encoding='utf-8')
    (target/'farm_ground.rgba').write_bytes(ground.tobytes())
    (target/'farm_front.rgba').write_bytes(front.tobytes())
    (target/'avatar.rgba').write_bytes(avatar.tobytes())
    (target/'collision.bin').write_bytes(bytes(collision))
    (ROOT/'native'/'scene_config.h').write_text(f'#pragma once\nconstexpr int MAP_W={w}, MAP_H={h}, TILE=16;\nconstexpr float START_X={spawn[0]}.0f, START_Y={spawn[1]}.0f;\n')
    data = ROOT/'native/data'
    data.mkdir(exist_ok=True)
    for name in ['farm_ground', 'farm_front', 'avatar']:
        (data/f'{name}.bin').write_bytes((target/f'{name}.rgba').read_bytes())
    (data/'collision.bin').write_bytes(bytes(collision))
    embedded = {key:'data:image/png;base64,'+base64.b64encode((target/name).read_bytes()).decode()
        for key,name in [('ground','farm_ground.png'),('front','farm_front.png'),('avatar','avatar_reference.png')]}
    (ROOT/'preview/scene-data.js').write_text('window.SCENE='+json.dumps(scene)+';\nwindow.ASSETS='+json.dumps(embedded)+';\n')
    print(f'Built {w}x{h} map; {sum(collision)} blocked tiles; spawn {spawn}')


if __name__ == '__main__': build()
