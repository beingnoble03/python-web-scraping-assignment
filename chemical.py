import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="python_img"
)

class Chemical:
    def __init__(self, name, cas_number):
        self.name = name
        self.cas_number = cas_number
        print(f"Chemical with Name: {self.name} and CAS Number: {self.cas_number} created.")
    
    def show(self):
        print(f"Chemical name: {self.name} and CAS Number: {self.cas_number}.")

    def save(self):
        if self.name and self.cas_number:
            cursor = database.cursor()
            query = "INSERT INTO chemical(name, cas_number) VALUES (%s, %s)"
            values = (self.name, self.cas_number)
            cursor.execute(query, values)
            database.commit()

            print(f"Chemical name: {self.name} and CAS Number: {self.cas_number} saved in Database.")
        else:
            print("Name or CAS Number cannot be None.")