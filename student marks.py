from tkinter.font import names

students = {
    "thanveer":90,
    "akash":80,
    "parthiv":100,
    "sam":98,
    "anzil":99
}

topper=max(students,key=students.get)
print("Topper is ",topper)
