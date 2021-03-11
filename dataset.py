import numpy as np
from PIL import Image

class ImageLoader:
    def __init__(self, path):
        self.path = path

    def __call__(self):

        img = Image.open(self.path)
        img = np.asarray(img)
        img = img / 255

        number_of_pixels = img.shape[0]*img.shape[1]
        X = np.zeros((number_of_pixels, 2))
        y = np.zeros((number_of_pixels, 3))

        count = 0
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                X[count] = np.array([i,j])
                y[count] = img[i,j,:]
                count += 1
        y = y.astype(np.float32)
        return X, y


if __name__ == "__main__":
    imgLoader = ImageLoader('data/kodim05.png')
    X, y = imgLoader()
    print(X.shape,
          y.shape,
          X.shape[0] == 768*512,
          X.shape[1]==2,
          y.shape[0] == X.shape[0],
          y.shape[1]==3)

    print(np.min(X) == 0, np.max(X) == 767)
    print(X)