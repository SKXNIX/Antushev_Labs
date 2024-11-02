# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    uniq_letters = {}
    for letter in text:
        if letter.isalpha():
            if letter not in uniq_letters:
                uniq_letters.update({letter:1})
            else:
                uniq_letters[letter] += 1
    return uniq_letters     # {"letter": count}


# TODO Функция подсчета общего количества букв
def count_all_letters(letters_dict):
    count_ = 0
    for count_letters in letters_dict.values():
        count_ += count_letters
    return count_


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_dict):
    count_all = count_all_letters(letters_dict)
    for letter in letters_dict.keys():
        letter_freq = letters_dict[letter] / count_all
        letter_freq = "%.2f" % letter_freq
        letters_dict[letter] = letter_freq
    return letters_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


# TODO Распечатайте в столбик букву и её частоту в тексте
for item in calculate_frequency(count_letters(main_str)).items():
    print(f"{item[0]}: {item[1]}")