lst_lbs = []  #creating empty list for lbs
lst_kgs = []  #creating empty list for kgs
stu_num = int(input("Enter the number of students:"))  #taking input from user about number of students and converting to integer value
for i in range(stu_num):  #looping through each value of student
    num = int(input('Enter the value to be inserted:')) #taking input about students weights in lbs and converting to integer value
    lst_lbs.append(num)   #list comprehension
    kilograms = num * 0.454  #converting into kgs
    lst_kgs.append(round(kilograms)) # appending into empty list
print(f'weights in lbs are {lst_lbs} and weights in kgs are {lst_kgs}') #printing out values in lbs and kgs

