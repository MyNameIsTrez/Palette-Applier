# Run manually: python main.py
# Build EXE: pyinstaller --onefile --icon="Media/palette-applier.ico" --add-data="Media/github-icon.png;Media" --add-data="Media/finish.wav;Media" --name="Palette Applier" main.py


# TODO:
# Reading the pixels of the CC palette file with Pillow and saving them into a 2D list.
#   The indices of the top-level list represent the indices of the colors in the CC palette.
# Loop over every image in the Input folder, reading the pixels of an image with Pillow and storing it in a 2D list.
# Go over every pixel in the input image's 2D list.
#   Whenever a pixel isn't equal to one in the CC palette file, replace it with the closest pixel in the CC palette file in CIELAB color space.
# Saving the updated 2D list as a CC palette indexed PNG to the Output folder.


from Python import gui

gui.init_window_theme()
gui.run_window(gui.init_window())