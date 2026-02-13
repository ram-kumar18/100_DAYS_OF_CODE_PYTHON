# from turtle import Turtle, Screen
# chokli = Turtle()
# print(chokli)
# chokli.shape("turtle")
# chokli.color("Red","Blue")
# chokli.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l" # left align
print(table)
