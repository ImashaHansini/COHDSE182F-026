alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
cc = ''
ctext = input("Enter your text to be convert to cipher : ")
for c in ctext :
    if c in alphabet :
        cc += alphabet[(alphabet.index(c)+key)%(len(alphabet))]
print("Encrypted Text is : "+cc)
ntext = input("Enter your cipher text to be convert to normal text : ")
for n in ntext :
    if n in alphabet :
        cc += alphabet[(alphabet.index(n)-key)%(len(alphabet))]
print("Decrypted Text is : "+cc)
