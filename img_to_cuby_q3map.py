from PIL import Image
import sys
import map0

if __name__ == "__main__":
	map0.entity_preamble()
	
	i = Image.open(sys.argv[1])
	
	size = i.size
	for x in range(0, size[0]):
	    for y in range(0, size[1]):
	        pixel = i.getpixel((x,y))
	        if pixel[0] < 250:
	            map0.cube([64 * x, 64 * y, 0],  [64 * (x+1), 64 * (y+1), int(0.5 * (255 - pixel[0]))])
	
	map0.entity_finish()
