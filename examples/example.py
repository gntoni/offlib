#!/usr/bin/env python

import offlib

vertices, faces = offlib.read("cube.off", verts_per_face = 4)

print("Read object with %d vertices" % len(vertices))
