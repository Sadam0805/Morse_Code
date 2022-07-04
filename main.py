
morse_dic = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
             'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
             'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
             'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'}

decode_morse_dic = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
                    '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
                    '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
                    '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
                    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' '}

# single text
# check = input("Enter a Text: ").lower()
# print(morse_dic[check])

# decode morse code single text
# check = input("Enter a decode Text: ")
# print(decode_morse_dic[check])

choose = input("Do You Want to type 'Normal Text' or 'Morse Decode' using '.-'? (eg: Normal or Decode): ").title()

if choose == 'Normal':
    check = input("Enter a Word: ").lower()
    word = ''
    for i in check:
        word += f'{morse_dic[i]} '
    print(word)

elif choose == 'Decode':
    check = input("Enter a decode Word: ").split(' ')
    word = ''
    for i in check:
        word += decode_morse_dic[i]
    print(word)

else:
    print("Sorry! Try again")
