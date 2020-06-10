import os,sys,time,json
from PIL import Image, ImageDraw
from PIL.ImageOps import invert
from plane import plane
from Fibel.FolioText import FolioText
from math import sqrt
import wave
import argparse
import simpleaudio as sa

parser = argparse.ArgumentParser()
parser.add_argument("path", help="the relative path to the content used",
                    type=str)
args = parser.parse_args()

sentences = []
page_dir = args.path
jsons = []
wavs = []
texts = []

font = 'Fonts/schola.otf'
margin_width = 20
color = 0

plane_instance = 0

# ask here what format this is parsing, this is not json
def load_variables():
    lines = open(page_dir+'/content','r').readlines()
    for line in lines:
        row = line.split(";")
        texts.append(row[0])
        jsons.append(json.loads('['+(row[1].rstrip())+']'))
        try:
            wavs.append(sa.WaveObject.from_wave_read(wave.open(page_dir+'/'+row[0]+'.wav', 'rb')))
        except:
            wavs.append("")

def initialize_plane():
    plane_instance = plane(3,"back")
    plane_instance.initaudio()
    plane_instance.initscreen()
    plane_instance.initgesture()


load_variables()
initialize_plane()
print(wavs)
