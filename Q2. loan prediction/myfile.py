def search(d):
    n = input("enter the seacrh key: ")
    if n in d:
        print("record found")
        print("name:",n)
        print("age: ",d[n]['age'])
        print("address: ",d[n]['addre'])

    else:
        print("recored not found")