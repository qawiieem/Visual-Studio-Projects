employee_file = open("EMPLOYEES.txt","r")  # r= read mode, w= write mode, a= append mode, r+= read & write mode

#print(employee_file.readable())                # check whether the file is readable

#print(employee_file.read())                    # print all the information inside the file

#print(employee_file.readline())                # read line 1 inside the file
#print(employee_file.readline())                # read line 2 inside the file
#print(employee_file.readline())                # read line 3 inside the file
#print(employee_file.readline())                # read line 4 inside the file

#print(employee_file.readlines())               # read all of the line inside the file into a list

#print(employee_file.readlines()[1])            # read line 1

#for employee in employee_file.readlines():
    #print(employee)

employee_file.close()                          # close file
