# def is_leap(year):
#     # leap = False
    
#     # Write your logic here
    
#     return(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# year = int(input("Enter a year: "))
# print(is_leap(year))



def is_leap(year):
    return(year % 4 == 0 and year % 100 != 0) or (year % 400 ==0)
    
year = int(input("Enter a year: "))
print(is_leap(year))
