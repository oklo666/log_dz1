"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""


users = {'ivan': 'dfg885', 'Oleg': 'dghg887', 'Niko': 'jgr456', 'Mila': 'llsla959', 'Kolya': 'ggg456', 'Olya': 'yyy959'}
passwords = {'id1': 'dfg885', 'id2': 'dghg887', 'id3': 'jgr456', 'id4': 'llsla959', 'id5': 'hghhd12','id6': 'iru333000'}


# линейная сложность
def authorization (users):
    for k, v in users.items():                                  #O(N)
        if v in passwords.values():                             #O(1)
            print(k, 'your authorization done' )                #O(1)
        else:
            print(k, 'you are not logged in, please log in')    #O(1)
authorization(users)
# Итоговая сложность O(N) + O(1) + O(1) + O(1) = O(N) линейная


# константная сложность

users = {'ivan': ['dfg885','activated good'], 'Oleg': ['dghg887','banned'],
         'Vova': ['dfg887775','activated good'], 'Olga': ['d000ghg887','banned']}

def authorization(login, password):
    if login in users.keys():                         #O(1)
        print('login is correct')                     #O(1)
        if password in users[login][0]:               #O(1)
            print('password is correct')              #O(1)
            if users[login][1] == 'activated good':   #O(1)
                print('your authorization done')      #O(1)
            else:
                print('your account is banned')       #O(1)
        else:
            print('incorrect password')               #O(1)
    else:
        print('incorrect login')                      #O(1)

# Итоговая сложность O(1) + O(1) + O(1) + O(1) + O(1) + O(1) + O(1) + O(1) + O(1) = O(1) константная

authorization('Vova', 'dfg887775')
print('-------------------------------------')
authorization('Pasha', 'd87775')
print('-------------------------------------')
authorization('ivan', 'dfg885')
print('-------------------------------------')
authorization('Olga', 'd09900ghg887')

"""
Констаное (О(1)) решение эффективнее т.к. нет итераций
"""







