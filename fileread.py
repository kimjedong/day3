with open('MYPAGE') as file:
    #content = file.read()
    content = file.readlines()



print(content)

num = 1
for line in content:
    print(str(num)+":"+line)
    num +=1