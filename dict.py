dic = {'algorithm': '알고리즘','DataBase':'데이터 베이스','information':'정보','communication':'통신',
       'APP':'애플리케이션','Bite/Byte':'바이트', 'Bug':'버그','Cloud':'클라우드','Cookie':'쿠키','Compile':'컴파일'}
print("인터넷없이 사용 가능한 코딩 단어 사전입니다!")

while True:
    print("1.영한 사전 / 2.한영사전")
    menu = int(input("메뉴 선택하기(번호 선택) : "))

    if menu == 1:
        print(sorted(dic.keys()))
        
        en_input = input("영어 단어 입력: ")
        
        if en_input in dic.keys():
            print(dic[en_input])
        else:
            print("그런 영어 단어는 사전에 없습니다! 추가해 주세요!")
            new_wordE = en_input
            new_wordK = input('한글(뜻): ')
            dic[new_wordE] = new_wordK
            print("저장되었습니다!!")

    elif menu == 2:
        print(sorted(dic.values()))
        
        ko_input = input("한글 단어 입력: ")
        
        if ko_input in dic.values(): #value로 key를 찾는 과정입니다.
            for ke, val in dic.items():
                if val == ko_input:
                    print(ke)
        else:
            print("그런 한글 단어는 사전에 없습니다!")
            print("그런 한글 단어는 사전에 없습니다! 추가해 주세요!")
            new_wordE = ko_input
            new_wordK = input('한글(뜻): ')
            print("저장되었습니다!!!")
    break