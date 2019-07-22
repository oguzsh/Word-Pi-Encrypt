pi = 3.14

alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter)) 

data = input("Metin: ").lower().replace(" ", "")

words=[]
for word in range(len(data)):
    words.append(data[word])
 
message = []   
for i in words:
    for j in alphabet:
        if(i == j):
            msg = alphabet.index(i) + 1
            message.append(msg)
    
enc_msg = (''.join(map(str, message)))
com_msg = int(enc_msg) * pi

print(" encode ")

print(com_msg)

print(" decode ")

print(com_msg / pi)
