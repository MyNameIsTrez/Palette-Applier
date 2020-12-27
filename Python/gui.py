import os, sys
import webbrowser
import PySimpleGUI as sg

from Python import shared_globals as cfg
from Python import convert


sg.user_settings_filename(filename="settings.json", path=".")


# TODO: Move to shared_globals.py
def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)


def init_window_theme():
	path_set_color = "#528b30"
	progress_bar_color = "#17569c"

	sg.theme("DarkGrey14")
	sg.theme_progress_bar_color((progress_bar_color, sg.theme_progress_bar_color()[1]))
	sg.theme_button_color((sg.theme_text_color(), "#2a3948"))


def init_window():
	if not os.path.isfile(sg.user_settings_filename()):
		sg.Popup("This is a tool that allows you to apply a palette to a group of images automatically. You can get more information from the GitHub repo by clicking its corresponding icon.", title="Welcome screen", custom_text=" OK ")

	paths_column = [
		[sg.Frame(layout=[[
			sg.ProgressBar(999, size=(15.6, 32), key="-PROGRESS BAR-"),
			sg.Button("Convert", key="-CONVERT-")
		]], title="Convert Images")]
	]

	play_finish_sound_setting = sg.user_settings_get_entry("play_finish_sound")
	sg.user_settings_set_entry("play_finish_sound", True if play_finish_sound_setting == None else play_finish_sound_setting)

	options_column = [
		[sg.Frame(layout=[[
			sg.Checkbox("Play finish sound", tooltip=" For when converting takes long ", key="-PLAY FINISH SOUND-", default=sg.user_settings_get_entry("play_finish_sound"), enable_events=True)
		]], title="Options")],
	]

	info_column = [
		[sg.Frame(layout=[[
			sg.Image(resource_path("Media/github-icon.png"), enable_events=True, key="-GITHUB-", tooltip=" Visit this program's GitHub page "),
		]], title="", pad=((9, 0), (12, 0)))]
	]

	layout = [
		[
			sg.Column(paths_column),
		],
		[
			sg.Column(options_column),
			sg.Column(info_column)
		]
	]

	cfg.sg = sg

	window = sg.Window("Palette Applier", layout, icon=resource_path("Media/palette-applier.ico"), font=("Helvetica", 16))
	cfg.progress_bar = window["-PROGRESS BAR-"]

	return window


def run_window(window):
	while True:
		event, values = window.read()

		if event == "Exit" or event == sg.WIN_CLOSED:
			window.close()
			break

		# print(event, values)

		if event == "-PLAY FINISH SOUND-":
			sg.user_settings_set_entry("play_finish_sound", values[event])
		elif event == "-CONVERT-":
			convert.convert()
		elif event == "-GITHUB-":
			webbrowser.open("https://github.com/MyNameIsTrez/Palette-Applier")