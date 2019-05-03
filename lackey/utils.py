import cv2
import numpy as np
from os.path import splitext

def cv2_imread(fpath):
    return cv2.imdecode(np.fromfile(fpath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

def cv2_imwrite(fpath, bitmap):
    path, ext = splitext(fpath)
    cv2.imencode(ext, bitmap)[1].tofile(fpath)
