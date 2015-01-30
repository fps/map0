from PIL import Image
import sys

i = Image.open(sys.argv[1])

def preamble():
	print("")
	print("// entity 0")
	print("{")
	print('"classname" "worldspawn"')
	
def cube(p1, p2):
	print("// brush 0")
	print("{")
	print("brushDef")
	print("{")
	print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p1[0], p1[1], p1[2],  p2[0], p1[1], p2[2],  p2[0], p1[1], p1[2]))
	print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p2[0], p1[1], p1[2],  p2[0], p2[1], p2[2],  p2[0], p2[1], p1[2]))
	print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p2[0], p2[1], p1[2],  p1[0], p2[1], p2[2],  p1[0], p2[1], p1[2]))
	print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p1[0], p2[1], p1[2],  p1[0], p1[1], p2[2],  p1[0], p1[1], p1[2]))
	print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p1[0], p1[1], p2[2],  p2[0], p2[1], p2[2],  p2[0], p1[1], p2[2]))
	print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p1[0], p1[1], p1[2],  p2[0], p2[1], p1[2],  p1[0], p2[1], p1[2]))
	print("}")
	print("}")
	
def finish():
    print("}")

preamble()
cube([1, 1, 1], [2, 2, 2])
finish()
