def rectangle_area(a, b):
    if(a>=0 and b>=0):
        area = a*b
        print("Pole prostokata wynosi:")
        print(area)
        
    else:
        print("Blad! Podaj nieujemna wartosc dlugosci boku")
        return

rectangle_area(3.23,1)
