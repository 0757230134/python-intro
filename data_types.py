from threading import active_count


def add(x,y):
    return x+y

print(add(1,2))
print(add("1","2"))


def add(x:int,y:int):
    return x/y

print(add(1,2))


def avg(numbers:list):
    return sum(numbers)/len(numbers)

def printDetails(details:dict):
    for key, value in details.items():
        print(f"{key}: {value}")


def daysOfTheWeek(weekdays:set)
     for item in weekdays:
        print(item)


def sides(data:tuple):
    print(data)


def show_balance(active:count):
    """Takes in an account and shows its balance."""
     print(account.balance)

    acc1 = Account("002","Jim",2000)
    show show_balance(acc1)



























