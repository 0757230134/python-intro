file = open('test.txt', 'w') #to repeat= 'a' then \n (in 'here')

file.write("mash cool ")   #(here)
file.close()

try:
    file = open('test.txt', 'r')
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError:
    print("File not found")

# asn find out how to create and read csv files

data = [2, 3]
x=data[0]
y=data[1]
x, y = data
print(y)
print(x)



def population():
    return "Nairobi" ,4000000

name,pp=population()
print(pp)
print(name)


