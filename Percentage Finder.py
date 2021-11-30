list = []
Subjects = int(input("Tell the Number of Subjects: "))
for i in range(0,Subjects):
    Marks = int(input("Enter your marks: "))
    list.append(Marks)
listsum = (sum(list))
solution = listsum / Subjects
print (solution)
    
