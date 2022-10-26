from functools import partial
from heapq import merge
from tempfile import TemporaryFile

def sort(fProduct):

    sorted_files = []

    nbytes = 1 << 10
    
    for lines in iter(partial(fProduct.readlines, nbytes), []):
        lines.sort(key=lambda k: k.strip('\n').split()[0])
        f = TemporaryFile("w+")
        f.writelines(lines)
        f.seek(0)
        sorted_files.append(f)

    fProduct.writelines(merge(*sorted_files, key=lambda k: k.strip('\n').split()[0]))

    for f in sorted_files:
        f.close()