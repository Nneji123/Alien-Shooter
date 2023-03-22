import os
import sys
from cx_Freeze import setup, Executable

# Include all the required files
include_files = [
    "alien.png",
    "background.png",
    "bullet.png",
    "explosion.wav",
    "laser.mp3",
    "player.png",
    "sfx.mp3",
    "icon.ico",
    "SPACEBOY.ttf",
]

# Dependencies
build_exe_options = {"packages": ["pygame"], "include_files": include_files}

# Executable
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executable = [
    Executable(
        "alien_shooter.py",
        base=base,
        target_name="AlienShooter",
        icon="icon.ico",
    )
]

setup(
    name="Alien Shooter",
    version="1.0",
    description="A simple game",
    options={"build_exe": build_exe_options},
    executables=executable,
)