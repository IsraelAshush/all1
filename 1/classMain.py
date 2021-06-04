import class1

def main():
    dog1 = class1.dog()
    dog2 = class1.dog('aviv')
    dog3 = class1.dog('dviv')
    dogs = [dog1, dog2, dog3]
    for dog in dogs:
        print(dog)
    dog1.set_age(3)
    print dog1


if __name__ == '__main__':
    main()