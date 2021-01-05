import Tokenization

def result():
    text = Tokenization.Result()
    arr=[]
    n=[]

    for i in range(0 , 10):
        for j in range(0 , len(text[i])):
            pl=Exists(arr , text[i][j])
            if(Exists(arr , text[i][j])):
                n[Exists(arr , text[i][j])]=f"{1+int(n[Exists(arr , text[i][j])])}"
            else:
                arr.append(text[i][j])
                n.append(1)
        print(f"\nFile{i+1}")
        for i in range(0 , len(arr)):
            print(f"{arr[i]}  {n[i]}")
        arr=[]
        n=[]

def Exists(a , word):
    for i in range(0 , len(a)):
        if(a[i]==word):
            return i;
    return False;