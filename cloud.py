#!/usr/bin/env python3
# File    : cloud.py 
# Purpose : A program to create word clouds out of txt input
# Author  : Joe McManus josephmc@alumni.cmu.edu
# Version : 0.1  05/14/2018 Joe McManus
# Copyright (C) 2018 Joe McManus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with 

from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from collections import defaultdict,Counter
from os import path
import random
import argparse
import matplotlib 
matplotlib.use('Agg') 
from scapy.all import *
import sys


parser = argparse.ArgumentParser(description='DNS  Word Cloud Image Generation')
parser.add_argument('infile', help="Source file", type=str)
parser.add_argument('outfile', help="Destination image file", type=str)
parser.add_argument('--bgimage', help="Optional image filei to shape around", type=str)
args=parser.parse_args()

if path.exists(args.infile):
	print("Source file: " + args.infile)
	print("Output file: " + args.outfile)
else:
	print("ERROR: Source file does not exist, exitting.") 
	quit()




text=[]
#Read source file
fh=open(args.infile, "r")
for line in fh:
    text.append(line.strip()[:-1])


cnt = Counter()
for item in text:
    cnt[item] += 1
#to change colormaps look at http://matplotlib.org/examples/color/colormaps_reference.html

if args.bgimage:
    import numpy as np
    mask = np.array(Image.open(args.bgimage))
    wc = WordCloud(regexp=r'.*\s', max_words=100, mask=mask, colormap='ocean', max_font_size=60, prefer_horizontal=1, height=800, width=1200).generate_from_frequencies(cnt)
else: 
    wc = WordCloud(regexp=r'.*\s', max_words=100, colormap='ocean', max_font_size=60, prefer_horizontal=1, height=800, width=1200).generate_from_frequencies(cnt)

wc.to_file(args.outfile)


