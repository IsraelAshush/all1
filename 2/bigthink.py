
class BigThing:

    def __init__(self, var = 6):
        self._var = var

    def size(self):
        if (type(self._var) is int or type(self._var) is float):
            return self._var
        elif(type(self._var) is (str) or type(self._var) is (dict) or type(self._var) is (list)):
            return len(self._var)
        else:
            return "Error"

def main():
    print '0'






if __name__ == '__main__':
    main()