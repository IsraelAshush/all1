

class dog:
    def __init__(self, name = 'dog'):
        self._name = name
        self._age = 0

    def birthday(self):
        self._age += 1

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def __str__(self):
        return "The animal is: {} , and the age is: {}".format(self.get_name() , self.get_age())



def main():
    dog1 = dog()



if __name__ == '__main__':
    main()