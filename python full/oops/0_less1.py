"""
procedrial programming  - >fortan , cobal 

methods - > function of a particular object
attribute -> variables of a particular object


class la kasa call kartat 
" obj = class_name() '

"""
'''
# here we are fguring out turtule module 
from turtle import Turtle,Screen

timmy=Turtle()
# calling 

screen1=Screen()
screen1.canvheight
# its the attribute

screen1.exitonclick()
# this is the method 

'''
from prettytable import PrettyTable

Table=PrettyTable()

Table.field_names = ["Pokémon Name", "Pokémon Type"]

# Add rows
# Table.add_row(["Pikachu", "Electric"])
# Table.add_row(["Raichu", "Electric"])
# or

Table.add_rows([
    ["Pikachu", "Electric"],
    ["Raichu", "Electric"]
])

# allign 
Table.align['Pokémon Name'] = 'l'
Table.align['Pokémon Type'] = 'l'

# Display the table
print(Table)
# allign 
Table.align['Pokémon Name'] = 'c'
Table.align['Pokémon Type'] = 'c'

# Display the table
print(Table)
# allign 
Table.align['Pokémon Name'] = 'r'
Table.align['Pokémon Type'] = 'r'

# Display the table
print(Table)
