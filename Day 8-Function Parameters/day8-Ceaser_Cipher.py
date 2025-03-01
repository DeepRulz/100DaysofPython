from day8art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
def inputdata():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    return direction,text,shift
def ceaser(t,s,e):
    cipher=""
    for i in t:
        if i in alphabet:
            key=alphabet.index(i)
            new_key=key+s if e=="encode" else key-s
            cipher+=alphabet[new_key]
        else: cipher+=i
    print(f"The {e+'d'} text is {cipher}")
    b=input("Type 'yes' if you want to go again, Otherwise type 'no'")
    if b=="yes":
        e,t,s=inputdata()
        ceaser(t,s,e)
    else:
        print("Goodbye")
di,te,sh=inputdata()
ceaser(te,sh,di)

