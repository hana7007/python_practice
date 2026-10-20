#یک رشته بگیر و تعداد تکرار هر حرف را در یک دیکشنری برگردان
def count_charcter(sentens):
    dic_charcter={}  # creat empty Dictionary 
    for char in sentens:
       dic_charcter[char]= dic_charcter.get(char,0)+1# نتیجه را در دیکشنری ذخیره می‌کند
       #این متد مقدار مربوط به کلید رااز دیکشنری می‌خواند.
       #اگر حرف تکرای وجود نداشته باشد، مقدار پیش‌فرض 0 را برمی‌گرداند.
      # اگر حرف تکراری وجود داشته باشد، تعداد فعلی آن را برمی‌گرداند.
    return dic_charcter
text=input("please enter a word: ")
print(count_charcter(text))

