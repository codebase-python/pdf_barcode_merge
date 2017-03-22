from wand.image import Image

def pdf_to_image():
	with Image(filename='./cimpress_sample.pdf',resolution=150,format="jpg") as img:
		img.save(filename='cimpress_sample.jpg')