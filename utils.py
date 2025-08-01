import sys
import os

def resource_path(relative_path):
    """Get correct path for files when running normally or as PyInstaller executable"""
    try:
        base_path = sys._MEIPASS  # PyInstaller-created temp folder
    except AttributeError:
        base_path = os.path.abspath(".")  # Normal running directory
    
    return os.path.join(base_path, relative_path)
