from PIL import Image
import sys
import map0

if __name__ == "__main__":
	map0.preamble()
	
	i = Image.open(sys.argv[1])
	
	size = i.size
	for x in range(0, size[0]):
	    for y in range(0, size[1]):
	        pixel = i.getpixel((x,y))
	        if pixel[0] < 128:
	            map0.cube([x,y,0], [x+1, y+1, 1])
	map0.finish()
