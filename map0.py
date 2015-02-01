def entity_preamble():
	print("")
	print("// entity 0")
	print("{")
	print('"classname" "worldspawn"')

def entity_finish():
    print("}")

def brushdef_preamble():
    print("// brush 0")
    print("{")
    print("brushDef")
    print("{")

def brushdef_finish():
    print("}")
    print("}")

def face(p1, p2, p3):
    print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p1[0], p1[1], p1[2],  p2[0], p2[1], p2[2],  p3[0], p3[1], p3[2]))

def cube(p1, p2):
    brushdef_preamble()
    face([ p1[0], p1[1], p1[2] ], [ p2[0], p1[1], p2[2] ], [ p2[0], p1[1], p1[2] ])
    face([ p2[0], p1[1], p1[2] ], [ p2[0], p2[1], p2[2] ], [ p2[0], p2[1], p1[2] ])
    face([ p2[0], p2[1], p1[2] ], [ p1[0], p2[1], p2[2] ], [ p1[0], p2[1], p1[2] ])
    face([ p1[0], p2[1], p1[2] ], [ p1[0], p1[1], p2[2] ], [ p1[0], p1[1], p1[2] ])
    face([ p1[0], p1[1], p2[2] ], [ p2[0], p2[1], p2[2] ], [ p2[0], p1[1], p2[2] ])
    face([ p1[0], p1[1], p1[2] ], [ p2[0], p2[1], p1[2] ], [ p1[0], p2[1], p1[2] ])
    brushdef_finish()

# all coordinates of p1 must be smaller than those of p2	
#def cube(p1, p2):
#	print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p1[0], p1[1], p1[2],  p2[0], p1[1], p2[2],  p2[0], p1[1], p1[2]))
#	print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p2[0], p1[1], p1[2],  p2[0], p2[1], p2[2],  p2[0], p2[1], p1[2]))
#	print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p2[0], p2[1], p1[2],  p1[0], p2[1], p2[2],  p1[0], p2[1], p1[2]))
#	print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p1[0], p2[1], p1[2],  p1[0], p1[1], p2[2],  p1[0], p1[1], p1[2]))
#	print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p1[0], p1[1], p2[2],  p2[0], p2[1], p2[2],  p2[0], p1[1], p2[2]))
#	print("( %s %s %s ) ( %s %s %s ) ( %s %s %s ) ( ( 0.0625 0 63.5 ) ( 0 0.0625 0 ) ) NULL 0 0 0" % (p1[0], p1[1], p1[2],  p2[0], p2[1], p1[2],  p1[0], p2[1], p1[2]))

# p1, p2, p3 are [x, y, z] coordinates of the top of the column. the column
# extends to z = 0.
def triangle_column(p1, p2, p3):
    pass

