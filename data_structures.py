# data structures
# collections
# list, dictionary, set

scores = [45, 35, 54, 67, 87, 77, 67, 57, 89, 34, 65, 57, 49, 73, 64, 38, 50, 93, 43, 22]

# access a score
print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])

# add a score
scores.append(89)
print(scores)

# remove scores (only the 1st one)
scores.remove(77)
print(scores)

print(len(scores))

print(scores.count(45))

scores.sort()  # ascending order
print(scores)

scores.sort(reverse=True)  # descending
print(scores)

# slice list
top_5 = scores[:5]  # cutting upto pos 5
print(top_5)

top_5 = scores[1:5]  # cutting from pos 1 to 5
print(top_5)

top_5 = scores[-5:]  # cutting the last 5
print(top_5)

# dictionary

person = {"name": "Ronnie", "Age": 22, "Weight": 56}
print(person["name"])
print(person["Age"])

# set
days = {"mon", "tue", "wed", "thu", "fri", "sat", "sun", "mon"}
print(days)

for s in scores:  # for each score in scores
    print(s)
    if s < 50:
        pass
    print(s)

for d in days:  # for each day in days
    print(d)
