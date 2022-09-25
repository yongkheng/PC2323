import pathlib
import shutil

p = pathlib.Path('.')
flist = p.rglob('Sec*/**')
dlist = [item for item in flist if item.is_dir()]
dlist = [d for d in dlist if d.name.split('.')[-1] in ['git', 'idea']]

for d in dlist:
    print(f"removing {d}")
    shutil.rmtree(d)
