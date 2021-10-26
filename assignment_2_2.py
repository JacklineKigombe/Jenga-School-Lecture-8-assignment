#profit.py
#A program to calculate profit in October
#by: Jackline Kigombe

def main():
    print("Good morning! Nice to see you today.")
    print("Let's see how much you made in October.")
    print()
    totalrevenue = eval(input("Enter total revenue for October in kshs: "))
    profit = (0.23 * totalrevenue)
    print("Profit made in October is ",profit," kshs.")


main()
    
