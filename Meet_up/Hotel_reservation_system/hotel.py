import names
from datetime import datetime
from datetime import timedelta
from random import randrange



class Room:
    def __init__(self, be, pr, se, bo,ro):
        self.beds = be
        self.price = pr
        self.seeview = se
        self.booked = bo
        self.room_name = ro


def create_hotel():
    hotel = {}
    for x in range(100):
        beds = randrange(4)+1
        price = 10 * (randrange(10)+1)
        seeview = randrange(2)

        booked_for = randrange(20)
        booked = []
        for x in range(booked_for):
            booked.append(str(datetime.now()+timedelta(days=randrange(x+1)))[:10])

        name = names.get_first_name(gender='female')

        hotel[x] = Room(beds, price, seeview, booked, name)

    return hotel


def conv_to_dic(obj):
    dict_ex = {}
    for x in obj:
        dict_ex[x] = [obj[x].beds, obj[x].price, obj[x].seeview, obj[x].booked, obj[x].room_name]

    return dict_ex



if __name__ == '__main__':
    hotel = create_hotel()

    print('The name of room is {}'.format(hotel[10].room_name))
    dic_hotel = conv_to_dic(hotel)  # This is the one :-)

    for x in (dic_hotel):
        print('hotel {} properties are {}'.format(x, dic_hotel[x]))

