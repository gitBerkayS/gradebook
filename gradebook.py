#Using 2D lists to add and remove entries

#two dimentional list
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
print("Last Semester Gradebook:\n", last_semester_gradebook)
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

#appending more subjects
gradebook.append(["computer science"])
gradebook[4].append(100)
gradebook.append(["visual arts"])
gradebook[5].append(93)

#They made a mistake grading and are rewarding an extra 5 points for our visual arts class
gradebook[5][1] += 5

#switching from a numerical grade value to a Pass/Fail option for your poetry class.
gradebook[2].remove(85)
gradebook[2].append("Pass")

print("")
print("Current Gradebook:\n", gradebook)

#combining gradebooks
full_gradebook = last_semester_gradebook + gradebook



print("")
print("Full Gradebook:\n", full_gradebook)
