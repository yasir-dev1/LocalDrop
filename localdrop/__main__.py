import os
import click
import string
import random
import time
import json
import subprocess
import itertools
import cilent


current_dir = os.path.dirname(os.path.abspath(__file__))  
messages_path = os.path.join(current_dir, 'message.json')  

def encrypt(message, key):
    if len(key) != 4:
        raise ValueError("Key must be 4 characters long")
    
    for char in key:
        if not (char.isupper() or char.isdigit()):
            raise ValueError("Key must contain only uppercase letters and digits")
    
    encrypted = ""
    key_index = 0
    
    for char in message:
        if char.isalpha():
            current_key_char = key[key_index % 4]
            
            if current_key_char.isupper():
                key_shift = ord(current_key_char) - ord('A')
            else:
                key_shift = int(current_key_char)
            
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
            
            key_index += 1
        else:
            encrypted += char
    
    return encrypted

def generate_code(message):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(4))


@click.group()
def cli():
    pass

@click.command()
def init():
    current_dir = os.path.dirname(os.path.abspath(__file__))  
    messages_path = os.path.join(current_dir, 'message.json')  
    if not os.path.exists(messages_path):
        with open(messages_path, 'w') as file:
            file.write("{}")
    sender_path = os.path.join(current_dir, 'sender.py')
    subprocess.Popen(['cmd', '/c', f'start pythonw {sender_path}'])

@click.command()
@click.argument('message')
def send(message):
    if not os.path.exists(messages_path):
        print("Please initialize the LocalDrop Using 'localdrop init' first.")
    else:
        code = generate_code(message)
        c = code
        message_dict = {
            "expireTime":time.time() + 60,
            "message": code[0]+encrypt(message, c),
        }
        print(f"Your Code: {code}")
        with open(messages_path, 'w') as file:
            json.dump(message_dict, file, ensure_ascii=False, indent=4)

@click.command()
@click.argument('code')
def get(code):
    message = cilent.get_message_from_sender(code)
    if message:
        print(f"{message}")
    else:
        print("No message found for the given code.")

cli.add_command(init)
cli.add_command(send)
cli.add_command(get)

if __name__ == "__main__":
    cli()