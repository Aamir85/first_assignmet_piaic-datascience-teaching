import numpy as np
import matplotlib.pylab as plt
from PIL import Image
import os
size_200 = (200,200)

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_200)
        i.save('photo/{}_300{}'.format(fn,fext))

    def plti(im, h=8, **kwargs):

        y = im.shape[0]
        x = im.shape[1]
        w = (y/x) * h
        plt.figure(figsize=(w,h))
        plt.imshow(im, interpolation="none", **kwargs)
        plt.axis('off')

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        im = plt.imread(f)
        print(type(im))
        plti(im)
        im = im[20:300,:300,:3]
        #plti(im)
        print( im )