import os
import re


# With regex
def filter_extensions_regex(input_files=None, image_extensions=None):
    """
    A function to filter out incorrect paths in a folder based on given image_extensions
    :param input_files: input image files
    :param image_extensions: image_extensions to filter
    :return:
    """
    if not input_files:
        print("No input files: {0}".format(input_files))
        return

    if not image_extensions:
        print("No extension given: {0}".format(image_extensions))
        return
        
    extensions = "|".join(image_extensions)
    reg_exp = re.compile(r'.*\.({e})$'.format(e=extensions))

    # alternative regex
    # reg_exp = re.compile(r'.*[0-9]\.({e})$'.format(e=extensions))

    filtered_files = [f for f in input_files if re.match(reg_exp, f)]
    output_files = sorted(filtered_files, key=lambda f: os.path.splitext(f)[::-1])

    print("Filter with regex".center(100, '-'))
    for f in output_files:
        print('{0}'.format(f))


# With any()
def filter_extensions_any(input_files=None, image_extensions=None):
    """
    A function to filter out incorrect paths in a folder based on given image_extensions
    :param input_files: input image files
    :param image_extensions: image_extensions to filter
    :return:
    """
    if not input_files:
        print("No input files: {0}".format(input_files))
        return

    if not image_extensions:
        print("No extension given: {0}".format(image_extensions))
        return

    filtered_files = [f for f in input_files if any(f.endswith('.'+e) for e in image_extensions)]
    output_files = sorted(filtered_files, key=lambda f: os.path.splitext(f)[::-1])

    print("Filter with any()".center(100, '-'))
    for f in output_files:
        print('{0}'.format(f))


# With endswith()
def filter_extensions_endswith(input_files=None, image_extensions=None):
    """
    A function to filter out incorrect paths in a folder based on given image_extensions
    :param input_files: input image files
    :param image_extensions: image_extensions to filter
    :return:
    """
    if not input_files:
        print("No input files: {0}".format(input_files))
        return

    if not image_extensions:
        print("No extension given: {0}".format(image_extensions))
        return

    jpegs = ['jpeg', 'jpg']

    for e in image_extensions:
        if e in jpegs:
            image_extensions = list(set(image_extensions + jpegs))
            break

    image_extensions = tuple(['.'+e for e in image_extensions])
    filtered_files = [f for f in input_files if f.endswith(image_extensions)]
    output_files = sorted(filtered_files, key=lambda f: os.path.splitext(f)[::-1])

    print("Filter with endswith tuple".center(100, '-'))
    for f in output_files:
        print('{0}'.format(f))


if __name__ == "__main__":

    path = r'C:\Users\honey\Pictures\images'
    files = [os.path.join(path, f) for f in os.listdir(path) if not os.path.isdir(f)]
    extensions = ["jpg", "png"]
    # filter_extensions_regex(files, extensions)
    # filter_extensions_any(files, extensions)
    filter_extensions_endswith(files, extensions)
