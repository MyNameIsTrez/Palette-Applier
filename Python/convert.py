import os, sys, time, math
from playsound import playsound
from PIL import Image

from Python import shared_globals as cfg
from Python import update_progress


TRUE_INPUT_FOLDER = os.path.join("Input", os.pardir) # TODO: Better variable name.


# TODO: Move to shared_globals.py
def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)


def is_image(name):
	return name.lower().endswith((".bmp", ".png", ".jpg", ".jpeg"))


def convert():
	time_start = time.time()

	FINISH_SOUND = resource_path("Media/finish.wav")

	update_progress.set_max_progress()

	for name in os.listdir("Input"):
		if is_image(name):
			try:
				file_path = os.path.join("Input", name)
				im = Image.open(file_path)
				print("Converting '{}'".format(name))
				im.rotate(45).show()
				update_progress.increment_progress()
			except:
				pass

	# 	mod_subfolder_parts = pathlib.Path(mod_subfolder).parts
	# 	if len(mod_subfolder_parts) > 0 and mod_subfolder_parts[0].endswith(".rte"):
	# 		process_files(input_subfiles, input_subfolder_path, mod_subfolder, "Input")

	update_progress.progress = 0
	update_progress.total_progress = 0

	elapsed = math.floor(time.time() - time_start)
	if cfg.sg.user_settings_get_entry("play_finish_sound"):
		playsound(FINISH_SOUND)
	print("Finished in {} {}".format(elapsed, pluralize("second", elapsed)))


# def process_files(input_subfiles, input_subfolder_path, mod_subfolder, "Input"):
# 	for full_filename in input_subfiles:
# 		filename, file_extension = os.path.splitext(full_filename)

# 		input_file_path  = os.path.join(input_subfolder_path, full_filename)
# 		output_file_path = os.path.join(os.path.join("Output", mod_subfolder), full_filename)

# 		if full_filename == "desktop.ini":
# 			continue

# 		if file_extension in (".ini", ".lua"):
# 			create_converted_file(input_file_path, output_file_path, "Input")
# 		else:
# 			shutil.copyfile(input_file_path, output_file_path)


# def create_converted_file(input_file_path, output_file_path, "Input"):
# 	try: # TODO: Figure out why this try/except is necessary and why it doesn't check for an error type.
# 		with open(input_file_path, "r") as file_in:
# 			with open(output_file_path, "w") as file_out:
# 				all_lines_list = []
# 				file_path = os.path.relpath(input_file_path, "Input")

# 				line_number = 0
# 				for line in file_in:
# 					line_number += 1

# 					if warnings_available:
# 						for old_str, new_str in warning_rules.items():
# 							if old_str in line:
# 								warnings.append("'{}' line {}: {} -> {}".format(file_path, line_number, old_str, new_str))

# 					all_lines_list.append(line)

# 				all_lines = "".join(all_lines_list)

# 				for old_str, new_str in conversion_rules.items():
# 					all_lines = all_lines.replace(old_str, new_str)

# 				all_lines = regex_rules.regex_replace(all_lines)
# 				file_out.write(regex_rules.regex_replace_bmps_and_wavs(all_lines))
# 	except:
# 		shutil.copyfile(input_file_path, output_file_path)


# def warnings_popup():
# 	if warnings_available:
# 		w = max(30, len(max(warnings, key=len)))
# 		h = min(50, len(warnings)) + 1 # + 1 necessary because popup_scrolled adds an extra line.
# 		cfg.sg.popup_scrolled("\n".join(warnings), title="Lines needing manual replacing", size=(w, h), button_color=cfg.sg.theme_button_color(), background_color=cfg.sg.theme_background_color())


def pluralize(word, count):
	return word + "s" if count != 1 else word