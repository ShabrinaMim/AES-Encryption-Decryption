if __name__ == '__main__':

    import os
    import time
    import aes

    print('Key:')
    inputKey = input() 
    inputValue = str.encode(inputKey)
    for x in inputValue: 
        print(format(x,'x'),end = " ")
    print('\n') 
    print('Plain Text:')  
    myText = input()   
    plainText = str.encode(myText)
    for x in plainText: 
        print(format(x,'x'),end = " ")
    print('\n') 
    encryptedText = []
    temp = []
    for i in plainText:
        temp.append(i)
    if len(temp) == 16:
        encryptedText.extend(aes.encryptionFunction(temp, inputKey))
        del temp[:]
    else:
        emptySpaces = 16 - len(temp)
        for i in range(emptySpaces - 1):
            temp.append(0)
        temp.append(1)
        encryptedText.extend(aes.encryptionFunction(temp, inputKey))
    print('Cipher Text:')
    for x in encryptedText:
        print(format(x,'x'),end = " ")
    print('\n')
    print("".join(map(chr,encryptedText)))
    #decription part
    decryptedText = []
    decryptedText.extend(aes.decryptionFunction(encryptedText, inputKey))
    print('Deciphered Text:')
    for x in decryptedText: 
        print(format(x,'x'),end = " ") 
    print('\n')  
    print("".join(map(chr,decryptedText)))
    print('\n') 
    print('Execution Time')
    print('Key Scheduling: %s seconds'%(aes.time_afterKeyExpansion))
    print('Encryption Time: %s seconds'%(aes.time_afterEncryptionTime))
    print('Decryption Time: %s seconds'%(aes.time_afterDecryptionTime))
