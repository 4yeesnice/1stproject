names = ["vova","petya","batya","sestra","kot"]
salaries = [0,10]
i = 0
while i<len(names):
    try:
        salaries[i]*=2
    except IndexError:
        salaries.append(0)
    i+=1
print(salaries)