class Color:
    def __init__(self, color):
        self.__color = color

#Métodos getter y setter para "color"
    def set_color(self, color):
        self.__color = color
    
    def get_color(self):
        return self.__color

#print(Color.mro())

"""color_1 = Color(None)
color_1.set_color(input("Color de la figura: "))
print(f"Color: {color_1.get_color()}")"""