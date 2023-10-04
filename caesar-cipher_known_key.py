def encryption():
    encm = ""
    msg = input("Enter the original message:\n")
    shift = int(input("Enter the shift number:\n"))
    for i in range(len(msg)):
        pc = msg[i]
        pos = 0
        if pc in cap:
            while pc != cap[pos]:
                pos += 1
            pos = (pos + shift) % 26
            encm += cap[pos]
        elif pc in sm:
            while pc != sm[pos]:
                pos += 1
            pos = (pos + shift) % 26
            encm += sm[pos]
        elif pc in num:
            while pc != num[pos]:
                pos += 1
            pos = (pos + shift) % 10
            encm += num[pos]
        elif pc in spch:
            while pc != spch[pos]:
                pos += 1
            pos = (pos + shift) % 28
            encm += spch[pos]
        else:
            encm += pc
    print(f"Encrypted message is...\n{encm}")

def decryption():
    orm = ""
    msg = input("Enter the encrypted message:\n")
    shift = int(input("Enter the shift number:\n"))
    for i in range(len(msg)):
        pc = msg[i]
        pos = 0
        if pc in cap:
            while pc != cap[pos]:
                pos += 1
            pos = (pos - shift) % 26
            if pos < 0:
                pos += 26
            orm += cap[pos]
        elif pc in sm:
            while pc != sm[pos]:
                pos += 1
            pos = (pos - shift) % 26
            if pos < 0:
                pos += 26
            orm += sm[pos]
        elif pc in num:
            while pc != num[pos]:
                pos += 1
            pos = (pos - shift) % 10
            if pos < 0:
                pos += 10
            orm += num[pos]
        elif pc in spch:
            while pc != spch[pos]:
                pos += 1
            pos = (pos - shift) % 28
            if pos < 0:
                pos += 28
            orm += spch[pos]
        else:
            orm += pc
    print(f"Decrypted message is...\n{orm}")
sm = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
spch = ['!','@','#','$','^','&','*','(',')','_','','+','=','[',']','{','}','|',':',';',',','/','?','<','>','₹','%','"']
cap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['1','2','3','4','5','6','7','8','9','0']
run = True
while(run):
    ch = input("Choices are...\n 1. Encrypt\n 2. Decrypt\n Enter any other key to exit\nEnter your choice:\n")
    if ch == '1':
        encryption()
    elif ch == '2':
        decryption()
    else:
        run = False
