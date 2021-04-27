#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile

def compreszip(p_file):
    print(p_file.replace('.', '_')+'.zip')
    jungle_zip = zipfile.ZipFile(p_file.replace('.', '_')+'.zip', 'w')
    jungle_zip.write(p_file, compress_type=zipfile.ZIP_DEFLATED)
 
    jungle_zip.close()

if __name__ == "__main__":
    compreszip('/home/erik/Escritorio/PandoraSoft_Logo.png')