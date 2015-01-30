from PIL import Image
import sys

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

if __name__ == "__main__":
	preamble()
	
	i = Image.open(sys.argv[1])
	
	size = i.size
	for x in range(0, size[0]):
	    for y in range(0, size[1]):
	        pixel = i.getpixel((x,y))
	        if pixel[0] < 128:
	            cube([x,y,0], [x+1, y+1, 1])
	finish()
