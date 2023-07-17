import re


def solution(A):

    # This pattern r"\.\d+\.\w{2,}$" matches a dot (\.) followed by one or more digits, followed by another dot (\.),
    # followed by two or more word characters (\w{2,}) until the end of the string ($).
    regex = re.compile(r"\.\d+\.\w{2,}$")

    # a dictionary to save image counter for each "name.ext" key, example: {"foo.jpg": 3, "bar.png" 1}
    image_map = dict()

    # initialize a list, same length as input.
    output = [None] * len(A)

    # sort the input list to get the correct sequence
    sorted_files = sorted(A)
    for image in sorted_files:
        # get the index of the image from the original list
        index = A.index(image)

        # check if the image matches the <name>.<padding>.<extension> pattern, valid extension is longer than 2 letters.
        if re.search(regex, image):
            # split image name in name, number and extension
            name, num, ext = image.split('.')

            # create a key with name.extension (foo.jpg)
            key = name + '.' + ext

            # check if the key exists in the image_map, if it doesn't, initialize counter by 0 then add 1 to it
            # {foo.jpg: 2, bar.png: 1}
            image_map[key] = image_map.get(key, 0) + 1

            # get the counter from the image map and create new name with the padding of 4 (foo.0002.jpg)
            image = name + '.' + str(image_map[key]).zfill(4) + '.' + ext

        # if the image name doesn't match the pattern, add it to the original index unaltered.
        # if the image name matches the pattern, add it to the original index.
        output[index] = image
    return output


if __name__ == "__main__":
    # A = ['foo.11.jpg', 'foo.12.jpg', 'foo.13.jpg', 'foo.14.jpg']
    # A = ['foo.0001.jpg', 'foo.0027.jpg',]
    # A = ['foo.0001.jpg', 'foo.0027.png',]
    # A = ['foo.0001.jpg', 'foo.002.jpg', 'bar.0001.jpg',]
    # A = ['foo.2.jpg', 'foo.4.jpg', 'foo.6.jpg', 'foo.5.jpg']
    # A = ['foo.1.jpg', 'foo.2.jpg', 'foo.3.png', 'bar.4.png']
    # A = ['foo.jpg', 'foo.1.jpg', 'foo.2.jpg', 'foo.3.png', 'bar.4.png', 'bar.1.p']
    A = ['foo.jpg', 'foo.1.jpg', 'foo.3.jpg', 'foo.2.jpg', 'bar.4.png', 'bar.1.p']
    d = solution(A)
    print(d)
