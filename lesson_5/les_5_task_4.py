from googletrans import Translator

translator = Translator()
with open('task_4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ft = translator.translate(line, 'ru')
        print(ft)
