# SEZAR ŞİFRELEME
key = int(input("Şifre Anahtarı Giriniz: "))
def encrypted_message():
    encrypted_message = ""

    alphabet = ["a" , "b" , "c" ,"ç" ,"d" , "e" , "f" , "g" , "h" , "ı" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "ö" , "p" , "q" , "r" , "s" , "ş" , "t" , "u" , "ü" , "v" , "w" , "x" , "y" , "z"]


    message = input("Mesajınızı giriniz: ")
    for i in message:
        encrypted_message += alphabet[(alphabet.index(i) + key) % 32]

    print(encrypted_message)

    return encrypted_message

def main():
    encrypted_message()
    print("Şifreli mesajınız: " + encrypted_message())
main()

        