quit = False
data = []
names = []
while not quit:
    print("----Welcome-------")
    print("1. Clear data")
    print("2. Input score")
    print("3. Remove student's data")
    print("4. Print the Average/Max/Min data for the scores")
    print("5. End the program")
    print("------------------")
    res = input("Please input your choice:")
    if res == "1":
        print("here are the codes for clear the data")
        names = []
        data = []
    elif res == "2":
        print("here are the codes for append new data with student's name")
        stuname = input("student name:")
        names.append(stuname)
        stuscore = int(input("student score:"))
        data.append(stuscore)
    elif res == "3":
        print("here are the codes for remove old data with student's name")
        stuname = input("student name:")
        index = names.index(stuname)
        data.pop(index)
        names.pop(index)
    elif res == "4":
        print("here are the codes for print the summary of the data")
        if len(data) != 0:
            print("Avg score is:",round(sum(data)/len(data),2))
            print("Max score is:",max(data))
            print("Min score is:",min(data))
        else:
            print("There is no score to output")
    elif res == "5":
        quit = True
    else:
        print("I can't recognize your command! test")