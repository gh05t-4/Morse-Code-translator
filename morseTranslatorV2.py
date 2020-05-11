# Morse Translator by gh05t-4

print("\t\tMorse Code Translator\n")
print("""Choose the option:
    1) Encrypt
    2) Decrypt""")
opt = str(input("Option: "))

morse_chart = {     'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'
              } 


# Function to encrypt the message
if opt == '1':
        message = input("\nEnter the message to translate: ")
        message = message.upper()
        cipher = '' 
        for letter in message: 
            if letter != ' ':
                cipher += morse_chart[letter] + ' '
            else: 
                cipher += ' '
        print("\nMorse Code: "+cipher)

# Function to decrypt the morse code 
elif opt == '2':
            message = input("\nEnter the morse code to translate: ")
            message += ' '
  
            decipher = '' 
            citext = '' 
            for letter in message: 
  
                if (letter != ' '): 
                    i = 0 
                    citext += letter 
   
                else: 
                    i += 1
  
                    if i == 2 :  
                        decipher += ' '

                    else: 
                        decipher += list(morse_chart.keys())[list(morse_chart .values()).index(citext)] 
                        citext = '' 

            print("\nPlain Text: "+decipher)


else:
        print("Invalid option.")
