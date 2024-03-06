print("\nWelcome to the final stage of the quiz bowl game you have been playing for weeks on end by now!")
print("\nWe have 5 categories to chose from now! Database mgmt, Business stats, Marketing, Business application devolpement,\n and Business managment\n")
user_data = input(" Please chose a category and spell it exactly as I have above: ")
if user_data == "Database mgmt":
    print ("Welcome to the Database mgmt quiz bowl! ")
    #for
elif user_data == "Business stats":
    print ("Welcome to the Business stats quiz bowl! ")
elif user_data == "Marketing":
    print ("Welcome to the Marketing quiz bowl! ")
elif user_data == "Business application":
    print ("Welcome to the Business application quiz bowl! ")
elif user_data == "Business managment":
    print ("Welcome to the Business managment quiz bowl ")
else:
    print ("You spelled the categories wrong, please re-run the program and please look carefully how the categories are spelled. ")
