village_school = {"name": "Boalia High School", "established": 1965, "total_teachers": 45, "total_students": 658}
school_details = {"address": "Boalia Bazar", "principal": "Sohidullah Kaisar", "founder": "Johir Raihan", "managing_committee": [{"name": "Sohrab Hossain", "age": 55, "occupation": "Retired person", "designation": "Chairman"}, {"name": "Raisul Islam", "age": 49, "occupation": "Businessman", "designation": "General Member"}, {"name": "Altaf Khan", "age": 33, "occupation": "Founder of Toto Company", "designation": "Vice Chairman"}, {"name": "Sohidul Islam", "age": 45, "occupation": "Businessman", "designation": "General Member"}]}

managing_committee_caniddates = [{"name": "Sultan Ahmed", "age": 43, "occupation": "Service Holder", "designation": "General Member"}, {"name": "Jamsed Khan", "age": 45, "occupation": "Doctor", "designation": "Vice Chairman"}, {"name": "Jahangir Talukder", "age": 47, "occupation": "Doctor", "designation": "Chairman"}, {"name": "Josim Uddin", "age": 38, "occupation": "Farmar", "designation": "Vice Chairman"}]

#0)output the data type of village_school
print(type(village_school))

#1)output the name of the above school
print(village_school["name"])

#2)try to access "number_of_rooms" key of that school without getting any error
print(village_school.get("number_of_rooms"))

#3)change that schools establishment year and make it 1962
village_school["established"] = 1962
print(village_school["established"])

#4)try to access "number_of_rooms" key of that school without getting any error
print(village_school.get("number_of_rooms"))

#4)add school_details to village_school
village_school.update(school_details)
print(village_school)

# *** PLEASE REMEMBER THAT AFTER ADDING 'school_details' to 'village_school' all items of 'school_details' are now available in 'village_school' dictionary

#5)check the length of village_school after adding school_details to it
print(len(village_school))

#6)add number_of_classrooms key with value 25 in village_school dictionary
village_school.update({"number_of_classrooms": 25})
print(village_school)

#7)check the data type of village_school
print(type(village_school))

#8)loop through all the values of village_school and check if any list type data found there if found print the key name
for item in village_school.items():
    if(type(item[1]) == type([])):
        print(item)
        print(item[0])

#9)output how many members are there in the managing committee
fetched_managing_committee = school_details["managing_committee"]
print(len(fetched_managing_committee))

#10)check if 'Founder of Toto Company' exist in the managing committee if found then remove that person from the managing committee
for item in fetched_managing_committee:
    if item["occupation"] == "Founder of Toto Company":
        fetched_managing_committee.remove(item)
        print(fetched_managing_committee)
    school_details["managing_committee"] = fetched_managing_committee

#11)output all the members occupation of the managing committee to check "Founder of Toto Company" is not there
for item in fetched_managing_committee:
    if item["occupation"] == "Founder of Toto Company":
        print(item)

#12)remove the last added item from the village_school (remember we've a built in function for that)
village_school.popitem()
print(village_school)

#13)remove the founder of that school
village_school.pop("founder")
print(village_school)

#14)set default value for founder key to "Robiul Islam"
village_school.setdefault("founder", "Robiul Islam")
print(village_school)

#15)check for a doctor in the 'managing_committee_candidates' list and make sure he wants to be the 'Vice Chairman' of that school if so then add that person to the managing_committe of that school

for item in managing_committee_caniddates:
    if item["occupation"] == "Doctor" and item["designation"] == "Vice Chairman":
        fetched_managing_committee.append(item)
school_details["managing_committee"] = fetched_managing_committee
print(school_details)

#16)output the member of managing_committee after update
print(school_details["managing_committee"])

#17)wipe out all the prperties of village_school and make it empty
village_school.clear()
print(village_school)


students1 = {"shaon", "sufian", "sohrab", "risat", "sohrab", "shaon", "sohan", "romiz"}
students2 = {"kobir", "shaon", "rakib"}

a = {8, 4, 3, 3, 2, 7, 5}
b = {1, 4, 9, 20, 34}

#1)check the data type of students
print(type(students1))
print(type(students2))

#2)check the length of students
print(len(students1))
print(len(students2))

#3)add "sweety" to students
students1.add("sweety")
print(students1)

#4)remove "risat" from students
students1.remove("risat")
print(students1)

#5)try to safely remove "raihan" from students without facing any error


#6)add students2 to students1
students1.update(students2)
print(students1)

#7)check is students2 is the subset of student1
print(students2.issubset(students1))

#8)check is students1 is the superset of student2
print(students1.issuperset(students2))

#9)clear student1
students1.clear()
print(students1)

#10)print all the combined items of student1 and student2, without any duplication (without making any permanent change)
students1.union(students2)
print(students1)

#10)print all the combined items of student1 and student2, with all common values of them (without making any permanent change)
students1.intersection_update(students2)
print(students1)

#10)print all the combined items of student1 and student2, with all uncommon values of them (without making any permanent change)
students1.symmetric_difference_update(students2)
print(students1)
