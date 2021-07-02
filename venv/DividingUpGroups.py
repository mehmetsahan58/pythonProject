
Num_Of_People = int(input("Number of People: "))
People_Per_Groups = int (input("Number of Groups: "))

Groups = Num_Of_People // People_Per_Groups

People_Left = Num_Of_People % People_Per_Groups

print ("There are " + str(Groups) + " groups with " + str(People_Left) + " leftover")