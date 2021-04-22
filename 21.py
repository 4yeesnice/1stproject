import pprint

data = [
    {'dress':[
                {'name':'louis vuitton',
                'popularity':500,
                 'price':1000
                },
                {'name':'versace',
                'popularity':21,
                 'price':888
                },
                {'name':'supreme',
                'popularity':57,
                 'price':765
                },
    ]
    },
    {'jeans':[
                {'name':'adidas',
                'popularity':42,
                 'price':2300
                },
                {'name':'armani',
                'popularity':678,
                 'price':110
                },
                {'name':'casio',
                'popularity':230,
                 'price':3000
                },
    ]
    },
    {'t-shirt':[
                {'name':'tom ford',
                'popularity':999,
                 'price':5000
                },
                {'name':'lacoste',
                'popularity':777,
                 'price':230
                },
                {'name':'luxury',
                'popularity':876,
                 'price':2300
                },
    ]
    }
]
list1 = ['dress','jeans','t-shirt']
i = 0
category_price = {}
for category in data:
    category_sum = 0
    key = list1[i]
    category_value = category[key]
    for product in category_value:
        category_sum += product['price']
    category_price[key] = category_sum
    i+=1
print(max(category_price.values()),category_price)

i = 0
category_popul = {}
for category in data:
    value_sum = 0
    key = list1[i]
    category_value = category[key]
    for product in category_value:
        value_sum += product['popularity']
    category_popul[key] = value_sum
    i+=1
print(max(category_popul.values()),category_popul)

money_list = []
name_list = []

i = 0
for category in data:
    key = list1[i]
    clothes = category[key]
    for money in clothes:
        bucks = money['price']
        money_list.append(bucks)

    for names in clothes:
        name_list.append(names['name'])
    i+=1
    # m = max(new_list)
    # x = new_list.index(m)
    # l = min(new_list)
    # y = new_list.index(l)
print(money_list, name_list)
dict.


