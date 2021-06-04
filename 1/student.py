import person


class student(person.Person):

    def __init__(self, name, age, score = 60):
        #super(student,self)._init_(name,age)
        person.Person.__init__(self, name, age)
        self._Avarage_score = score

    def get_Avarage_score(self):
        return self._Avarage_score

    def set_Avarege_score(self, score):
        self._Avarage_score = score





def main():
    print 'a'



if __name__ == '__main__':
    main()