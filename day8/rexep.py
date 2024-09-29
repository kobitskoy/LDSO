import re
# txt = """
# Ауди стоит 1000
# БМВ стоит 1200
# VW стоит 900
# """
#
# list_munbers = re.findall(r'\d+', txt)
# print(list_munbers)
#
# regex_rule = re.compile(r'\d+')
# print(regex_rule.findall(txt))
phone =r'\+7\(\d{3}\)-\d{2}[2]'
number = '+7(999)-77-77'

if re.fullmatch(phone,number):
    print('Верно')
else:
    print('Неверно')
