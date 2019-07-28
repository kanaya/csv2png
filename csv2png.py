from PIL import Image
import csv
import sys

input_fn = sys.argv[1]
output_fn = sys.argv[2]

csv_file = open(input_fn, "r")
csv_image = csv.reader(csv_file, delimiter=',')
image_width = 0
image_height = 0
raster = []
for row in csv_image:
	w = len(row)
	raster.append(row)
	image_height += 1
	image_width = max(image_width, w)
image = Image.new('RGB', (image_width, image_height))
for y, r in enumerate(raster):
	for x, p in enumerate(r):
		if p.strip() == '0':
			c = 0
		else:
			c = 255
		image.putpixel((x, y), (c, c, c))
image.save(output_fn)

