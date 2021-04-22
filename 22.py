'''
Functions
'''


# def max_of_list(numbers):
#     return (max(numbers))
#
#
# print(max_of_list([1, 2, 3, 4, 5, 6]))
#
# def max_of():
#     x = int(input())
#     y = int(input())
#     if x>y:
#         print(x)
#     else:
#         print(y)
list = {"username":[],
        'password':[]
        }
def registration():
    username = input()
    # >8 symbols
    password = input()
    # only letters
    check_password = input()
    if len(username)>=8 and password.isalpha() == False:
        if check_password == password:
            return username,password
try:
    i = 0
    while i<=2:
            username, password = registration()
            list['username'].append(username)
            list['password'].append(password)
            i+=1
    print(list)
    def log_in(list):
            login = input()
            password = input()
            i = 0
            while i < len(list['username']):
                if login in list['username'][i] and password in list['password'][i]:
                    print("SUCCESFUL")
                    break
                else:
                    print("UNSUCCESFUL")
                    i+=1
    log_in(list)
except TypeError:
    print("Введите правильные данные")