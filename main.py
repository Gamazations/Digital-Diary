#Creates the function that allows the user to create and read the diary
def DigitalDiary():
  #Clears all the data values used in the function for each use
  diaryInput = " "
  wantToContinue = " "
  diarySetting = " "
  setCharacters = " "
  howManyCharacters = " "
  #Asks the user what they want to do with the diary
  diarySetting = input("What would you like to do with your diary? (Write, Read, or Delete): ")
  #If the user wants to write in the diary, it will append new values to the bottom or create a new file if not already existing and add values inputted by the user
  if diarySetting == "Write":
    #Opens the diary to edit
    diary = open("diary.txt", "a")
    #Asks the user for inputs for the diary
    diaryInput = input("What do you want to write in your diary?: ")
    #Adds these inputs into the diary to a new line for organization
    diary.write("\n" + diaryInput)
    #Closes the file
    diary.close()
    #Asks the user if they want to continue, if they do, it allows the user to continue, if they don't it gives the user a farewell message.
    wantToContinue = input("Want to continue using your diary? (Y/N): ")
    if wantToContinue == "Y":
      functionOne()
    else: 
      print("Have a good day!")
  #If the user wants to read the diary, it will give the user options on how to read the diary
  if diarySetting == "Read":
    #Asks the user if they want to read the entire diary or only a set amount of characters (EXTRA)
    setCharacters = input("Do you want to read your entire diary or a set amount of characters? (Entire/Set Amount): ")
    #If they choose the entire diary, it will read the user the entire file
    if setCharacters == "Entire" or setCharacters == "entire":
      #Opens the file
      diary = open("diary.txt", "r")
      #Sets all the content of the diary into a variable
      diaryContent = diary.read()
      #Prints the variable for the user to read
      print(diaryContent)
      #Closes the file
      diary.close()
      #Asks the user if they want to continue, if they do, it allows the user to continue, if they don't it gives the user a farewell message.
      wantToContinue = input("Want to continue using your diary? (Y/N): ")
      if wantToContinue == "Y":
        DigitalDiary()
      else:
        print("Have a good day!")
    #If they choose a set amount of characters, it will ask the user for how many characters it should read up to (EXTRA)
    elif setCharacters == "Set Amount" or setCharacters == "set amount":
      #Gets the amount of characters via input from the user
      howManyCharacters = int(input("Enter the amount of characters you want to read from your diary: "))
      #Opens the file
      diary = open("diary.txt", "r")
      #Sets the content of the set amount of characters from the file into a variable
      diaryContent = diary.read(howManyCharacters)
      #Prints the variable for the user to read
      print(diaryContent)
      #Closes the file
      diary.close()
      #Asks the user if they want to continue, if they do, it allows the user to continue, if they don't it gives the user a farewell message.
      wantToContinue = input("Want to continue using your diary? (Y/N): ")
      if wantToContinue == "Y":
        DigitalDiary()
      else:
        print("Have a good day!")  
  #If the user wants to clear out the diary, it simply clears the entire file
  if diarySetting == "Delete":
    #Opens the file and then clears all the data with .close()
    diary = open("diary.txt", "w").close()
    #Lets the user know that their diary has been cleared
    print("Your diary entries have been deleted!")
    #Asks the user if they want to continue, if they do, it allows the user to continue, if they don't it gives the user a farewell message.
    wantToContinue = input("Want to continue using your diary? (Y/N): ")
    if wantToContinue == "Y":
      DigitalDiary()
    else:  
      print("Have a good day!")
    
#Initially runs the function so the program can start.
DigitalDiary()
