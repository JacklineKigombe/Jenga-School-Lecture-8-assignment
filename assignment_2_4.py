#Pseudocode:
#n = input by user, number to find the power of
#p = input by user, power of number
#Find the power of n
#Output message displaying the result

def main():
    n  = eval(input("Enter the number you want to find power: "))
    p  = eval(input("Enter the power: "))
    pwr = 1
    for i in range (p):
        pwr = pwr * n

    print("The power of the number is",pwr)


main()
    







