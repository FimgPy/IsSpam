dataset = {}
with open('dataset.txt', 'r', encoding='utf-8') as text:
    for line in text:
        line = line.strip()
        mas = line.split(' - ')
        message = mas[0].replace('"', '').replace(',', '')
        label = mas[1].strip()
        if label == 'не спам':
            dataset[message] = 0
        else:
            dataset[message] = 1

static = {}
for message, label in dataset.items():
    words = message.lower().split()
    for word in words:
        if word in static:
            if label == 1:
                static[word]['spam'] += 1
            else:
                static[word]['non_spam'] += 1
        else:
            if label == 1:
                static[word] = {'spam': 1, 'non_spam': 0}
            else:
                static[word] = {'spam': 0, 'non_spam': 1}

spam_ratio = {}
for word, counts in static.items():
    spam_count = counts.get('spam', 0)
    total_count = spam_count + counts.get('non_spam', 0)
    if total_count == 0:
        ratio = 0
    else:
        ratio = (spam_count / total_count) * 100
    spam_ratio[word] = int(ratio)


def is_spam(str_):
    mas_ = str_.replace(",", '').split()
    lowwermas = [i.lower() for i in mas_]
    res = 0
    count = 0
    for i in lowwermas:
        if i in spam_ratio.keys():
            res += spam_ratio[i]
            count += 1

    if count > 0:
        average = res // count
        if average >= 50:
            return f'Спам'  # Вероятность: average%
        else:
            return f'Не спам'  # Вероятность: (100 - average)%
    else:
        return 'Нет данных для определения'


if __name__ == '__main__':
    print(is_spam('Нигирийский принц завещал вам наследство. Перейдите по ссылке чтобы получить его'))
