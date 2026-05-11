import random

#자료 구조
limit_error = 7

def select_word():
    word_list = ['APPLE', 'BANANA', 'MAN', 'WOMAN', 'TOMATO']
    return random.choice(word_list)

#게임 로직
#1. Com이 단어 선택하여 보여주기
target_word= select_word()
blank_char = "_"
word_screen = blank_char * len(target_word)


num_error = 0
while num_error < limit_error:
    #2. 사용자 알파벳 입력
    user_input = input(">> 알파벳 입력 : ").upper()

    #3. 게임 상태 업데이트
    # 알파벳이 단어에 있으면 채워주기
    if target_word.find(user_input) != -1 and user_input != "": # 없으면 오류 횟수 증가
        for i in range(len(target_word)):
            if target_word[i] == user_input and word_screen[i] == blank_char:
                word_screen = word_screen[:i] + user_input + word_screen[i+1:]
                break
        print ("정답 : ", word_screen)
    else : # 알파벳이 단어에 있으면 채워주기
        num_error += 1
        print(f"오답 : {num_error}회")
    # 4. 단어를 다 맞췄으면(word_screen에 _가 없으면) 사용자 win
    if word_screen.rfind(blank_char) == -1 :
        print("You win ~~!~!~!~!")
        break

# 5. 시도 횟수가 7번을 넘었으면 loose
if num_error >= limit_error:
    print('You loose... : ', target_word)