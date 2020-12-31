from PySimpleGUI import PySimpleGUI as sg
from cryptography.fernet import Fernet

cryptography_key = b'ZXH4IVKgAdcena7QnkLkaxi4igieGDT9lJ5gJRJAtS4=' # Change this key

def encrypt_text(text, cryptography_key):

    cipher_suite = Fernet(cryptography_key)
    encoded_text = bytes(text, 'utf-8') # Encode to bytes utf-8
    encrypted_text = cipher_suite.encrypt(encoded_text) #required to be bytes

    return encrypted_text.decode("utf-8")


def decrypt_text(encrypted_text, cryptography_key):

    try:

        encoded_text = bytes(encrypted_text, 'utf-8')

        cipher_suite = Fernet(cryptography_key)
        ciphered_text = encoded_text
        unciphered_text = (cipher_suite.decrypt(ciphered_text))

        text = bytes(unciphered_text).decode("utf-8") # convert to string

        return text
    except:
        return('get_unverified_token_data')

def key_generate():

    key = Fernet.generate_key()

    key_decoded_in_string = key.decode('utf-8')
    return key_decoded_in_string

# Layout 
layout_title = 'Rodolfho Crypto Tool'
sg.theme('Reddit')
layout = [
    [sg.Text('Enter something:'), sg.Input(key='text', size=(70,0))],
    [sg.Text('', key='', size=(0,0))],
    [sg.Button('Encrypt'), sg.Button('Decrypt'), sg.Button('Generate Key')],
    [sg.Text('Result:', key='out', size=(30,0))],
    [sg.Output(size=(90,20), key = '_output_')],
    [sg.Button('Clear Output'), sg.Text('version: 0.3')]
    ]

# Windows
window = sg.Window(layout_title, layout)

# Read Events
while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break

    if events == 'Encrypt':

        msg = values['text']
        msg = (encrypt_text(msg, cryptography_key))
        
        print(f"Result: {msg}")
        print("")

    if events == 'Decrypt':

        msg = values['text']
        msg = (decrypt_text(msg, cryptography_key))
        
        
        if msg ==  'get_unverified_token_data':
            print(f"ERROR: {msg}")
        
        else:
            print(f"RESULT: {msg}")

    if events == 'Generate Key':
        
        print(f"Key: {key_generate()}")
        print("")
        
    if events == 'Clear Output':
        window.FindElement('_output_').Update('')
        
