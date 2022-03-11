# Using variables, conditions, and for loop

alex = {
    "name": "Alex",
    "age": 19,
}
melissa = {
    "name": "Melissa",
    "age": 22,
}
dan = {
    "name": "Dan",
    "age": 28,
}
rita = {
    "name": "Rita",
    "age": 20,
}
friends = [alex, melissa, dan, rita]
for i in range(0, len(friends)): 
        if friends[i]["age"] >= 21:
         print("Hello", friends[i]["name"] + ". You may have a drink at the bar!")
        else:
            print("Sorry", friends[i]["name"] + ". You are too young to drink!")


