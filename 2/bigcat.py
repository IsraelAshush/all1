import bigthink


class BigCat(bigthink.BigThing):

    def __init__(self,weight):
        bigthink.BigThing.__init__(self)
        self.weight = weight

    def size(self):
        if self.weight > 20:
            return "Very fat"
        elif self.weight > 15:
                return "Fat"






def main():
    big1 = bigthink.BigThing()
    print big1.size()
    big2 = bigthink.BigThing("aba")
    print big2.size()
    big3 = BigCat(30)
    print big3.size()







if __name__ == '__main__':
    main()