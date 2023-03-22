import sys
from cx_Freeze import setup, Executable

# Include all the required files
include_files = [
    "assets",
    "icon.ico",
]

# Dependencies
build_exe_options = {"packages": ["pygame"], "excludes": ["tkinter"], "include_files": include_files}

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
    description="Destroy all aliens!",
    options={"build_exe": build_exe_options},
    executables=executable,
)