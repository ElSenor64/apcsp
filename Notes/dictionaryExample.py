teacherNames = dict()



# assigning keys to values

teacherNames["barnett"] = "Jenna"

teacherNames["del valle"] = "Ileana"

teacherNames["wade"] = "Jacob"

teacherNames["yeh"] = "Kyle"



# retrieving info from dictionary

lname = raw_input("What is the teacher's last name?  ").lower()

print("The first name of that teacher is " + teacherNames[lname])
