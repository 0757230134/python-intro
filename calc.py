x=input("Enter 1st number:")
y=input("Enter 2nd number:")


#TODO say hello sam

#convert to numbers
try:
    int_x=int(x)  #ints=whole numbers while floats are decimals
    int_y=int(y)
    print(int_x+int_y)

except ValueError:
    print("Invalid input")


# pip freeze>requirements.txt











