import re


def solution(A):
    """
    A function to rename the image sequences.
    :param A: a list of image names
    :return: a list of renamed image sequences, with original order
    """

    # The pattern r"\.\d+\.\w+$" matches a dot (\.) followed by one or more digits, followed by another dot (\.),
    # followed by one or more word characters (\w) until the end of the string ($).
    regex = re.compile(r"\.\d+\.\w+$")

    # a dictionary to save image counter for each "name.ext" key, example: {"foo.jpg": 3, "bar.png" 1}
    image_map = dict()

    # initialize the output list with the same length as input.
    output = [None] * len(A)

    # create index dictionary to get index in the loop below, efficient than doing A.index(image)
    index_map = {image: index for index, image in enumerate(A)}

    # sort the input list to get the correct padding and maintain the order, that is, in the list [2, 4, 3],
    # 4 gets higher padding than 3
    sorted_files = sorted(A)
    for image in sorted_files:
        # get the index of the image from the index_map
        index = index_map[image]

        # check if the image matches the <name>.<padding>.<extension> pattern.
        if re.search(regex, image):
            # split image name in name, number and extension
            name, num, ext = image.split('.')

            # create a key with name.extension (foo.jpg)
            key = name + '.' + ext

            # check if the key exists in the image_map, if it doesn't, initialize counter by 0, then increment by 1
            # {foo.jpg: 2, bar.png: 1}
            image_map[key] = image_map.get(key, 0) + 1

            # get the counter from the image map and create the new name with the padding of 4 digits (foo.0002.jpg)
            image = name + '.' + str(image_map[key]).zfill(4) + '.' + ext

        # if the image name doesn't match the pattern, add it to the original index unaltered.
        # if the image name matches the pattern, add the updated image name to the original index.
        output[index] = image
    return output


if __name__ == "__main__":
    # A = ['foo.11.jpg', 'foo.12.jpg', 'foo.13.jpg', 'foo.14.jpg']
    # A = ['foo.0001.jpg', 'foo.0027.jpg',]
    # A = ['foo.0001.jpg', 'foo.0027.png',]
    # A = ['foo.0001.jpg', 'foo.002.jpg', 'bar.0001.jpg',]
    # A = ['foo.2.jpg', 'foo.4.jpg', 'foo.6.jpg', 'foo.5.jpg']
    # A = ['foo.1.jpg', 'foo.2.jpg', 'foo.3.png', 'bar.4.png']
    # A = ['foo.1.jpg', 'foo.2.jpg', ]
    # A = ['foo.jpg', 'foo.1.jpg', 'foo.2.jpg', 'foo.3.png', 'bar.4.png', 'bar.1.p']

    # ======================== uncomment to run each test case ========================
    # A = ['foo.1.jpg', 'foo.2.jpg', 'foo.3.jpg', 'foo.4.jpg', 'foo.5.jpg', 'foo.6.jpg', 'foo.7.jpg', 'foo.8.jpg', ]
    # A = ['foo.11.jpg', 'foo.12.jpg', 'foo.13.jpg', 'foo.14.jpg',]
    # A = ['foo.0001.jpg', 'foo.0002.jpg', 'foo.0003.png', 'foo.0004.png',]
    # A = ['foo.1.jpg', 'foo.2.jpg', 'bar.3.png', 'bar.4.png',]
    # A = ['foo.1.jpg', 'foo.2.jpg', 'foo.5.jpg', 'foo.3.jpg', 'foo.6.jpg', 'foo.4.jpg',]

    A = ['foo.jpg', 'bar', 'foo.14.jpg', 'foo.16.jpg', 'foo.15.jpg', 'bar.16.png', 'bar.1.p', 'bar.j']

    result = solution(A)
    print(result)

