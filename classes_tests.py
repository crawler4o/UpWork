from dataclasses import dataclass
class Job:
    def __init__(self, *args):
        self.job_id = args[0]
        self.job_name = args[1]
        self.price = args[2]

    def __repr__(self):
        return f'Job ID is {self.job_id} and Job name is {self.job_name}'

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.job_id, self.job_name, self.price) == (other.job_id, other.job_name, other.price)


class Pr(Job):
    def __init__(self, *args):
        Job.__init__(self, *args)
        self.pr = args[3]


a = Pr('AZ2020', 'Azure', 50, ['tikvi', 'maruli'])
b = Job('LE1010', 'Lefter', 100, ['dini', 'repi'])

print(a)
print(a.__eq__(b))
print(a.__dict__)
print(a.__repr__)

print(b)
print(b.__eq__(a))
print(b.__dict__)



@dataclass
class Bostan:
    name: str
    mellons : int

c = Bostan('naKiro', 20)
print(c)
#breakpoint()
print(c.__dict__)
print(c.__repr__)

def kvadratche(a: 'tova e a') ->'a na kvadrat':
    return a**a

b = kvadratche(10)
print(b.__annotations__)