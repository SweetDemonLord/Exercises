class TextClass:
    def __init__(self):
        self._lst = ""

    def __setattr__(self, name, value):
        if name == "lst":
            if type(value) == list:
                self._lst = ''.join(k[0] for k in value if type(k)==str)
            else:
                raise ValueError("Can't read a field: value must be a list.")
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        if name == "lst":
            return self._lst
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

txt = TextClass()
txt.lst = ["Sos", "odd", "nigger", "yellow"]
print("txt.list = ", txt.lst)

try:
    txt.lst = "not a list"
except ValueError as e:
    print(e)

try:
    print(txt.nonexistent)
except AttributeError as e:
    print(e)