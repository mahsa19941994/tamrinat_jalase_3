import Tokenization
import Entropy
import ImportantWords
import WordCloude
import Matrix

arr=Tokenization.Result()
print("پیش پردازش")
for i in range(0, 10):
    print(arr[i])
print("----------------------------------------------------------------------------")
arr = ImportantWords.Result()
print("فراوانی تعداد کلمات کلیدی")
for i in range(0 , 10):
    print(arr[i])
print("------------------------------------------------------------------------------")

a=[]
b=[]
print("آنتروپی")
for i in range(0 , 10):
    for j in range(0 , len(arr[i])):
        b = arr[i][j][0].split(" ");
        for k in range(0 , len(b)):
            a.append(b[k])
    print(Entropy.eta(a))
    a=[]
print("-------------------------------------------------------------------------------")
for i in range(1 , 11):
    WordCloude.Result(f"data/{i}.txt")

Matrix.result()