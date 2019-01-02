import main


def menu():
    print("""Simple math tasks\n\
Press the number of the task you want program to complete:\n\t1.Searching square area\n\t\
2.Searching rectangle area\n\t3.Searching triangle area\n\t4.Searching parallelogram area with two known sides and\
degree between them\n\t5.Searching parallelogram area with known base and height\n\t6.Degrees - radians converter\n\t\
7.Radians - degrees converter\n\t8. Searching square equation roots\n\t9. Check if year is leap""")
    number = int(input("Your choice is:"))
    
    if number == 1:
        side_size = int(input("Enter size length:"))
        result = main.square_area(side_size)
        
        print("Your square has", result, "area")
    
    elif number == 2:
        first_side = int(input("Enter size length:"))
        second_side = int(input("Enter second length:"))
        result = main.rectangle_area(first_side, second_side)
        
        print("Your rectangle has", result, "area")
    
    elif number == 3:
        first_side = int(input("Enter size length:"))
        second_side = int(input("Enter next length"))
        last_side = int(input("Enter last length:"))
        result = main.triangle_area(first_side, second_side, last_side)
        
        print("Your triangle has", result, "area")
    
    elif number == 4:
        first_side = int(input("Enter size length:"))
        second_side = int(input("Enter second length:"))
        degree = int(input("Enter the degree between two sides:"))
        result = main.parallelogram_area_sin(first_side, second_side, degree)
        
        print("Your parallelogram has", result, "area")
    
    elif number == 5:
        base = int(input("Enter base length:"))
        height = int(input("Enter height length:"))
        result = main.parallelogram_area_base(base, height)
        
        print("Your parallelogram has", result, "area")
    
    elif number == 6:
        degree = int(input("Enter your degree:"))
        result = main.degree_to_radians(degree)
        
        print("{} degrees = {} radians".format(degree, "{0:.1f}".format(result)))
    
    elif number == 7:
        radian = int(input("Enter your radian:"))
        result = main.radians_to_degrees(radian)
        
        print("{} radians = {} degrees".format(radian, "{0:.1f}".format(result)))
    
    elif number == 8:

        quadratic_coefficient = int(input("Enter the quadratic coefficient:"))
        linear_coefficient = int(input("Enter the linear coefficient:"))
        constant = int(input("Enter the constant:"))
        x_1, x_2 = main.square_equation_roots(quadratic_coefficient, linear_coefficient, constant)
        
        print("Equation {}x^2 + {}x + {} = 0 has following roots\n x = {}\n x = {}"
              .format(quadratic_coefficient, linear_coefficient, constant, x_1, x_2))
    
    elif number == 9:
        year = int(input("Enter your year:"))
        if main.is_leap(year):
            print("This year is not leap")
        else:
            print("This year is leap")
    
    else:
        print("You entered a wrong number")


if __name__ == "__main__":
 
    menu()