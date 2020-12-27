import os, sys, time, math
from playsound import playsound
from PIL import Image

from Python import shared_globals as cfg
from Python import update_progress


DITHERING = False
PALETTE_FILENAME = "palette.bmp"


# TODO: Move to shared_globals.py
def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)


def is_input_image(name):
	return name.lower().endswith((".bmp", ".png", ".jpg", ".jpeg")) and name.lower() != "palette.bmp"


def convert():
	time_start = time.time()

	update_progress.set_max_progress()

	palette = get_palette()

	for name in os.listdir("Input"):
		if is_input_image(name):
			print("Converting '{}'".format(name))
			process_file(name, palette)
			update_progress.increment_progress()

	update_progress.progress = 0
	update_progress.total_progress = 0

	elapsed = math.floor(time.time() - time_start)
	if cfg.sg.user_settings_get_entry("play_finish_sound"):
		playsound(resource_path("Media/finish.wav"))
	print("Finished in {} {}".format(elapsed, pluralize("second", elapsed)))


def process_file(name, palette):
	file_path = os.path.join("Input", name)
	old_img = Image.open(file_path)

	scale = 1
	old_img = old_img.resize((int(old_img.width * scale), int(old_img.height * scale)))

	# putpalette() always expects 256 * 3 ints.
	for k in range(256 - int(len(palette) / 3)):
		for j in range(3):
			palette.append(palette[j])

	palette_img = Image.new('P', (1, 1))
	palette_img.putpalette(palette)
	new_img = old_img.convert(mode="RGB").quantize(palette=palette_img, dither=DITHERING)
	new_img.save(os.path.join("Output", os.path.splitext(name)[0]) + ".png")


def get_palette():
	return Image.open(os.path.join("Input", PALETTE_FILENAME)).getpalette()
	# return [0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0, 255, 0, 255, 255, 255, 255]
	# return [0, 0, 0, 255, 255, 255]


def pluralize(word, count):
	return word + "s" if count != 1 else word