def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f

    return decorate


@attrs(versionadded="2.2",
       author="Guido van Rossum")
class mymethod():
    def __init__(self):
        # print(getattr(mymethod, 'versionadded', 10))
        # print(getattr(mymethod, 'versed', 10))
        # print(getattr(mymethod, 'author', ))
        pass


if __name__ == "__main__":
    xx = mymethod()
    print(getattr(xx, 'versionadded', 10))
    print(xx.versionadded)