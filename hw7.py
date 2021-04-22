data = [
    {'text':'oh hi duuuude how r uy??check this 1xbet'},
    {'text':'Dear Harry Potter, i am Frodo Baggins i represent 1xbet company.Best bet service'},
    {'text':'wooooh yoow harry look at my jackpot 100000000$ at 1xbet service'},
    {'text':'Harry , today i saw the man who looks like Hawkeye from Avengers on 100% and he dont use 1xbet service'},
]
final_mail = 'Hello Harry, my name is Maksim, Im still waiting for the letter from Hogwarts 1XBET'
f = []
sp_sentence = 0
res_mail = 0
for i in data:
   sp_sentence = i['text'].lower().split()
   f.extend(sp_sentence)
new_list = []
ban_word_list = []
ban_word = 0
for i in f:
    count = f.count(i)
    if count>1:
        ban_word_list.append(i)
for i in ban_word_list:
    if ban_word_list.count(i)>=4:
        ban_word = i
print(ban_word)
final_mail = final_mail.lower()
if ban_word in final_mail:
    print("spam")
    res_mail = final_mail.replace(ban_word,"")
    res_mail = res_mail.lower()
else:
    print("not spam")
print(res_mail)