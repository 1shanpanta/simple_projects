import imageio.v3 as iio
filenames = ['1.png', '2.png']
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("result.gif",images,duration=800,loop=0)
