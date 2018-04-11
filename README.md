# OFFlib
Library to read [OFF files](https://en.wikipedia.org/wiki/OFF_(file_format))

## Usage

```python
import offlib

vertices, faces = offlib.read("examples/cube.off", verts_per_face = 4)

print("Read object with %d vertices" % len(vertices))
```
