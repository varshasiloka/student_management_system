students= {}

while True:
    print("\n===student management===")
    print("1.add student")
    print("2.display students")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
    print("6.exit")

    choice=input("enter choice:")

    if choice=="1":
        roll=int(input("enter the roll number:"))
        name=input("enter name:")
        marks=float(input("enter marks:"))
        students[roll]={"name":name,"marks":marks}
        print("student added!")

    elif choice=="2":
        for roll,data in students.items():
            print(roll,data)

    elif choice=="3":
        roll=int(input("enter the roll number:"))
        print(students.get(roll,"student not found!"))
                 
    elif choice=="4":
        roll=int(input("enter the roll number:"))
        if roll in students:
                 students[roll]["name"]=input("new name:")
                 students[roll]["marks"]=float(input("new marks:"))
                 print("record update!")
        else:
            print("student not found!")

    elif choice=="5":
         roll=input("enter roll number:")
         if roll in students:
             del students[roll]
             print("student deleted!")
         else:
             print("student not found!") 
    elif choice=="6":
          break
