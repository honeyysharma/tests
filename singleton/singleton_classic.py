"""
Classic Singleton creates an instance only if there is no instance created so far; otherwise, it will return the
instance that is already created. Let’s take a look at the below code.
"""

class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


class SingletonChild(SingletonClass):
    pass


if __name__ == "__main__":
    singleton = SingletonClass()
    child = SingletonChild()

    # Here, you can see that SingletonChild has the same instance of SingletonClass and also shares the same state.

    print(child is singleton)

    singleton.sinl1_var = "singleton var"
    print(child.sinl1_var)

