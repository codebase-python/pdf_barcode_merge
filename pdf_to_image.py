from wand.image import Image

def pdf_to_image():
	with Image(filename='./cimpress_sample.pdf',resolution=150,format="png") as img:
		img.alpha_channel = False
		img.save(filename='cimpress_sample.png')