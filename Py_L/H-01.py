class Music(object):
    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        print("ini: %s" % name)

    def __str__(self):
        return "%s\nstr: %s" % (super().__str__(), self.name)


a = Music("a")
b = Music("b")
print(a)

str_1 = 'mute'
print(str_1)
