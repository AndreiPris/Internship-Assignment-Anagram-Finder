def read_words_from_file(filename):
    words = []   
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip() # - пробелы и переносы
                word = word.lower() #ToLowerCase               
                #проверка
                if not word:
                    continue        
                if word.isalpha():
                    words.append(word)
                
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")
        raise
    except IOError as e:
        print(f"Ошибка чтения файла: {e}")
        raise
        
    return words

def group_anagrams(words):
    anagram_groups = {}
    
    for word in words:
        sort = sorted(word)
        key = ''.join(sort)
        if key in anagram_groups:
            anagram_groups[key].append(word)
        else:
            anagram_groups[key] = [word]
    
    return anagram_groups

if __name__ == "__main__":
    filename = "sample.txt"
    
    try:
        words = read_words_from_file(filename)
        groups = group_anagrams(words)
        
        for key, group in groups.items():
            if len(group) > 1:
                print(' '.join(group))
            else:
                print(group[0])          
                  
    except Exception as e:
        print(f"Ошибка: {e}")