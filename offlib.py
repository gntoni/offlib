#!/usr/bin/env python

import numpy as np

def read(path, verts_per_face=3):
    with open(path, "r") as offfile:
        mtype = offfile.readline().strip()
        if mtype == "COFF":
            has_color = True
        elif mtype == "OFF":
            has_color = False
        else:
            raise RuntimeError("Unknown File type: " + path)

        nVertices, nFaces, nEdges = map(int, offfile.readline().strip().split())

        if nEdges != 0:
            print("[WARNING]: %d edges present. Edges are ignored.")

        if has_color:
            vertices = np.zeros((nVertices, 7), dtype=float) # x,y,z,r,g,b,i
        else:
            vertices = np.zeros((nVertices, 3), dtype=int) # x,y,z

        faces = np.zeros((nFaces, verts_per_face+1)) # n, v_1, v_2, ..., v_n (n=vets_per_face)

        for idx in range(nVertices):
            vertices[idx] = np.array(offfile.readline().strip().split()).astype(float)
        for idx in range(nFaces):
            faces[idx] = np.array(offfile.readline().strip().split()).astype(float)

        return (vertices, faces)