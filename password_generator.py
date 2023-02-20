# defining function of generate_password using mudules, random and string

import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

# lettersは、文字の事で、それをcharactersに定義しなおしている
# そしてnumbersは、文字と数字の組み合わせ、special_charactersは文字と特別な文字との組み合わせだと定義している
    characters = letters
    if numbers:
        characters+= digits
    if special_characters:
        characters += special

#　はじめの状態
    pwd =""
    meets_criteria = False
    has_number = False
    has_special = False

# パスワードがつくられる過程（meet_criteriaの基準がみたされていない、または文字の長さが最短よりながくなるまで、characterを作り続ける）
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        # ここのrandomがmoduleでランダムに数字を選ぶことができる
        pwd += new_char
        # ここで、パスワードはつくられた新しい文字とあわさり、pwdに追加される 


# ここでどのような新しい文字がどのような状態だとnumberをもっていることになるのか、special charactersをもっていることになるのかをきめている
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special= True


#　numbersだけ、charactesだけ、両方、両方なしのどの選択になっても、meets_criteriaはTrueになっている。それがfalseになるまで、新しいパスワードがつくられる。→エラーを防ぐため
        meets_criteria = True 
        if numbers:
            meets_criteria = has_number

        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd
 


min_length =int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)?").lower()=="y"
# 何をうっても、lowercaseになるようにする。pythonでは、yはyes、nはnoをいえる
has_special = input("Do you want to have special characters (y/n))?").lower()=="y"
pwd= generate_password(min_length, has_number, has_special)
print ("The generated password is:", pwd)


