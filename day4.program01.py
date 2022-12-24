student=[[44,'prasad',75,87],[13,'Anju',82,79],[53,'Archu',72,80],[35,'vachan',86,85]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
