import os

iconvert = 'C:/Houdini/bin/iconvert.exe'

def convert(src, trg=None):
    if trg:
        if not os.path.exists(trg):
            os.makedirs(trg)
        elif os.path.isfile(trg):
            trg = os.path.dirname(trg)
        basename = os.path.basename(src)
        name, ext = os.path.splitext(basename)
        trg = os.path.join(trg, name + '.exr')
    else:
        trg = os.path.splitext(src)[0] + '.exr'
    cmd = ' '.join([iconvert, src, trg])
    os.popen(cmd)


# convert('C:/texture.jpg')