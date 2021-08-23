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
        print("Entered informataion: "+ s_info)
        s_info_split=s_info.split(' ')
        write_into_csv(s_info_split)
        print("Entered splitted information: " + str(s_info_split))
        check=input("Enter y if you want to enter student info again and n if you dont:" )
        if(check=="y"):
            condition=True
        elif(check=="n"):
            condition=False
    
