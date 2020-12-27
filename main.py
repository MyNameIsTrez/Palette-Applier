# Run manually: python main.py
# Build EXE: pyinstaller --noconsole --onefile --icon="Media/palette-applier.ico" --add-data="Media/github-icon.png;Media" --add-data="Media/finish.wav;Media" --name="Palette Applier" main.py

from Python import gui

gui.init_window_theme()
gui.run_window(gui.init_window())