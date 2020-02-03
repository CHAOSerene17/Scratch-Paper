attributes = ["tall", "nice", "old"]

for characteristics in attributes:
   answer = input("Are you " + characteristics + "? Print yes/no. \n")
   if answer == "yes":
       print("That's good to know.\n")
   else:
        print("That's too bad.\n")