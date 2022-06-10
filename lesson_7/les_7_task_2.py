from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def tailoring(self):
        pass


class Report:

    coat_count = 0
    suit_count = 0
    fab_cons = 0

    @property
    def rep(self):
        return f'Produced {Report.suit_count} suit and {Report.coat_count} coat, fabric consumption {Report.fab_cons}'


class Coat(Clothes):

    def __init__(self, size):
        self.size = size
        Report.coat_count += 1

    @property
    def tailoring(self):
        c_f_c = round((self.size / 6.5 + 0.5), 2)
        Report.fab_cons += c_f_c
        return c_f_c


class Suit(Clothes):

    def __init__(self, height):
        self.height = height
        Report.suit_count += 1

    @property
    def tailoring(self):
        s_f_c = round((self.height * 2 + 0.3), 2)
        Report.fab_cons += s_f_c
        return s_f_c


s_1 = Suit(1.88)
c_1 = Coat(42)
c_2 = Coat(50)
s_2 = Suit(1.76)
c_3 = Coat(64)
print(c_1.tailoring)
print(s_1.tailoring)
print(c_2.tailoring)
print(s_2.tailoring)
print(c_3.tailoring)
print(Report().fab_cons)
print(Report().suit_count)
print(Report().coat_count)
print(Report().rep)
