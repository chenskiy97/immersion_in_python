'''
✔ Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии
'''

# def get_dict(lst_name, lst_stv, lst_prem):
#     return {lst_name[i]: lst_stv[i] * float(lst_prem[i][:-1]) / 100 for i in range(len(lst_name))}
#
#
ln = ['Ivan', 'Petr']
ls = [1000, 2000]
lp = ['10.25%', '15%']
# print(get_dict(ln, ls, lp))

print({ln[i]: ls[i] * float(lp[i][:-1]) / 100 for i in range(len(ln))})

gen_dict = ({ln[i]: ls[i] * float(lp[i][:-1]) / 100} for i in range(len(ln)))
print(*gen_dict)
