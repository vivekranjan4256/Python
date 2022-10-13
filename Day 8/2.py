# number of cans=(wall height * wall width) / coverage per can
import math
def area_calc(height,width,coverage):
    no_of_cans=math.ceil((height*width)/coverage)
    print(f"No of cans required is {no_of_cans}")

height=int(input("Enter height of wall: "))
width=int(input("Enter width of wall: "))
coverage=int(input("Enter coverage per can: "))
area_calc(height,width,coverage)