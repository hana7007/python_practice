#palindrom بدست اوردن برعکس کلمه
word=input("please enter a world: ")
def palindrome_word():
    return word[: :-1] #word[start:stop:step]  slicingبا ایندکس کار میکنه -1 یعنی عقبی بیا جای خالی اول یعنی ازاول شروع کن
print(" word's palindrome: ",palindrome_word())
