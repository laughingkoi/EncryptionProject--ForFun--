import random
import json
import time

Character_Set = {
    # Lowercase letters
    'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e',
    'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j',
    'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o',
    'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't',
    'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z',

    # Uppercase letters
    'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E',
    'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J',
    'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O',
    'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T',
    'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z',

    # Numbers
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
    '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',

    # Common symbols
    ' ': ' ', '!': '!', '"': '"', '#': '#', '$': '$',
    '%': '%', '&': '&', "'": "'", '(': '(', ')': ')',
    '*': '*', '+': '+', ',': ',', '-': '-', '.': '.',
    '/': '/', ':': ':', ';': ';', '<': '<', '=': '=',
    '>': '>', '?': '?', '@': '@', '[': '[', '\\': '\\',
    ']': ']', '^': '^', '_': '_', '`': '`', '{': '{',
    '|': '|', '}': '}', '~': '~',
}

Password_Set = {
    # Lowercase letters
    'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e',
    'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j',
    'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o',
    'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't',
    'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z',

    # Uppercase letters
    'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E',
    'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J',
    'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O',
    'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T',
    'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z',

    # Numbers
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
    '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
}

Character_List = list(Character_Set.keys())
Password_List = list(Password_Set.keys())

def Generate():
    Encrypted_Character_Set = {}
    Characterchanged=[]
    CharacterUsed=[]
    exceptions=[]
    key=""
    for i in range(len(Character_List)):
        all_numbers = set(range(1, 96))
        allowed_numbers = list(all_numbers - set(exceptions))
        IntergerChosen = random.choice(allowed_numbers)
        exceptions.append(IntergerChosen)
        Encrypted_Character_Set[Character_Set[Character_List[i-1]]] = Character_List[IntergerChosen-1]
        CharacterUsed.append(Character_List[IntergerChosen-1])
        Characterchanged.append(Character_List[IntergerChosen-1])
    #Generating Key
    for i in range(10):
        number = random.randint(1, 63)
        key = key + Character_List[number]
    print("Your Encryption Key is:", key)
    with open(f"{key}.json", "w") as file:
        json.dump(Encrypted_Character_Set, file)

def Encrypt():
    Encrypted_Text = ""
    Encrypted_Character_Set = {}
    Encrypted_List = []
    Text = input("Enter Text Here For Encryption: ")
    Text = Text.replace('\u2018', "'").replace('\u2019', "'").replace('\u201C', '"').replace('\u201D', '"').replace(
        '\u2026', '...')
    Key = input("Enter The Key: ")
    with open(f"{Key}.json", "r") as file:
        Encrypted_Character_Set = json.load(file)
    TextLength = len(Text)
    TextList = []
    for i in range(TextLength):
        TextList.append(Text[i])
    for i in range(len(TextList)):
        Encrypted_List.append(Encrypted_Character_Set[TextList[i]])
    for i in range(len(TextList)):
        Encrypted_Text += Encrypted_List[i]
    print(Encrypted_Text)

def Decrypt():
    Encrypted_Character_Set = {}
    Decrypted_Character_Set = {}
    Encrypted_Character_Set_Keys = []
    Encrypted_Character_Set_Values = []
    Encrypted_List = []
    Decrypted_List = []
    Decrypted_Text = ""
    Text = input("Enter Encrypted Text Here For Decryption: ")
    Key = input("Enter The Key: ")
    with open(f"{Key}.json", "r") as file:
        Encrypted_Character_Set = json.load(file)
    for i in range(len(Text)):
        Encrypted_List.append(Text[i])
    for ke, values in Encrypted_Character_Set.items():
        Decrypted_Character_Set[values] = ke
    for i in range(len(Encrypted_List)):
        Decrypted_List.append(Decrypted_Character_Set[Encrypted_List[i]])
    for i in range(len(Decrypted_List)):
        Decrypted_Text += Decrypted_List[i]
    print("Your Decrypted text is:", Decrypted_Text)



def Main():
    print("Select your choices: ")
    print("[1] Generate Key")
    print("[2] Encrypt")
    print("[3] Decrypt")
    print("[4] Exit")
    Choice = int(input("Enter your choice: "))
    if Choice == 1:
        Generate()
    elif Choice == 2:
        Encrypt()
    elif Choice == 3:
        Decrypt()
    elif Choice == 4:
        exit()
    else:
        print("Invalid choice")

while True:
    Main()
    time.sleep(1)