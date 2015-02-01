from PIL import Image
import sys
import map0

if __name__ == "__main__":
    map0.entity_preamble()

    i = Image.open(sys.argv[1])

    size = i.size
    for x in range(0, size[0] - 1):
        for y in range(0, size[1] - 1):
            pixel1 = 256 - i.getpixel((x,y))[0]
            pixel2 = 256 - i.getpixel((x,y+1))[0]
            pixel3 = 256 - i.getpixel((x+1,y+1))[0]
            pixel4 = 256 - i.getpixel((x+1,y))[0]
            
            map0.triangle_column([64 * (x), 64 * (y), pixel1], [64 * (x), 64 * (y+1), pixel2], [64 * (x+1), 64 * (y+1), pixel3])
            map0.triangle_column([64 * (x), 64 * (y), pixel1], [64 * (x+1), 64 * (y+1), pixel3], [64 * (x+1), 64 * (y), pixel4])
    
    map0.entity_finish()
