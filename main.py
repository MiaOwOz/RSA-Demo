from myRSA import RSA
import tkinter as tk
from hashlib import md5

p = 11
q = 13

rsa = RSA(p, q)
keys = rsa.construct_keys()

def runCryptCommand():
    message = clearTextInput.get('1.0', tk.END)

    # 1 is encrypt
    # it was once here. when I added hashing, I decided to put it as the else. otherwise I'd have to restructure
    # the whole code, lol.
    if selection.get() == 2:
        # RSA#encrypt takes a string and returns an encrypted list of integers representing the encrypted characters
        encrypted_list = rsa.encrypt(keys[0], message)

        # Insert the numbers from the list into the fitting text field to view on the GUI
        cryptedListInput.config(state=tk.NORMAL)
        cryptedListInput.delete('1.0', tk.END)
        cryptedListInput.insert('1.0', encrypted_list)
        cryptedListInput.config(state=tk.DISABLED)
        
        # concatenate the list of numbers into a string to show in the GUI
        encrypted_message = ""

        for i in encrypted_list:
            encrypted_message += chr(i)

        # Put the final string onto the GUI
        cryptedTextInput.config(state=tk.NORMAL)
        cryptedTextInput.delete('1.0', tk.END)
        cryptedTextInput.insert('1.0', encrypted_message)
        cryptedTextInput.config(state=tk.DISABLED)
    elif selection.get() == 3:
        # Take the encrypted message and create an integer list of it
        message_list = []
        for c in message:
            message_list.append(ord(c))

        # Decrypt the integer list
        decrypted_list = rsa.decrypt(keys[1], message_list)

        # Show the decrypted list on the GUI
        cryptedListInput.config(state=tk.NORMAL)
        cryptedListInput.delete('1.0', tk.END)
        cryptedListInput.insert('1.0', decrypted_list)
        cryptedListInput.config(state=tk.DISABLED)
        
        # Create the decrypted message from the decrypted list
        decrypted_message = ""

        for i in decrypted_list:
            decrypted_message += chr(i)

        # Show the decrypted message on the GUI
        cryptedTextInput.config(state=tk.NORMAL)
        cryptedTextInput.delete('1.0', tk.END)
        cryptedTextInput.insert('1.0', decrypted_message)
        cryptedTextInput.config(state=tk.DISABLED)
    else:
        cryptedListInput.config(state=tk.NORMAL)
        cryptedListInput.delete('1.0', tk.END)
        cryptedListInput.insert('1.0', "Not supported for this operation")
        cryptedListInput.config(state=tk.DISABLED)

        cryptedTextInput.config(state=tk.NORMAL)
        cryptedTextInput.delete('1.0', tk.END)
        cryptedTextInput.insert('1.0', md5(message.encode()).hexdigest())
        cryptedTextInput.config(state=tk.DISABLED)

# Create the TK window
tkWindow = tk.Tk()
tkWindow.title('RSA Encryption Example')
tkWindow.geometry('400x600')

# selection is needed for the radio button, it stores the currently selected radio button as an int (decided by the value argument of each radio button)
selection = tk.IntVar()
selection.set(1) # Set default selection, in this case, encrypt

# Initialize UI components
chooseTypeLabel = tk.Label(tkWindow, text="Select the operation you want to do:")
chooseTypeLabel.place(x=0, y=0)

md5Radiobutton = tk.Radiobutton(tkWindow,
                                text="MD5",
                                variable=selection,
                                value=1)
md5Radiobutton.place(x=0, y=20)

encryptRadiobutton = tk.Radiobutton(tkWindow,
                                    text="Encrypt",
                                    variable=selection,
                                    value=2)
encryptRadiobutton.place(x=60, y=20)

decryptRadiobutton = tk.Radiobutton(tkWindow,
                                    text="Decrypt",
                                    variable=selection,
                                    value=3)
decryptRadiobutton.place(x=135, y=20) # I hate frontend development, ugh fucking magical position values

textToCryptLabel = tk.Label(tkWindow, text="Input the text you want to encrypt:")
textToCryptLabel.place(x=0, y=50)

clearTextInput = tk.Text(tkWindow, width=50, height=10)
clearTextInput.place(x=0, y=70)

# command takes the name of the function that's called when the button is pressed
buttonGo = tk.Button(tkWindow, text="GO!", command=runCryptCommand)
buttonGo.place(x=0, y=210)

cryptedListLabel = tk.Label(tkWindow, text="Crypted list view:")
cryptedListLabel.place(x=0, y=250)

cryptedListInput = tk.Text(tkWindow, state=tk.DISABLED, width=50, height=10)
cryptedListInput.place(x=0, y=280)

cryptedTextLabel = tk.Label(tkWindow, text="Crypted text view:")
cryptedTextLabel.place(x=0, y=430)

cryptedTextInput = tk.Text(tkWindow, state=tk.DISABLED, width=50, height=10)
cryptedTextInput.place(x=0, y=450)

# Run event loop
tkWindow.mainloop()