"""
The match statement is used to perform different actions based on different conditions.

The Python Match Statement
Instead of writing many if..else statements, you can use the match statement.

The match statement selects one of many code blocks to be executed.
This is how it works:

The match expression is evaluated once.
The value of the expression is compared with the values of each case.
If there is a match, the associated block of code is executed.
The example below uses the weekday number to print the weekday name:


"""

day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7: 
        print("Sunday")
        
day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the weekend")
        
day = 4

match day:
    case 1| 2|3|4|5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")
        
month = 5
day = 4

match day:
    case 1| 2|3|4|5 if month == 4:
        print("A weekday in April")
    case 1|2|3|4|5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
        