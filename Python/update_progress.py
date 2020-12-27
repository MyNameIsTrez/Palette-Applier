import os

from Python import shared_globals as cfg
from Python import convert


progress = 0
total_progress = 0


def increment_progress():
	global progress # TODO: See what happens when this line is removed.
	progress += 1
	cfg.progress_bar.UpdateBar(progress % total_progress, total_progress)


def set_max_progress():
	global total_progress # TODO: See what happens when this line is removed.
	total_progress = len([name for name in os.listdir("Input") if convert.is_input_image(name)])