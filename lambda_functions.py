from functools import reduce


def add_two_numbers(a, b):
    return a + b


print(add_two_numbers(1, 2))

add_two = lambda a, b: a + b
print(add_two(1, 2))

scores = [{"eng": 23, "mat": 34}, {"eng": 45, "mat": 44}, {"eng": 45, "mat": 56}, {"eng": 45, "mat": 66}]

sorted_by_maths = sorted(scores, key=lambda s: s["mat"])
print(sorted_by_maths)

def get_eng_score(score):
    return score["eng"]

sorted_by_eng = sorted(scores, key= get_eng_score)
print(sorted_by_eng)

ages=[34,45,54,66,78,65,44,67,89,89,670,60,55,66,64,63,44,57,68,69,85]

total_age=reduce(lambda x,y:x+y, ages, 0  )

print(total_age)

new_ages= map(lambda x : x*2, ages)
new_ages= map(lambda x : x+2, ages)
print(list(new_ages))


above_45=filter(lambda age : age>45, ages)
print(list(above_45))





