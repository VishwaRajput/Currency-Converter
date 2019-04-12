dire={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}
num=int(input("Enter any number of four digit: "))
if (num in dire)==True:
    print (dire[num])
elif num>100 and num<1000:
    a=num//100
    b=num%100
    c=b//10
    d=b%10
    print(dire[a],dire[100],dire[c*10],dire[d])
elif num<100:
    a=num//10
    b=num%10
    print(dire[a*10],dire[b])
elif num>1000:
    a=num//1000
    b=num%1000
    c=b//100
    d=b%100
    e=d//10
    f=d%10
    if c!=0:
        print(dire[a],dire[1000],dire[c],dire[100],dire[e*10],dire[f])
    else:
        print(dire[a],dire[1000],dire[e*10],dire[f])

