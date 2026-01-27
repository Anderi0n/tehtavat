from hmac import new

number_list = []
while True:
    que = (input("give number: "))
    if que == (""):
        break
    quenum = int(que)
    number_list.append(quenum)
    number_list.sort(reverse=True)



print(number_list[:5])

