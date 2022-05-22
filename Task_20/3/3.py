from  dict import MyDict
dict1 = dict(растения=['роза', 'плющ', 'крапива', 'пион'],
             животные=['кенгуру', 'коала', 'морж', 'тюлень', 'черепаха'])
diction = MyDict(dict1)
print(diction.get('птицы'))
print(diction.get('животные'))