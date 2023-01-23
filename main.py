from matplotlib.image import imread
from PIL import Image
import numpy as np
from scipy.stats import mode

mazeimg = Image.open(".\Maze200x200.png")
gray = mazeimg.convert('L')
arr = np.array(gray)
print(arr.shape)

for i in range(arr.shape[0]):
    fila = arr[i]
    for j in range(fila.shape[0]):
        if arr[i][j]>127:
            arr[i][j] = 255
        else:
            arr[i][j] = 0
        # código para procesar la columna


print(arr)
im = Image.fromarray(arr)
im.save('nueva_imagen.jpg')
