import mysql.connector
from Models.Row import Row
class Dal:
    eagle_eye_db = mysql.connector.connect(
        host="localhost",
        database="eagle_eye",
        user="root",
        password="",
        port="3306")

    #insert row into table
    def insert_row(self,row):
        try:
            my_cursor = self.eagle_eye_db.cursor()
            sql = "INSERT INTO agents (codeName,realName,location,status,missionsCompleted) VALUES (%s,%s,%s,%s,%s)"
            val = (row.code_name,row.real_name,row.location,row.status,row.missions)
            my_cursor.execute(sql,val)
            self.eagle_eye_db.commit()
        except Exception as ex:
            print(f"The error is: {ex}")

    #selct all table into a list
    def select_all(self):
        try:
            my_cursor = self.eagle_eye_db.cursor()
            my_cursor.execute("SELECT * FROM agents")
            all_rows = my_cursor.fetchall()
            list_rows = []
            for row in all_rows:
                row_object = Row(row[1],row[2],row[3],row[4],row[5])
                row_object.val_by_default(row[0])
                list_rows.append(row_object)
            return list_rows
        except Exception as ex:
            print(f"The error is: {ex}")

    #select the names of all columns
    def select_columns(self):
        try:
            my_cursor = self.eagle_eye_db.cursor()
            my_cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'agents'")
            all_columns = my_cursor.fetchall()
            list_of_columns = []
            for t in all_columns:
                list_of_columns.append(t[0])
            return list_of_columns
        except Exception as ex:
            print(f"The error is: {ex}")

    #
    def update(self,column,row_id,new_value):
        try:
            all_rows = self.select_all()
            set_id = []
            for row in all_rows:
                set_id.append(row.id)
            if column in self.select_columns() and row_id in set_id:
                my_cursor = self.eagle_eye_db.cursor()
                sql = f"UPDATE agents SET {column} = %s WHERE id = {row_id}"
                val = (new_value,)
                my_cursor.execute(sql,val)
                self.eagle_eye_db.commit()
            else:
                print("The column you entered doesn't exist")
        except Exception as ex:
            print(f"The error is: {ex}")
    def delete_by_id(self,the_id):
        try:
            all_rows = self.select_all()
            all_id = []
            for row in all_rows:
                all_id.append(row.id)
            if the_id in all_id:
                my_cursor = self.eagle_eye_db.cursor()
                sql = f"DELETE FROM agents WHERE id = {the_id}"
                my_cursor.execute(sql)
                self.eagle_eye_db.commit()
                print(f"Row {the_id} deleted")
            else:
                print(f"The id {the_id} doesn't exist!")
        except Exception as ex:
            print(f"The error is: {ex}")