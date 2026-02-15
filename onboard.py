import numpy as np

def plane(v1,v2):
    proj = (v1@v2/(v1@v1))*v1
    v_plane = v2-(v2@v1)*v1
    return v_plane

