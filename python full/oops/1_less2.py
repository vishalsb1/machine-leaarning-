# making aur oown class
'''# typees of naming used in python 
1-> Pascal Case - je words astil tyache 1st letter Capital asel
2-> Camel Case - je words astil tyacha second words cha 1st letter Capptial
3-> snake_case - sagla chota but used underscore in words

'''
"""
class User:
    pass


user1=User()
print(user1)

user1.id=90
user1.name="irtru"

user2=User()
user2.id=19
user2.name="ootior"
 """
'''
atta hai sarkha karnyat 
kai barra nhi vattat so constructor user hoto
      def __init__(self):
        attributes
        etc
'''

class User:
    
    # initializing constructor 
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.name=user_name
        self.follower=0  # its know as the default parameter

# creating an object
user1=User(80,"soumya")
print(user1.id)
print(user1.name)
print(user1.follower)