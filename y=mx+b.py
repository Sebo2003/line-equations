from fractions import Fraction
from fractions import gcd
import math

def asker():
    global y2
    global y1
    global x1
    global x2
    y2 = float(input("What's your y2 value?:"))
    y1 = float(input("What is your y1 value?"))
    x2 = float(input("What is your x2 value?:"))
    x1 = float(input("What is your x1 value?:"))

def standardizer():
    global fractionize_x
    global fractionize_b
    global new_x
    global new_b
    global new_y
    x_denominator = fractionize_x.denominator
    b_denominator = fractionize_b.denominator
            
    product = x_denominator*b_denominator
    new_x = product*fractionize_x
    new_b = product*fractionize_b
    new_y = product*1
            
    if new_x < 0:
        new_x = new_x*-1
                
    new_x,new_b,new_y = int(new_x),int(new_b),int(new_y)
    gcf = math.gcd(new_y, math.gcd(new_x,new_b))
    gcf = str(gcf)
    print("The greatest common factor is: " + gcf)
            
    gcf = float(gcf)
    new_x = new_x/gcf
    new_b = new_b/gcf
    new_y = new_y/gcf

input("This program will help you find slope and create line equations.")
while True:
    equation = input("Do you want standard, slope-intercept, or point-slope form? Type in 'standard', 'slope', or 'point'")

    if equation == 'standard':
        try:
            A = int(input("What is your 'A' value?"))
            if A < 0:
                print("'A' cannot be a negative in standard form!!")
                break
        except ValueError:
                print("No decimals in standard form!")
                break
        try:
            B = int(input("What is your 'B' value?"))
        except ValueError:
             print("No decimals in standard form!")
             break

        gcf = math.gcd(A,B)
        gcf = str(gcf)
        print("The greatest common factor is: " + gcf)            
        gcf = float(gcf)
        A = A/gcf
        B = B/gcf            
        print("Your equation is: {}x + {}y = C".format(A,B))
        break
        
    elif equation == 'slope':
        while True:
            slope = input("Do you need to find slope? Type 'yes' or 'no'.")
            if slope == 'yes':
                asker()
                m = (y2-y1)/(x2-x1)
                break
            elif slope == 'no':
                m = input("What is the slope?")
                break
            else:
                print("Must put in either 'yes' or 'no'")
                continue            

        b = float(input("What is your y-intercept?"))
        m,b = str(m),str(b)
        print("Your equation is: y = {}x + {}".format(m,b))

        simplify = input("Do you want to simplify this to standard form? Type in 'yes' or 'no'")

        if simplify == 'yes':
            m,b = float(m),float(b)
         
            fractionize_x = Fraction(m).limit_denominator()
            fractionize_b = Fraction(b).limit_denominator()
            
            standardizer()    
            print("Your equation is: {}x + {}y = {}".format(new_x,new_b,new_y))
            break
        else:
            break
      
    elif equation == 'point':
        while True:
             slope = input("Do you need to find slope? Type 'yes' or 'no'.")
             if slope == 'yes':
                asker()
                m = (y2-y1)/(x2-x1)

                break
             elif slope == 'no':
                m = input("What is the slope?")
                y1 = float(input("What is your y1 value?"))
                x1 = float(input("What is your x1 value?:"))
                break
             else:
                print("Must enter in either 'yes' or 'no'")
                continue
            
        print("Your equation is: y - {} = {}(x - {})".format(y1,m,x1))
        while True:
            simplify = input("Would you like to convert this to slope-intercept form? Type 'yes' or 'no'")

            if simplify == 'yes':
                m,x1 = float(m),float(x1)
                x1 = x1*-1   
                y_m = m*x1
                 
                m = str(m)
                x_m = m
                x_m = str(x_m)
                 
                y_m,y1 = float(y_m),float(y1)
                 
                added_y_m = y_m + y1
                added_y_m = str(added_y_m)
                converted = ("y = {}x + {}".format(x_m,added_y_m))
                print("Your equation is: " + converted)
                break
            else:
                break
        simplify_again = input("Would you like to convert {} into standard form? Type in 'yes' or 'no'".format(converted))
        while True:
            if simplify_again == 'yes': 
                x_m,added_y_m  = float(x_m),float(added_y_m)

                fractionize_x = Fraction(x_m).limit_denominator()
                fractionize_b = Fraction(added_y_m).limit_denominator()
                
                standardizer()
                print("Your equation is: {}x + {}y = {}".format(new_x,new_b,new_y))
                break
            elif simplify_again == 'no':
                break
            else:
                print("Must be 'yes' or 'no'")
                continue            
    else:
        print("You must input a valid response")
        continue

  
            
        
        




