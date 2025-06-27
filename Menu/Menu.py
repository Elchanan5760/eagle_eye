from Dal.DAL import Dal
from Models.Row import Row

class TheMenu:
    dal = Dal()
    def menu(self):
        cond = True
        while cond:
            choose = input("======Menu======\n"
                           "(1) To Create\n"
                           "(2) To Read\n"
                           "(3) To Update\n"
                           "(4) To Delete\n"
                           "(0) To Exit\n")
            if choose == "0":
                cond = False
            elif choose == "1":
                self.create()
            elif choose == "2":
                self.read_all()
            elif choose == "3":
                self.update()
            elif choose == "4":
                self.delete()
            else:
                print("The value is invalid")
    def create(self):
        code_name = input("Please enter code name:")
        real_name = input("Please enter real name:")
        location = input("Please enter location:")
        status = input("Please enter status:")
        missions = input("Please enter missions complete:")
        new_row = Row(code_name,real_name,location,status,missions)
        self.dal.insert_row(new_row)

    def read_all(self):
        all_table = self.dal.select_all()
        for row in all_table:
            print(row)

    def update(self):
        columns = self.dal.select_columns()
        rows = self.dal.select_all()
        cond = True
        while cond:
            column = (input("Which column do you want to update:\n"
                           f"(1) {columns[1]}\n"
                           f"(2) {columns[2]}\n"
                           f"(3) {columns[3]}\n"
                           f"(4) {columns[4]}\n"
                           f"(5) {columns[5]}\n"))
            print("Which row do you want to update (choose by id):")
            list_of_id = []
            for row in rows:
                print(row)
                list_of_id.append(row.id)
            choose_id = input()
            new_val = input("Which value do want to add:\n")
            if column.isdigit() and choose_id.isdigit():
                column = int(column)
                choose_id = int(choose_id)
                if column > 0 and column < 6 and choose_id in list_of_id:
                    self.dal.update(columns[column],choose_id,new_val)
                    print("The value changed successfully!")
                    cond = False
                else:
                    print("In column and row you can enter only numbers are available in the menu!")
            else:
                print("In column and row you can enter only numbers!")
    def delete(self):
        print("Which row do you want to update (choose by id):")
        rows = self.dal.select_all()
        list_of_id = []
        for row in rows:
            print(row)
            list_of_id.append(row.id)
        choose = input()
        if choose.isdigit():
            choose = int(choose)
            if choose in list_of_id:
                self.dal.delete_by_id(choose)
            else:
                print("The id doesn't exist!")
        else:
            print("You can enter only numbers!")

