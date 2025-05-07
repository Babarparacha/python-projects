import random
import string 

def generate_password(length,use_lowercase,use_uppercase,use_numbers,use_special):
    chars=""
    if use_lowercase:
        chars+=string.ascii_lowercase
        #chars="abchfjdsfhuez"
    if use_uppercase:
        chars+=string.ascii_uppercase
    if use_numbers:
        chars+=string.digits
    if use_special:
        chars+=string.punctuation
    if not chars:
        print("oops! no character type selected using lower case by default")
        chars+=string.ascii_lowercase    
    password=""
    for i in range(length):
        password+=random.choice(chars)
    return password        
def check_password_strength(password):
    score=min(len(password)/16,1.0)
    has_lower=any( c.lower() for c in password)
    has_upper=any( c.upper() for c in password)
    has_digit=any( c.isdigit() for c in password)
    has_special=any( c in string.punctuation for c in password)
    variety=(has_lower+has_upper+has_digit+has_special)/4.0
    final_score=(score * 0.6)+(variety*0.4)
    if final_score>=0.8:
        return " 🔥 ultra strong"
    elif final_score>=0.6:
        return "💪Strong"
    elif final_score>=0.4:
        return "👍 Decent"
    else:
        return "Need Improvement"
  
def get_yes_no_input(question):
    while True:
        response=input(question+"y/n: ").lower()
        if response in ['yes','y']:
            return True
        elif response in ['no','n']:
            return False
        else:
            print("please enter y or n:")
def main():
    print("=== password generator===")
    print("=== create super strong adn secure password with ease===")
    while True:

        try:
            length=int(input("Enter password length(8-30)"))
            if 8<=length<=30:
                break
            else:
                print("Please choose a length between 8 and 30")

        except ValueError:
            print("oops! please enter number, like 12 or 16")    
    print("let customize your password")
    use_lowercase=get_yes_no_input("include lowercase letters(a-z)")        
    use_uppercase=get_yes_no_input("include uppercase letters(A-Z)")        
    use_numbers=get_yes_no_input("include numbers letters(0-9)")        
    use_special=get_yes_no_input("include special characters (!#@$%&/)")
    print("generating your magical password....")
    password=generate_password(length,use_lowercase,use_uppercase,use_numbers,use_special)
    print("=== your new password is==")
    strength=check_password_strength(password)
    print(f"{password}")
    print(f"password strength:{strength}")
    if get_yes_no_input("would you like to create another password:"):
        main()
    else:
        print("Thank for using the super fun password generator! stay secure")    
main()    