import re


def solution(A):
    image_ext_map = dict()

    """
    This pattern r"\.\d+\.\w{2,}$" matches a dot (\.) followed by one or more digits, followed by another dot (\.),
    followed by two or more word characters (\w{2,}) until the end of the string ($).
    """

    # the regex will filter out all the images not following the pattern <name>.<padding>.<extension>, where extension
    # length is less than 2

    # the block filtering the input matching and not matching the pattern of <name>.<padding>.<extension>,
    # is not part of the submitted solution.
    regex = re.compile(r"\.\d+\.\w{2,}$")

    matched = []
    unmatched = []

    for img in A:
        if re.search(regex, img):
            matched.append(img)
        else:
            unmatched.append(img)

    # original submission starts from here

    for i in matched:
        img_contents = i.split('.')
        name, num, ext = img_contents[0], img_contents[1], img_contents[2]
        key = name + '.' + ext
        if key not in image_ext_map:
            image_ext_map[key] = [num]
        else:
            image_ext_map[key].append(num)

    output = []
    for name_ext, order in image_ext_map.items():
        res = []
        name, ext = name_ext.split('.')

        # next line was unfortunately, under the next for loop (facepalm)
        sorted_order = sorted(order)
        for i in range(len(order)):
            ind = sorted_order.index(order[i])
            res.insert(ind, name + '.' + str(i+1).zfill(4) + '.' + ext)
        output += res

    # added unmatched files back to the output (didn't add it to the original solution)
    return output + unmatched


if __name__ == "__main__":
    # A = ['foo.11.jpg', 'foo.12.jpg', 'foo.13.jpg', 'foo.14.jpg']
    # A = ['foo.0001.jpg', 'foo.0027.jpg',]
    # A = ['foo.0001.jpg', 'foo.0027.png',]
    # A = ['foo.0001.jpg', 'foo.002.jpg', 'bar.0001.jpg',]
    # A = ['foo.2.jpg', 'foo.4.jpg', 'foo.6.jpg', 'foo.5.jpg']
    # A = ['foo.1.jpg', 'foo.2.jpg', 'foo.3.png', 'bar.4.png']
    A = ['foo.jpg', 'foo.1.jpg', 'foo.2.jpg', 'foo.3.png', 'bar.4.png', 'bar.1.p']
    d = solution(A)
    print(d)
