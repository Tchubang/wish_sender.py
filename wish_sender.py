import webbrowser
import pyautogui
import time

wish = input("Please provide us greeting: ")


def onelinedeleting(sample_string, wish):
    while sample_string:
        # Get the first line of the string
        first_line = sample_string.split('\n')[0]

        # Print the first line
        sending_mech(first_line, wish)

        # Remove the first line from the string
        remaining_string = '\n'.join(sample_string.split('\n')[1:])

        # Update the sample string to the remaining string
        sample_string = remaining_string


def sending_mech(a, b):
    # Print the first line
    url = "whatsapp://send?text=" + b
    url = "whatsapp://send?text=" + b
# Open the URL using the default browser
    webbrowser.open(url)


# Wait for a few seconds before sending the keystrokes
    time.sleep(3)

    # Type sending massage by using keystrokes
    pyautogui.typewrite(a)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)


# Open the file and read its contents
with open('contacts.txt', encoding="utf-8") as file:
    text = file.read()


keyword = input(
    "Enter the keyword or press enter to send every one: ")

# Use a list comprehension to filter out lines that do not contain the text "FN" or the keyword variable value


def checking_for_keysensitive():
    keyword_sensitive_or_not = input('''
Press 1 for case sensitive
Press 2 for none case sensitive
''')

    if keyword_sensitive_or_not == '1':

        lines = text.splitlines()
# Use a list comprehension to filter out lines that do not contain the text "FN" variable value
        lines_with_fn_and_keyword = [
            line for line in lines if "FN" in line and keyword in line]
        result = "\n".join(lines_with_fn_and_keyword)
        result = result.replace("FN:", "")
        return result

    elif keyword_sensitive_or_not == '2':
        lines = text.splitlines()
# Use a list comprehension to filter out lines that do not contain the text "FN" or the keyword variable value
        lines_with_fn_and_keyword = [
            line for line in lines if "FN" in line and keyword.lower() in line.lower()]
        result = "\n".join(lines_with_fn_and_keyword)
        result = result.replace("FN:", "")
        return result
    else:
        print("Please choose correct option: ")
        checking_for_keysensitive()


result = checking_for_keysensitive()


def indexing(result):
    for i, line in enumerate(result.split('\n'), start=0):
        print(f"{i}: {line}")


indexing(result)


def removing_through_indexing(new_string=None):
    if new_string is None:
        # or set it to some default value if new_string is not passed as an argument
        new_string = result

    a = input("Number of index? ")
    a = int(a)

    line = new_string.split('\n')

    line_removed = line.pop(a)

    # Join the remaining lines back into a string
    new_string = "\n".join(line)

    indexing(new_string)

    print("This contact is removed from the list", line_removed)
    Choose = input('''Please choose what to happen next
    1 = Continue the process
    2 = remove more contacts
    ''')

    if Choose == '1':
        onelinedeleting(new_string, wish)

    elif Choose == '2':
        # Call the function again and pass the updated value of new_string as an argument
        indexing(new_string)
        removing_through_indexing(new_string)


def Keyword_search():
    choose = input('''want to remove contacts?
     If Yes Then press 1 and then enter
     else press 2 and then enter to continue the process
     ''')
    if choose == '1':
        removing_through_indexing()
    elif choose == '2':
        onelinedeleting(result, wish)


Keyword_search()
