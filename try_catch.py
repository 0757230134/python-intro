try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Something went wrong")