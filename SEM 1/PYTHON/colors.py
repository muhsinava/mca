c1=input("Enter list1 of colours=")
c1=c1.split(',')
c2=input("Enter list2 of colours=")
c2=c2.split(',')
print("colours are=",set(c1)-set(c2))