# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

w = str(input("Hey there! What is your name?"))

trips = {}

x = 0

while x != 'done':
    x = str(input(print("Enter a place you have gone on a trip to or type 'done' when finished: ")))
    if x == 'done':
        break
    y = str(input(print("Enter how many days the trip was: ")))
    trips[x] = y

for key, value in trips.items():
    print(w + " went to " + key + " for " + value + " days.")
