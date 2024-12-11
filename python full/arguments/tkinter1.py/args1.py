# arguments
def add(*args):
    sum=0
    for i in args:
       sum+=i
    return sum

print(add(1,2,3,4,5))

'''
 baically the argument that are pasedin the 
function are entered in a tuple and can be used to acces 
in the index form also
'''
#  kw argumets - unlimited variables create karu sakto aapn 

def calculate(n,** kw):
    n*=kw['add']
    n+=kw['multiply']
    print(n)

calculate(2,add=3,multiply=90)


# example of kwargs


class Car:

    def __init__(self,**kw):
        self.car_name=kw.get('car_name')
        self.car_model=kw.get('car_model')
        # get() jar samja apn kai input nhi
        # dela class cha object bolavlevar tevha 
        # error na deta it will give 'None' asa

car1=Car(car_name='mazda yedzvi',car_model='1790')
print(car1.car_name)
print(car1.car_model)

