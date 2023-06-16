"""
Borg singleton is a design pattern in Python that allows state sharing for different instances.
Eg. Navigation parent Singleton for Maya and Mari subclass singleton
"""

#from abc import ABCMeta

class BorgSingleton(object):
    __instance__ = {}

    # can create metaclass and abstract methods for subclass to implement
    #__metaclass__ = ABCMeta

    def __new__(cls, *args, **kwargs):
        cls.__instance__ = super(BorgSingleton, cls).__new__(cls, *args, **kwargs)
        cls.__instance__.test_dict = {'a': 1, 'b': 2}
        return cls.__instance__


class ChildBorg(BorgSingleton):
    pass


if __name__ == "__main__":
    borg = BorgSingleton()

    child = ChildBorg()
    print(child is borg)
    print(borg.test_dict)
    print(child.test_dict)
