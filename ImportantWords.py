from multi_rake import Rake
import FileManager

def Find(text):
    rake = Rake()
    keywords = rake.apply(text)
    return (keywords[:10])

def Result():
    arr=[]
    for i in range(1 , 11):
        path = f"data/{i}.txt"
        text = FileManager.Read(path)
        arr.append(Find(text))
    return arr