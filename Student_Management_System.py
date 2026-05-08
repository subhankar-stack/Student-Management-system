def add_Student_Details():
    BORDER = "+---+--------------------+---+---------+---------+--------------------------+---------------------+\n"
    students=int(input("Enter the number of student : "))
    Total_students=96
    
    if students>Total_students:
          print("❌ Total number of student for the department exceeds.")
    else:
        try:
          with open("Student_Details.txt","r") as file:
              lines=file.readlines()
              count=sum(1 for line in lines if line.startswith("|"))
        except FileNotFoundError:
          count=0

        for i in range(students):
            name = input("\033[1;36m Enter student name : \033[0m")
            age = int(input("\033[1;36m Enter student age : \033[0m"))
            month=input("\033[1;36m Enter the month of Addmission : \033[0m")
            date=input("\033[1;36m Enter the Addmission date of the student : \033[0m")
            college=input("\033[1;36m Enter the pevious college name of the student : \033[0m")
            school=input("\033[1;36m Enter the school name of the student : \033[0m")
            print("\n")

            with open("Student_Details.txt","a") as file:
             file.write(
               f"|{count+i+1:<3}"
               f"|{name:<20}"
               f"|{age:<3}"
               f"|{month:<9}"
               f"|{date:<9}"
               f"|{college:<26}"
               f"|{school:<20} |\n")
             file.write(BORDER)

def read_student_details():
    try:
        with open("Student_Details.txt", "r") as file:
            return file.readlines()  
    except FileNotFoundError:
        print("❌ \033[1;31m File not found\033[0m")
        return []

def search_by_name():
    name = input("\033[1;33m Enter name to search : \033[0m").lower()
    found = False

    lines = read_student_details()
    
    for line in lines:
        if line.startswith("|"):
            columns = line.split("|")
            student_name = columns[2].strip().lower()

            if name in student_name:
                print("\n\033[1;32m Student Found \033[0m 👇")
                print("\n")
                print(line)
                found = True

    if not found:
        print("❌ \033[1;31m No student found with this name\033[0m")

def search_by_month():
    month = input("\033[1;33m Enter the month of Addmission : \033[0m").strip().lower()
    found = False

    lines = read_student_details()

    for line in lines:
        if line.startswith("|"):
            columns = line.split("|")
            Addmission_month = columns[4].strip().lower()

            if month in Addmission_month:
                print("\n\033[1;32m Students Found\033[0m 👇")
                print("\n")
                print(line)
                found = True

    if not found:
        print("❌ \033[1;31m No student found for this Addmission month.\033[0m")

def search_by_date():
    date=input("\033[1;33m Enter the date of addmission : \033[0m").strip()
    found=False

    lines=read_student_details()

    for line in lines:
        if line.startswith("|"):
            columns=line.split("|")
            Addmission_date= columns[5].strip()
        
            if date in Addmission_date:
              print("\n\033[1;32m Students Found \033[0m 👇")
              print("\n")
              print(line)
              found=True
    if not found:
        print("❌ \033[1;31m NO student found for this Addmission date.\033[0m")

def search_by_age():
    age=input("\033[1;33m Enter the age of the student : \033[0m").strip()
    found=False

    lines=read_student_details()

    found = False

    for line in lines:
        if line.startswith("|"):
            columns = line.split("|")
            Student_age = columns[3].strip()

            if age in Student_age:
              if not found:
                print("\n\033[1;32m Students Found \033[0m 👇")
                print("\n")
              print(line)
              found = True

    if not found:
        print("❌ \033[1;31m NO student found for this age.\033[0m")

def update_name():
    try:
      with open("Student_Details.txt","r") as file:
        lines=file.readlines()
      print(f"\033[1;35m ------- Student Records -------\033[0m")
      print("\n")
      for line in lines:
        print(line,end="")
      slno=input("\n\033[1;33m Enter SL No to update name: \033[0m")
      found=False
      for i in range(len(lines)):
        if lines[i].startswith("|"):
            parts=lines[i].split("|")
            if parts[1].strip()==slno:
                found=True
                print(f"\033[1;34m ------- Old Record ------- \033[0m")
                print("\n")
                print(lines[i])
                new_name=input("\033[1;33m Enter new Name: \033[0m")
                update_line=(
                    f"|{parts[1].strip():<3}"
                    f"|{new_name:<20}"
                    f"|{parts[3].strip():<3}"
                    f"|{parts[4].strip():<9}"
                    f"|{parts[5].strip():<9}"
                    f"|{parts[6].strip():<26}"
                    f"|{parts[7].strip():<20}|\n"
                )
                lines[i]=update_line
                break
      if not found:
            print("❌ \033[1;31m Invalid Sl No\033[0m")
            
      with open("Student_Details.txt","w") as file:
            file.writelines(lines)
      print("✅ \033[1;32m Name updated successfully\033[0m")
    except FileNotFoundError:
        print("❌ \033[1;31m File not found\033[0m")

def update_age():
    try:
        with open("Student_Details.txt","r") as file:
           lines=file.readlines()
        print(f"\033[1;35m ------- Student Records -------\033[0m")
        print("\n")
        for line in lines:
            print(line,end="")
        slno=input("\033[1;33m Enter Sl No to update Age: \033[0m")
        found=False
        for i in range(len(lines)):
            if lines[i].startswith("|"):
                parts=lines[i].split("|")
                if parts[1].strip()==slno:
                   found=True
                   print("\n \033[1;34m ------- Old Record ------- \033[0m")
                   print("\n")
                   print(lines[i])
                   new_age=int(input("\033[1;33m Enter new Age: \033[0m"))
                   update_line=(
                        f"|{parts[1].strip():<3}"
                        f"|{parts[2].strip():<20}"
                        f"|{new_age:<3}"
                        f"|{parts[4].strip():<9}"
                        f"|{parts[5].strip():<9}"
                        f"|{parts[6].strip():<26}"
                        f"|{parts[7].strip():<20}|\n"
                    )
                   lines[i]=update_line
                   break
        if not found:
            print("❌ \033[1;31m Invalid Sl No\033[0m")
            
        with open("Student_Details.txt","w") as file:
            file.writelines(lines)
        print("✅ \033[1;32m Age updated successfully\033[0m")
    except FileNotFoundError:
     print("❌ \033[1;31m File not found\033[0m")

def update_Addmission_month():
    try:
        with open("Student_Details.txt","r") as file:
           lines=file.readlines()
        print("\n \033[1;35m ------- Student Records -------\033[0m")
        print("\n")
        for line in lines:
            print(line,end="")
        slno=input("\033[1;33m Enter Sl No to update Addmission Month: \033[0m")
        found=False
        for i in range(len(lines)):
            if lines[i].startswith("|"):
                parts=lines[i].split("|")
                if parts[1].strip()==slno:
                  found=True
                  print("\n \033[1;34m ------- Old Record ------- \033[0m")
                  print("\n")
                  print(lines[i])
                  New_Addmission_Month=input("\033[1;33m Enter new Addmission Month: \033[0m")
                  update_line=(
                        f"|{parts[1].strip():<3}"
                        f"|{parts[2].strip():<20}"
                        f"|{parts[3].strip():<3}"
                        f"|{New_Addmission_Month:<9}"
                        f"|{parts[5].strip():<9}"
                        f"|{parts[6].strip():<26}"
                        f"|{parts[7].strip():<20}|\n"
                    )
                  lines[i]=update_line
                  break
        if not found:
            print("❌ \033[1;31m Invalid Sl No\033[0m")
            
        with open("Student_Details.txt","w") as file:
            file.writelines(lines)
        print("✅ \033[1;32m Addmission Month updated successfully\033[0m")
    except FileNotFoundError:
     print("❌ \033[1;31m File not found\033[0m")

def update_Addmission_date():
    try:
        with open("Student_Details.txt","r") as file:
           lines=file.readlines()
        print("\n\033[1;35m ------- Student Records -------\033[0m")
        print("\n")
        for line in lines:
            print(line,end="")
        slno=input("\033[1;33m Enter Sl No to update Addmission date: \033[0m")
        found=False
        for i in range(len(lines)):
            if lines[i].startswith("|"):
                parts=lines[i].split("|")
                if parts[1].strip()==slno:
                  found=True
                  print("\n\033[1;34m ------- Old Record -------\033[0m")
                  print("\n")
                  print(lines[i])
                  New_Addmission_Date=input("\033[1;33m Enter new Addmission date: \033[0m")
                  update_line=(
                        f"|{parts[1].strip():<3}"
                        f"|{parts[2].strip():<20}"
                        f"|{parts[3].strip():<3}"
                        f"|{parts[4].strip():<9}"
                        f"|{New_Addmission_Date:<9}"
                        f"|{parts[6].strip():<26}"
                        f"|{parts[7].strip():<20}|\n"
                    )
                  lines[i]=update_line
                  break
        if not found:
            print("❌ \033[1;31m Invalid Sl No\033[0m")
            
        with open("Student_Details.txt","w") as file:
            file.writelines(lines)
        print("✅ \033[1;32m Addmission date updated successfully\033[0m")
    except FileNotFoundError:
     print("❌ \033[1;31m File not found\033[0m")

def update_college():
    try:
        with open("Student_Details.txt","r") as file:
           lines=file.readlines()
        print("\n \033[1;35m ------- Student Records -------\033[0m")
        print("\n")
        for line in lines:
            print(line,end="")
        slno=input("\033[1;33m Enter Sl No to update College: \033[0m")
        found=False
        for i in range(len(lines)):
            if lines[i].startswith("|"):
                parts=lines[i].split("|")
                if parts[1].strip()==slno:
                  found=True
                  print("\n\033[1;34m ------- Old Record -------\033[0m")
                  print("\n")
                  print(lines[i])
                  New_College=input("\033[1;33m Enter new College: \033[0m")
                  update_line=(
                        f"|{parts[1].strip():<3}"
                        f"|{parts[2].strip():<20}"
                        f"|{parts[3].strip():<3}"
                        f"|{parts[4].strip():<9}"
                        f"|{parts[5].strip():<9}"
                        f"|{New_College:<26}"
                        f"|{parts[7].strip():<20}|\n"
                    )
                  lines[i]=update_line
                  break
        if not found:
            print("❌ \033[1;31mInvalid Sl No\033[0m")
            
        with open("Student_Details.txt","w") as file:
            file.writelines(lines)
        print("✅ \033[1;32mCollege name updated successfully\033[0m")
    except FileNotFoundError:
     print("❌ \033[1;31mFile not found\033[0m")

def update_school():
    try:
        with open("Student_Details.txt","r") as file:
           lines=file.readlines()
        print("\n\033[1;35m ------- Student Records -------\033[0m")
        print("\n")
        for line in lines:
            print(line,end="")
        slno=input("\033[1;33m Enter Sl No to update School name: \033[0m")
        found=False
        for i in range(len(lines)):
            if lines[i].startswith("|"):
                parts=lines[i].split("|")
                if parts[1].strip()==slno:
                  found=True
                  print("\n\033[1;34m ------- Old Record ------- \033[0m")
                  print("\n")
                  print(lines[i])
                  New_School_Name=input("\033[1;33m Enter new School name: \033[0m")
                  update_line=(
                        f"|{parts[1].strip():<3}"
                        f"|{parts[2].strip():<20}"
                        f"|{parts[3].strip():<3}"
                        f"|{parts[4].strip():<9}"
                        f"|{parts[5].strip():<9}"
                        f"|{parts[6].strip():<26}"
                        f"|{New_School_Name:<20}|\n"
                    )
                  lines[i]=update_line
                  break
        if not found:
            print("❌ \033[1;31m Invalid Sl No\033[0m")

        with open("Student_Details.txt","w") as file:
            file.writelines(lines)
        print("✅ \033[32m School name updated successfully\033[0m")
    except FileNotFoundError:
     print("❌ \033[31m File not found\033[0m")

def delete_Student_Details():
    try:
        with open("Student_Details.txt", "r") as file:
            lines = file.readlines()

        print("\n\033[1;35m ------- Student Records -------\033[0m")
        print("\n")
        for line in lines:
            print(line, end="")

        slno = input("\n\033[1;33m Enter Sl No to delete: \033[0m")

        temp_lines = []
        found = False
        skip_next_border = False

        for i in range(len(lines)):
            line = lines[i]

            if skip_next_border:
                if line.startswith("+"):   
                    skip_next_border = False
                    continue

            if line.startswith("|"):
                parts = line.split("|")

                if parts[1].strip() == slno:
                    found = True
                    print("\n\033[1;36m ------- Deleted Record -------\033[0m")
                    print("\n")
                    print(line)

                    skip_next_border = True  
                    continue

            temp_lines.append(line)

        if not found:
            print("❌ \033[33m Invalid Sl No\033[0m")
            return

        new_lines = []
        new_slno = 1

        for line in temp_lines:
            if line.startswith("|"):
                parts = line.split("|")

                updated_line = (
                    f"| {new_slno:<3}"
                    f"| {parts[2].strip():<20}"
                    f"| {parts[3].strip():<3}"
                    f"| {parts[4].strip():<9}"
                    f"| {parts[5].strip():<9}"
                    f"| {parts[6].strip():<26}"
                    f"| {parts[7].strip():<20} |\n"
                )

                new_lines.append(updated_line)
                new_slno += 1
            else:
                new_lines.append(line)

        with open("Student_Details.txt", "w") as file:
            file.writelines(new_lines)

        print("✅ \033[32m Record deleted successfully and Sl No updated\033[0m")

    except FileNotFoundError:
        print(" ❌ \033[31m File not found\033[0m")

def check_student_details():
    st=int(input("\033[1;33m Enter 1 to check by name\033[0m"
    "\n\033[1;33m Enter 2 to check by month of Addmission\033[0m"
    "\n\033[1;33m Enter 3 to check byAddmission date\033[0m"
    "\n\033[1;33m Enter 4 to check by student age.\033[0m"
    "\n\033[1;33m Enter 5 to check the total student details. \n\033[0m"))
    if st==1:
        search_by_name()
    elif st==2:
        search_by_month()
    elif st==3:
        search_by_date()
    elif st==4:
        search_by_age()
    elif st==5:
        lines = read_student_details()

        if not lines:
          print("❌ No data found")
        else:
          print("\n\033[1;35m ------- Student Details -------\033[0m")
          print("\n")
          for line in lines:
            print(line.strip())
    else:
        print("\033[31m Invalid input\033[0m ❌")

def update_student_details():
        up=int(input("\033[1;33m Enter 1 to update name\033[0m"
        "\n\033[1;33m Enter 2 to update age.\033[0m"
        "\n\033[1;33m Enter 3 to update month of Addmission.\033[0m"
        "\n\003[1;33m Enter 4 to update Addmission date.\033[0m"
        "\n\033[1;33m Enter 5 to update previous college name.\033[0m"
        "\n\033[1;33m Enter 6 to update school name.\n\033[0m"))
        if up==1:
            update_name()
        elif up==2:
            update_age()
        elif up==3:
            update_Addmission_month()
        elif up==4:
            update_Addmission_date()
        elif up==5:
            update_college()
        elif up==6:
            update_school()
        else:
            print("\033[31m Invalid input\033[0m ❌")
    
while True:
    ch=int(input("\033[1;33m Enter 1 to view student details\033[0m"
    "\n\033[1;33m Enter 2 to add student details\033[0m"
    "\n\033[1;33m Enter 3 to update student details\033[0m"
    "\n\033[1;33m Enter 4 to delete student details\033[0m"
    "\n\033[1;33m Enter 5 to Exit.\n\033[0m"))
    if ch==1:
        check_student_details()
    elif ch==2:
        add_Student_Details()
    elif ch==3:
        update_student_details()
    elif ch==4:
        delete_Student_Details()
    elif ch==5:
        print("\033[32m Exiting...\033[0m")
        break
    else:
        print("\033[31m Invalid input\033[0m ❌")
