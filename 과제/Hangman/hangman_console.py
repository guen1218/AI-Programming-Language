from hangman import Hangman

def load_word_list():
    file = r'과제\hangman\voca.txt' 
    word_list = []
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            word = line.strip().split()
            if word:
                word_list.append(word[0])
    return word_list
    
word_list = load_word_list()

def start_hangman_console(hangman):
    print()
    print('='*10," Hangman ",'='*10)
    
    print(f'{hangman.display_word} {len(hangman.word)}글자')
    
    while True:
        letter = input(">> 알파벳 입력 : ")
        if letter.isalpha():
            result = hangman.check_letter(letter)
    
            if result == Hangman.RIGHT:
                print(f'정답 : {hangman.display_word}')
            elif result == Hangman.WRONG:
                print (f"오답 : {hangman.num_try}회 시도")
            elif result == Hangman.ERROR:
                print (hangman.error_status)
                continue
    
            #승패 확인
            result = hangman.is_win()
            if result == Hangman.WIN:
                print(f"You win ~~!~!~!~~~~ : {hangman.num_try}회 시도")
                break
            elif result == Hangman.LOOSE: 
                print (f"You loose ~~!~!~~~~ : {hangman.word}")
                break
        else:
            print("알파벳을 입력하시요")
            
if __name__ == "__main__":
    hangman = Hangman(word_list)
    start_hangman_console(hangman)
