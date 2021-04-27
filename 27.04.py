data = [
    {'user': 'digital', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'sam', 'email': 'digital', 'age': 23, 'salary': 200000, 'department': 'manager'},
    {'user': 'john', 'email': 'john@google.com', 'age': 23, 'salary': 200000, 'department': 'CEO'},
    {'user': 'sparrow', 'email': 'digital@go.com', 'age': 23, 'salary': 200000, 'department': 'SEO'},
    {'user': 'orlando', 'email': 'digital@gmail.com', 'age': 23, 'salary': 200000, 'department': 'food'},
    {'user': 'ben', 'email': 'digi', 'age': 23, 'salary': 200000, 'department': 'worker'},
    {'user': 'stiller', 'email': 'digital@apple.com', 'age': 23, 'salary': 200000, 'department': 'loan'},
    {'user': 'adam', 'email': 'email@email.com', 'age': 23, 'salary': 200000, 'department': 'credit'},
    {'user': 'eva', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'buying'},
    {'user': 'frodo', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'harry', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'ron', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
    {'user': 'germiona', 'email': 'digit', 'age': 23, 'salary': 200000, 'department': 'credit'},
    {'user': 'gannibal', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'food'},
    {'user': 'lector', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'food'}
]
data_new = [

]
worker_of_month = {'IT': ['adam', 'sparrow', 'ben', 'frodo', 'gannibal'],
                   'credit': [],
                   'loan': ['stiller'],
                   'food': ['gannibal', 'lector']}
"""
1.Всем работникам месяца увеличить зарплату на 10%
2.Отделу где больше одного работников месяца увеличить зарплату на 5% дополнительно
3.Отдел где нет работников месяца - уменьшить всем зарплату на 3%
4.Работники чьи email-не принадлежат гуглу все кроме [@google.com,@gmail.com] - уволить
"""
check_names = []
for depart in worker_of_month:
    for lists in worker_of_month[(depart)]:
        if lists not in check_names:
            check_names.append(lists)
        elif lists in check_names:
            eliminate = worker_of_month[(depart)].index(lists)
            worker_of_month[(depart)].pop(eliminate)
print(worker_of_month)
for person in data:
    for depart in worker_of_month:
        for worker in (worker_of_month[(depart)]):
            if worker in person["user"]:
                # if len((worker_of_month[(depart)]))>1:
                first_sal = person["salary"]
                #     bonus = first_sal*0.05
                #     person["salary"] = bonus+first_sal
                bonus = person["salary"]*0.1
                person["salary"] = bonus + person["salary"]
                if len((worker_of_month[(depart)])) > 1:
                    bonus2 = first_sal*0.05
                    person["salary"] = bonus2+person["salary"]
check_list = []
for depart in worker_of_month:
    for worker in (worker_of_month[(depart)]):
        print(len(worker_of_month[(depart)]),worker_of_month[(depart)])
        print((worker_of_month["credit"]))
    if worker_of_month[(depart)] == []:
        for person in data:
            if depart in person["department"]:
                start_sal = person["salary"]
                minus = start_sal*0.03
                total = start_sal-minus
                person["salary"] = total
c = "@gmail.com"
c2 = "@google.com"
for i in data:
    if c in i["email"]:
        print(i["user"])
        data_new.append(i)
    elif c2  in i["email"]:
        print(i["user"])
        data_new.append(i)
print(data_new)

