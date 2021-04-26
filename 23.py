name = input("name")
def operation(quantity):
    cash = int(input('cash'))
    overall = price*quantity
    change = cash - overall
    if change>=0:
        return overall
    else:
        print("van nehvataet cash")
        return -change
def search(name):
    if name in data:
        print(data[name])
        return data[(name)]
    else:
        print(":(")
        return None
data = {
    'glock.20':2000,
    'usp':2500,
    'fs':3467,
    'deagle':5000,
    'p92':4000,
    'colt':90000,
    'magnum':6000,
    'p90':10000,
    'mp7':11000,
    'uzi':12000,
    'mp5':14000,
    'm16':20000,
    'ak-47':19000,
    'm416':24000,
    'famas':21000,
    'AWM':30000,
    'Dragunov':31000,
    'Barett':50000,
    'RPG':100000,
    'Topol-M':2000000
}
price = search(name)

greet = int(input("1 if buy, 2 if not buy:"))
quantity = int(input("kol-vo"))
if greet == 1:
    total = {
        (name): quantity,
        "total": operation(quantity)
    }
    print(total)


"""
ТЗ:
По данным введенным пользователем вычислить, сможет он купить выбранный им товар или нет.
Если товар в списке отсутствует - NOT OK
__________
Входные данные: название товара,кол-во товара, наличные
Реализовать 2+ функциями
Выходные данные: словарь состящий из: 
{названия товара как ключ:кол-во, следующий элемент - потраченная сумма - ключ, значение сумма}
"""


