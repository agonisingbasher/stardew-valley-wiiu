"""Stage only the prototype's required assets from user-supplied Content part 1.zip."""
import sys
import zipfile
from pathlib import Path

NAMES = [
    'Maps/Farm', 'Maps/spring_outdoorTileSheet_extra', 'Maps/paths',
    'Maps/spring_outdoorsTileSheet', 'Maps/spring_outdoorsTileSheet2',
    'Characters/Abigail', 'Characters/Farmer/farmer_base',
]
if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    with zipfile.ZipFile(sys.argv[1]) as archive:
        for name in NAMES:
            filename = name+'.xnb'
            p = root/'work/packed'/filename
            p.parent.mkdir(parents=True,exist_ok=True)
            p.write_bytes(archive.read(filename))
    print('Staged',len(NAMES),'XNB files')
