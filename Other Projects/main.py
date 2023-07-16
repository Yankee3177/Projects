import onetimepad

message = "We hate Adams"
cipher = onetimepad.encrypt(message,'random')

ptext = onetimepad.decrypt(cipher,'random')



print(cipher)
print(ptext)