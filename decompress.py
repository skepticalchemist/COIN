import argparse
import pickle
import gzip
import numpy as np

import matplotlib.pyplot as plt

def decompress_image(path_to_model, xdim=758, ydim=512):
    with gzip.open(path_to_model, 'rb') as f:
        model = pickle.load(f)

    input = create_input(xdim, ydim)
    output = model.predict(input)
    return convert_output(output, xdim, ydim)


def create_input(xdim, ydim):
    image_input = np.zeros((xdim * ydim, 2))

    count = 0
    for x in range(xdim):
        for y in range(ydim):
            image_input[count] = np.array([x, y])
            count += 1
    return image_input

def convert_output(output, xdim, ydim):
    output_image = np.zeros((xdim, ydim, 3))
    count = 0
    for x in range(xdim):
        for y in range(ydim):
            output_image[x, y, :] = output[count]
            count += 1
    return output_image


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert fitted model into image.')
    parser.add_argument('--model', type=str, default="models/model-1.pkl.gz", help='path to the pickled model')
    parser.add_argument('--xdim', type=int, default=768, help='pixel dimensions x')
    parser.add_argument('--ydim', type=int, default=512, help='pixel dimensions x')

    args = parser.parse_args()
    image = decompress_image( args.model, xdim=args.xdim, ydim=args.ydim )
    plt.imshow(image)
    plt.show()