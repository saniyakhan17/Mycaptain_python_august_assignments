import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["name","age","contact number","email id"])
        writer.writerow(info_list)


if __name__ == '__main__':
    condition= True
    while(condition==True):
        s_info=input("Enter the name and class of the student in the format:(name, age, contact_number, email id): ")
        
        s_info_split=s_info.split(' ')
        print("\nEntered information is: \n Name:{}\n Age:{}\n Phone numbe:{}\n Email ID:{}".format(s_info_split[0],s_info_split[1],s_info_split[2],s_info_split[3]))
        choice_check=input("is the entered info correct>(yes/no)")
        
        if choice_check=="yes":
            write_into_csv(s_info_split)
            check=input("Enter y if you want to enter student info again and n if you dont:" )
            if(check=="y"):
                condition=True
            elif(check=="n"):
                condition=False
        elif choice_check=="no":
            print("\n please renter the information")
        
        

    
