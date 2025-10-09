lvl = input('Выбери уровень из 5: ')
text = input('ВВеди текст: ')

def lvl1(text):
    method = input('Выберите метод(upper; lower; capitalize): ')
    if method == 'upper':
        return text.upper()
    elif method == 'lower':
        return text.lower()
    elif method == 'capitalize':
        return text.capitalize()
    else:
        return 'ERROR'

def lvl2(text):
    method = input('Выберите метод(find; replace; count; index): ')
    if method == 'find':
        isk = input('Введите то, что ищем: ')
        return text.find(isk)
    elif method == 'replace':
        rep = input('Введите то, что будем заменять: ')
        rep1 = input('Введите то, чем заменим: ')
        return text.replace(rep,rep1,1)
    elif method == 'count':
        cnt = input('Введите то, что будем считать: ')
        return text.lower().count(cnt)
    #elif:
    else:
        return 'ERROR'

def lvl3(text):
    method = input('Выберите метод(split; join): ')
    if method == 'split':
        splt = input('Введите разделитель: ')
        return text.split(splt)
    elif method == 'join':
        sep = input('Введите соединитель: ')
        sim = input('Введите по какому символу будем соединять')
        text.split(sim)
        return sep.join(text)
    else:
        return 'ERROR'

def lvl4(text: str):
    method = input('Выберите метод(isdigit; isalpha; strip; format): ')
    if method == 'isdigit':
        return text.isdigit()
    elif method == 'isalpha':
        return text.isalpha()
    elif method == 'strip':
        strp = input('Ведите что будем обрезать: ')
        return text.strip(strp)
    elif method == 'format':
        form = input('Введите то, что будем вставлять: ')
        return text.format(form)
    else:
        return 'ERROR'

def lvl5(text: str):
    sim = input('Введите на каком символе должны стоять пробелы: ')
    text = text.split(sim)
    text = ' '.join(text)
    strp = input('Ведите что будем обрезать: ')
    text = text.strip(strp)
    text = text.capitalize()
    return text

if lvl == '1':
    print(lvl1(text))
elif lvl == '2':
    print(lvl2(text))
elif lvl == '3':
    print(lvl3(text))
elif lvl == '4':
    print(lvl4(text))
elif lvl == '5':
    print(lvl5(text))
else:
    print('ERROR')

