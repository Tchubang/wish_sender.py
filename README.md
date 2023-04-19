# wish_sender.py
This Python script automates sending WhatsApp messages to multiple contacts using webbrowser, pyautogui, and time modules. It filters contacts based on a keyword, allows the user to remove specific contacts, and continues sending the message. This tool saves time for users sending messages to large groups.


This Python script automates sending messages to WhatsApp contacts using the pyautogui and webbrowser libraries. The script reads contact information from a text file and prompts the user to enter a greeting message. The user can filter contacts by entering a keyword to display only lines containing the keyword. The filtered contact information is displayed with index numbers, and the user can remove contacts by entering the corresponding index number.

The script uses the onelinedeleting() function to send the greeting message to each contact. The function uses keystrokes to type the message, press "tab," and then press "enter" twice. The removing_through_indexing() function removes a contact using the index number provided by the user and displays the updated contact information with re-assigned index numbers using the indexing() function. The function prompts the user to either continue sending messages or remove more contacts.

The Keyword_search() function prompts the user to remove contacts or continue sending messages. The script provides an efficient and simple way to send messages to specific WhatsApp contacts while allowing for filtering and removal of unwanted contacts. The use of keystrokes and automation libraries streamlines the messaging process and saves time and effort for the user.

Overall, this script provides a useful tool for sending messages to specific WhatsApp contacts and can be easily customized to fit individual needs.
