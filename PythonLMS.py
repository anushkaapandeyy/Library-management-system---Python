import datetime
import os
os.getcwd()

class LMS:
    def __init__(self, list, lib_name):
        self.list = "list.txt"
        self.lib_name = lib_name
        self.books_dict = {}
        Id = 101
        with open(self.list) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
            "lender_name": "", "Issue_date": "", "Status":"Available"}})           
            Id = Id + 1
    def display_books(self):
        print("----------------------------------------------List Of Books--------------------------------------")
        print("Books ID", "\t","Title")
        print("-------------------------------------------------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key,"\t\t", value.get("books_title"), "- [", value.get("Status"),"]")

    def Issue_books(self):
        books_id = input("enter books ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books()
            elif self.books_dict[books_id]['Status'] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Already Issued"
                print("Book issued successfully \n")
        else:
            print("Book Id not found")
            return self.Issue_books()

    def add_books(self):
        new_books

l = LMS("list.txt","Python's Library") 
print(l.display_books())
#print(LMS("list.txt","Python's Library"))