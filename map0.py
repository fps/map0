def preamble():
	print("")
	print("// entity 0")
	print("{")
	print('"classname" "worldspawn"')

# all coordinates of p1 must be smaller than those of p2	
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
