# -*- coding: utf-8 -*-
from ntpath import join
import os
import pathlib
import shutil
from sys import argv
from os import path, rmdir

folder = []
home_dir = pathlib.Path.home()
name, path_dir = argv

images = ['.jpeg','.png','.jpg','.svg']
video = ['.avi','.mp4','.mov','.mkv']
documents = ['.doc','.docx','.txt','.pdf','.xlsx','.pptx']
music = ['.mp3','.ogg','.wav','.amr']
archives = ['.zip','.gz','.tar','.rar']

img_location = ('images')
vid_location = ('videos')
doc_location = ('documents')
mus_location = ('audio')
arc_location = ('archives')

location_dirs = [img_location, vid_location, doc_location, mus_location, arc_location]

def del_empty_dirs(path):
    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path_dir, dir)):
            inner_dir = os.listdir(os.path.join(path_dir, dir))
            if not len(inner_dir):
                os.rmdir(os.path.join(path_dir, dir))
        

def make_dirs(location):
    if not os.path.isdir(os.path.join(path_dir, location)):
        os.makedirs(os.path.join(path_dir, location))

def move_files(pa):
    
    file = os.path.split(pa)[1]
    
    file_name, file_ext = os.path.splitext(file)
    
    new_file_name = normalize(file_name)
    
    new_file = new_file_name + file_ext
        
    if file_ext in images:
        os.replace(pa, os.path.join(path_dir, img_location, new_file))
        return file_ext

    if file_ext in video:
        os.replace(pa, os.path.join(path_dir, vid_location, new_file))
        return file_ext

    if file_ext in documents:
        os.replace(pa, os.path.join(path_dir, doc_location, new_file))
        return file_ext

    if file_ext in music:
        os.replace(pa, os.path.join(path_dir, mus_location, new_file))
        return file_ext

    if file_ext in archives:
        os.replace(pa, os.path.join(path_dir, arc_location, new_file))
        shutil.unpack_archive(os.path.join(path_dir, arc_location, new_file), os.path.join(path_dir, arc_location, new_file_name))
        return file_ext

    else:
        os.replace(pa, os.path.join(path_dir, new_file))
        return file_ext


def normalize(string: str) -> str:

    trans_dict = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g',
                  ord('д'): 'd', ord('е'): 'e', ord('є'): 'ye', ord('ж'): 'zh',
                  ord('з'): 'z', ord('и'): 'y', ord('і'): 'i', ord('ї'): 'yi',
                  ord('й'): 'y', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm',
                  ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r',
                  ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f',
                  ord('х'): 'kh', ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh',
                  ord('щ'): 'shch', ord('ю'): 'yu', ord('я'): 'ya', ord('ы'): 'y',
                  ord('э'): 'e', ord('ё'): 'yo', ord('А'): 'A', ord('Б'): 'B',
                  ord('В'): 'V', ord('Г'): 'G', ord('Д'): 'D', ord('Е'): 'E',
                  ord('Є'): 'Ye', ord('Ж'): 'Zh', ord('З'): 'Z', ord('И'): 'Y',
                  ord('І'): 'I', ord('Ї'): 'Yi', ord('Й'): 'Y', ord('К'): 'K',
                  ord('Л'): 'L', ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O',
                  ord('П'): 'P', ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T',
                  ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'Kh', ord('Ц'): 'Ts',
                  ord('Ч'): 'Ch', ord('Ш'): 'Sh', ord('Щ'): 'Shch', ord('Ю'): 'Yu',
                  ord('Я'): 'Ya', ord('Ы'): 'Y', ord('Э'): 'E', ord('Ё'): 'Yo'}

    stringN = []
    for c in string:
        if not c.isalpha() and not c.isdigit():
            c = '_'
            stringN.append(c)
        else:
            c = c.translate(trans_dict)
            stringN.append(c)
    return ''.join(stringN)


for locations in location_dirs:
    make_dirs(locations)

for i in os.walk(path_dir):
    folder.append(i)
    
for address, dirs, files in folder:
    for file in files:
        x = os.path.join(address,file)
        move_files(x)
        
del_empty_dirs(path_dir)