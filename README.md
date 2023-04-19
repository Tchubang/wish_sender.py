This is a Python script that uses the pyautogui and webbrowser libraries to automate the process of sending messages to contacts on WhatsApp.

The user is prompted to input a greeting message, and then the script reads a text file called "contacts.txt" that contains contact information. The user is prompted to enter a keyword, and the script filters the contact information to only include lines that contain the keyword.

The filtered contact information is then displayed with an index number assigned to each line. The user can choose to remove a contact by entering the index number of the line that they want to remove.

The script uses the onelinedeleting() function to send the greeting message to each contact. For each line of the filtered contact information, the script types the message, presses the "tab" key, and then presses the "enter" key twice to send the message to the contact on WhatsApp.

The removing_through_indexing() function removes a contact by using the index number provided by the user to remove the corresponding line from the filtered contact information. The function then calls indexing() to display the updated filtered contact information with the index numbers reassigned. The user can choose to either continue sending messages to the remaining contacts or remove more contacts.

The Keyword_search() function prompts the user to either remove contacts or continue sending messages to the remaining contacts.

Overall, the script provides a simple and efficient way to send messages to specific contacts on WhatsApp using Python.

