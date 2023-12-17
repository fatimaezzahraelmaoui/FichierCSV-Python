import csv 
fichier = open("annuaire.csv","w")
ecrivaisCSV = csv.writer(fichier,delimiter=";")

ecrivaisCSV.writerow(["ali","salhi",12])
ecrivaisCSV.writerow(["kawtar","maoui",14])
ecrivaisCSV.writerow(["hafssa","srbani",45])
ecrivaisCSV.writerow(["monir","hassani",20])
fichier.close()
