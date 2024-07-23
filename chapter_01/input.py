name=input("enter student name:")
if name=="naina":
    medichem=int(input("Medicinal chemistry :" ))
    pathology=int(input("Pathology :"))
    pharmaceutics=int(input("Pharmaceutics :"))
    inorganic=int(input("Inorganic chemistry :"))
    physiology=int(input("Physiology :"))
    total=medichem+pathology+pharmaceutics+inorganic+physiology
    print("total marks obtain :" ,total, "out of 500")
    percentage=total/5
    
    print("total per obtain :",percentage)
    sgpa=(percentage/10)+0.5
    print("semester 1 sgpa:",sgpa)
    if percentage>=40:
        print ("Congratulation dear...",name)
    
    
else:
    print("wrong user")