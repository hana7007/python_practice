# کاراکترهایی را از یک رشته حذف کند. به این‌صورت که از کاراکتر اول شروع کرده و تا موقعیت
def remove(word,n):#پارامترn، مشخص‌کننده تعداد کاراکترهایی است که می‌بایست از ابتدای کلمه مورد نظر حذف شوند
    x=word[n:]  #یعنی  از ان شروع کن و تا اخر ادامه بده و برش  کن   «برش‌زنی رشته» (String Slicing) 
    return x
text=input("please enter word: ")
num=int(input("please enter a number: "))
print(remove(text,num))
