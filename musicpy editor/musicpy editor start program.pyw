import traceback
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.scrolledtext import ScrolledText
import PIL.Image, PIL.ImageTk
from tkinter import filedialog
import sys
import os
import midiutil
import mido
import pygame
import keyboard
import time
import pyglet
from pyglet.window import mouse
from pyglet import shapes
import pygame.midi
import re
from yapf.yapflib.yapf_api import FormatCode

abs_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(abs_path)
os.chdir('..')
sys.path.append('.')
musicpy_vars = dir(__import__('musicpy'))
exec("from musicpy import *")
os.chdir('musicpy editor')
from io import BytesIO
import pygame

pygame.mixer.init(44100, -16, 1, 1024)
with open('config.py', encoding='utf-8-sig') as f:
    exec(f.read())
with open('musicpy editor for exe.py', encoding='utf-8-sig') as f:
    exec(f.read())