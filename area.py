def triangle_area():
    print("What is the area of a triangle?")
    base = int(input("Enter a number "))
    print("What is the height of the triangle")
    height = int(input("Enter a number "))
    area_of_triangle = (base * height)/2
    print(f"The area of the triangle is {area_of_triangle} square units.")

triangle_area()    
