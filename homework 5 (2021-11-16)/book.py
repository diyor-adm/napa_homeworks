from typing import Text

with open('book.txt', 'r', encoding='utf-8') as book:

    # textni tozalash

    book_main = []
    for line in book:
        book_list = []
        for word in line.strip().split(' '):
            word_copy = ''
            if not word == '':
                for letter in word:
                    if letter != ',' and letter != '.' and letter != ')' and letter != '(' and letter != '”' and letter != '“' and letter != '_' and letter != ';' and letter != ':' and letter != "‘" and letter != "’" and letter != '[' and letter != ']' and letter != '*':
                        word_copy += letter
                book_list.append(word_copy)
        for new_word in book_list:
            book_main.append(new_word)

    # unikal so`zni qidiramiz

    unique = []
    for word in book_main:
        if word not in unique:

            # text faylga print qilamiz

            with open('unique.txt', 'a') as unique_book:
                unique_book.write(word + ' ')
            unique.append(word)
    print(unique)
