class student:
    def __init__(self ,name ,age):
        self.name=name
        self.age=age

    def display_details(self):
        print("Students name =" ,self.name)
        print("Students age =" , self.age)


s1 = student("parthiv", 23)
s1.display_details()
