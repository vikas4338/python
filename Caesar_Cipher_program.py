print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
''')

# this method convers message to desired format
# if isEncode is 'True' then encrypt or decrypt
def TextToCipherAndViceVersa(message_to_convert, isEncode):
    output_message = ""
    for char in message_to_convert:
        # Skip numeric / spaces or special chars (not char.isalnum())
        if char.isnumeric() or char.isspace() or not char.isalnum():
            output_message += char
            continue

        # if char is lowercase then we need to subtract base as 97 else 65
        if char.islower():
            if isEncode:
                output_message += chr((ord(char) - 97 + shift_number) % 26 + 97)
            else:
                output_message += chr((ord(char) - 97 - shift_number) % 26 + 97)
        elif char.isupper():
            if isEncode:
                output_message += chr((ord(char) - 65 + shift_number) % 26 + 65)
            else:
                output_message += chr((ord(char) - 65 - shift_number) % 26 + 65)
    return output_message


while True:
    action = input("Type \"Encode\" to encrypt or \"Decode\" to decrypt ").upper()
    if action not in ("ENCODE", "DECODE"):
        print("Invalid option selected")

    message_to_convert = input(f"Please type the message you want to process as per {action} ")
    shift_number = int(input("Please enter \"shift number\" "))
    print(f"Message: {message_to_convert}")
    print(f"Action is {action}")
    print(f"Shift Number: {shift_number}")

    output_message = TextToCipherAndViceVersa(message_to_convert, action == "ENCODE")

    print(f"Output message as per {action}: {output_message}")

    # Check if user want to continue with Encode / Decode process
    want_to_continue = input("Do you want to continue with \"Encode / Decode process\" ? "
                             "Please type in \"yes/y\" or \"no/n\" ")
    if want_to_continue.upper() not in ("YES", "Y"):
        break
