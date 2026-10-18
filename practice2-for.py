# شمارش تعداد حروف صدا داردر یک کلمه
word=input("enter string:  ")
sound="Oo,Uu,Ee,Ii,Aa"
count=0
for i in word:
    if i in sound:  #یعنی بررسی کن که آیا این حرف در مجموعه حروف صدادار هست یا نه.
      count=count+1 #یعنی هر وقت حرف صدادار پیدا شد شمارنده رو یک واحد افزایش بده.
print("cout is:  ",count)