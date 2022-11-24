import random
import cv2
from english_words import english_words_set
import numpy as np 
from PIL import ImageFont, ImageDraw, Image 
import glob

'''
def texto(image_size, words_qty, img_fraction, percent_variation):
	fontsize = 1
	palavras =  (random.sample(english_words_set, words_qty))
	for palavra in palavras:
		palavra = str(palavra)
		h, w = image_size
		low_percent, high_percent = percent_variation
		blank = 255*np.ones((h, w)).astype(np.uint8)
		image_pil = Image.fromarray(blank)
		draw = ImageDraw.Draw(image_pil)
		fonts = glob.glob("/home/palestina/Desktop/TESTES/Imagens/fontes/*")
		font = random.choice(fonts)
		font_pil = ImageFont.truetype(font, fontsize)
		while font_pil.getsize(palavra)[0] < img_fraction*w:
			fontsize += 1
			font_pil = ImageFont.truetype(font, fontsize)
		fontsize -= 1
		font_pil = ImageFont.truetype(font, fontsize)
		textsize = draw.textsize(palavra, font= font_pil)
		textw = int((w - textsize[0])/2)
		texth = int((h - textsize[1])/2)
		aw = ah = random.randint(low_percent, high_percent)/100
		x = int(textw + (aw*w))
		y = int(texth + (ah*h))
		rw = int((w*aw) + w)
		rh = int((h*ah) + h)
		dim = (rw, rh)
		draw.text((x, y), palavra, font = font_pil, align="center")
		processed = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
		cv2.resize(processed, dim)
		cv2.imwrite(f'{palavra}.png', processed)
'''

def config():
    image_size = 400, 100
    words_qty = 10
    img_fraction = 0.30
    percent_variation = -5,5
    return image_size, words_qty, img_fraction, percent_variation

def image_process(image_size, percent_variation):
    h, w = image_size
    blank = 255*np.ones((h, w)).astype(np.uint8)
    image_pil = Image.fromarray(blank)
    draw = ImageDraw.Draw(image_pil)
    return blank, image_pil, draw

def fonts_resizer(palavra, img_fraction, w):
    fontsize = 1
    fonts = glob.glob("/home/palestina/Desktop/TESTES/Imagens/fontes/*")
    font = random.choice(fonts)
    font_pil = ImageFont.truetype(font, fontsize)
    while font_pil.getsize(palavra)[0] < img_fraction*w:
        fontsize += 1
        font_pil = ImageFont.truetype(font, fontsize)
    fontsize -= 1
    font_pil = ImageFont.truetype(font, fontsize)
    return font_pil

def dimension(a_valor, palavra, draw, image_size, font_pil, low_percent, high_percent):
    w, h = image_size
    aw = ah = random.randint(low_percent, high_percent)/100
    textsize = draw.textsize(palavra, font= font_pil)
    textw = int((w - textsize[0])/2)
    texth = int((h - textsize[1])/2)
    rw = int((w*aw) + w)
    rh = int((h*ah) + h)
    x = int(textw + (aw*w))
    y = int(texth + (ah* h))
    dim = (rw, rh)
    coord = (x, y)
    return dim, coord

def text(dim, coord, palavra, font_pil, image_pil, x, y, draw, words_qty):
    palavras = (random.sample(english_words_set, words_qty))
    for palavra in palavras:
        draw.text((x, y), palavra, font = font_pil, align="center")
        processed = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
        cv2.resize(processed, dim)
        cv2.imwrite(f'{palavra}.png', processed)
if  __name__ == "__text__":
    text()