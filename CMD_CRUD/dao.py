from model import model
import re

class data_operation:

    def start(self,o):
        print('1.INSERT\n2.VIEW\n3.SEARCH\n4.UPDATE\n5.DELETE\n6.EXIT')
        i = int(input('enter your choice::'))

        if (i == 1):
            print('------INERT OPERATION------')
            o = self.insert(o)

        elif (i == 2):
            print('------DISPLAY OPERATION------')
            if(len(o) == 0):
                print("Please Enter Data First !! ")
                self.start(o)
            else:
                self.display(o)

        elif (i == 3):
            print('------SEARCH OPERATION------')
            if (len(o) == 0):
                print("Please Enter Data First !! ")
                self.start(o)
            else:
                self.search(o)
        elif (i == 4):
            print('------UPDATE OPERATION------')
            if (len(o) == 0):
                print("Please Enter Data First !! ")
                self.start(o)
            else:
                self.update(o)

        elif (i == 5):
            print('------DELETE OPERATION------')
            if (len(o) == 0):
                print("Please Enter Data First !! ")
                self.start(o)
            else:
                o = self.delete(o)

        elif (i == 6):
            print('------THANK YOU------')
            exit(0)

        self.start(o)

    def insert(self, data): # Insert Method
        i = int(input('how many profile you want to add ::'))
        for j in range(i):
            id= int(input('enter id ::'))
            name = input('enter name ::')
            number = input('enter number ::')
            d = model(id,name,number)
            data.append(d)

        flag = input("Do You Want To Add More Data ?? (Y/N)")

        if(flag == "Y"):
            self.insert(data)
        else:
            return data

        return data


    def display(self,ll): # Display Method
        print('ID \t NAME \t NUMBER')
        for i in range(len(ll)):
            print(ll[i].getId(),' \t ',ll[i].getName(),' \t ',ll[i].getNumber())


    def update(self,edit_data): #Update Method
        self.display(edit_data)
        ID = int(input("Enter the id of edit data ::"))

        data_needed_to_update = int(input("1. Update Name \n 2. Update Number"))
       # print(data_needed_to_update)

        if(data_needed_to_update == 1):
            updated_data = self.Update_name(ID, edit_data)
            print("**** Name Updated ****")
            flag = input("\nDo You Want To Update Number Also ?? (Y/N)")

            if(flag == 'Y'):
                updated_data = self.Update_number(ID,updated_data)
                self.display(updated_data)
            else:
                self.display(updated_data)
        else:
            updated_data = self.Update_number(ID,edit_data)
            print("**** Number Updated ****")
            flag = input("\nDo You Want To Update Name Also ?? (Y/N)")

            if(flag == 'Y'):
                updated_data = self.Update_name(ID,updated_data)
                self.display(updated_data)
            else:
                self.display(updated_data)




    def Update_name(self,id,update_data): #Update Name Function According TO ID
        for i in range(len(update_data)):
            if(update_data[i].getId() == id):
                New_name = input("Enter New Name")
                update_data[i].setName(New_name)
        return update_data



    def Update_number(self, id, update_data): #Update Number Function According TO ID
        for i in range(len(update_data)):
            if (update_data[i].getId() == id):
                New_number = input("Enter New Number")
                update_data[i].setNumber(New_number)
        return update_data


    def delete(self, data):
        self.display(data)
        ID = int(input("Enter The ID Of Delete Data"))

        for i in range(len(data)):
            if(data[i].getId() == ID):
                data.pop(i)
                print("Data Deleted")
                self.display(data)
        return data


    def pattern_match(self, f_key, data):
        temp = []
        pattern = re.compile(f_key)
        for i in range(len(data)):
            flag = pattern.match(data[i].getName())
            if (flag):
                temp.append(data[i])
        return temp


    def search(self, data):
        flag = int(input("1. Search From Name\n2. Search From Number"))
        temp_list = []

        if(flag == 1):
            print("For Name Search")
            type_of_search = int(input("1. Search From Starting\n2. Search From Middle\n3. Search From End"))

            if(type_of_search == 1):
                keyword = input("Enter Keyword For Search (Starting)")
                f_key = keyword + "[A-Za-z]*"
                temp_list = self.pattern_match(f_key,data)

            elif(type_of_search == 2):
                keyword = input("Enter Keyword For Search (Middle)")
                f_key = "[A-Za-z]*" + keyword + "[A-Za-z]*"
                temp_list = self.pattern_match(f_key,data)

            elif (type_of_search == 3):
                keyword = input("Enter Keyword For Search (End)")
                f_key = "[A-Za-z]*" + keyword
                temp_list = self.pattern_match(f_key, data)

        else:
            print("For Number Search")
            type_of_search = int(input("1. Search From Starting\n2. Search From Middle\n3. Search From End"))

            if (type_of_search == 1):
                keyword = input("Enter Keyword For Search (Starting)")
                f_key = keyword + "[0-9]*"
                temp_list = self.pattern_match(f_key, data)

            elif (type_of_search == 2):
                keyword = input("Enter Keyword For Search (Middle)")
                f_key = "[0-9]*" + keyword + "[0-9]*"
                temp_list = self.pattern_match(f_key, data)

            elif (type_of_search == 3):
                keyword = input("Enter Keyword For Search (End)")
                f_key = "[0-9]*" + keyword
                temp_list = self.pattern_match(f_key, data)

        self.display(temp_list)

        repeat_flag = input("Do You Want To Search Again ?? (Y/N)")

        if(repeat_flag == "Y"):
            self.search(data)
        else:
            self.start(data)
