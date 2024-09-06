"""
____________________________________________________________________________________________________________________
Chapter004.문자열(String)
____________________________________________________________________________________________________________________
"""

# 문자열 처리 ___________________________________________________________________________________________________________

# 001. String + String
stringProcessing001 = "string001"
stringProcessing002 = "string002"
print(stringProcessing001 + stringProcessing002)




# 002. String + Other Type
stringProcessing = "string"
intValue = 3
floatValue = 1.25
boolValue = True
NoneValue = None
complexVlaue = 1 + 2j

"""
     Error | can only concatenate str (not "other type") to str
"""
# print(stringProcessing + intValue)
# print(stringProcessing + floatValue)
# print(stringProcessing + boolValue)
# print(stringProcessing + NoneValue)
# print(stringProcessing + complexVlaue)


"""
     String과 Other Type을 연결해주려면 str()함수로 형변환을 시켜주면 된다.
     결과적으로 String + String의 형태로 만들어주어서 에러가 발생하지 않는다.
"""
print(stringProcessing + str(intValue))
print(stringProcessing + str(floatValue))
print(stringProcessing + str(boolValue))
print(stringProcessing + str(NoneValue))
print(stringProcessing + str(complexVlaue))




# 003. Length | len()
"""
     주의할 점
     "" = 값이 없다.
     " ", "\n", ".", "~" 등등 비트(bit)가 있는 문자 = 값이 있다.

     유니코드(Unicode)란?
         전 세계의 모든 문자를 컴퓨터에서 일관되게 표현하고 다룰 수 있도록 설계된 산업 표준이다.

     아스키 코드(ASCII Code)란?
         영문 알파벳을 사용하는 대표적인 문자 인코딩(Character Encoding)이다.
         아스키 코드(ASCII Code)의 확장판으로 안시 코드(ANSI Code)가 있다.

     UTF-8이란?
         표준 유니코드(Unicode)의 문자를 모두 표현할 수 있으며,
         부가적으로 한국어와 같은 어떤 언어도 깨지지않도록 표현가능한 문자 인코딩(Character Encoding)이다.

     문자 인코딩(Character Encoding)이란?
         줄여서 인코딩이라고도 부르며 입력한 문자나 기호들을 컴퓨터가 이용할 수 있는 신호로 변환하는 것을 말한다.
         즉, 복잡한 신호를 0과 1의 디지털 신호(2진수)로 변환하는 것을 의미한다.
"""
stringLength = "안녕하세요."
print(len(stringLength))




# 004. Multiline Text | \n을 사용하지 않아도 엔터(Enter)로 구분된 문자열을 인식한다. | Multiline Text안에는 '와 "를 탈출문자없이 표현 할 수 있다.
multilineString = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(multilineString)







# 문자열 메소드 ___________________________________________________________________________________________________________
letter = "LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING LEIT, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

# 001. lower() | 모두 소문자로 변환
print(letter.lower())




# 002. upper() | 모두 대문자로 변환
print(letter.upper())




# 003. capitalize() | 첫글자는 대문자로 나머지는 소문자로 변환
print(letter.capitalize())




# 004. title() | 단어마다 첫글자를 대문자로 변환
print(letter.title())




# 005. swapcase() | 소문자는 대문자로 대문자는 소문자로 변환
print(letter.swapcase())




# 006. split() | 띄어쓰기를 기준으로 단어들을 나누어 리스트로 반환
print(letter.split())
"""
     기준을 바꾸려면 메소드 인자에 원하는 기준 문자를 입력해주면 된다.
"""
print(letter.split(","))




# 007. count() | 문자열 중에서 지정한 문자가 몇개인지 int로 반환
print(letter.count("l"))
"""
     대소문자 구분없이 지정한 문자의 갯수를 알고 싶다면
     001. lower()함수로 모두 소문자로 변환한 후 count()함수 인자에 "소문자(cake)"를 입력해주면 된다.
     002. upper()함수로 모두 대문자로 변환한 후 count()함수 인자에 "대문자(CAKE)"를 입력해주면 된다.
"""
print(letter.lower().count("l"))
print(letter.upper().count("L"))




# 008. startswith() | 지정한 문자로 문자열이 시작되는지 boolean형태로 반환
print(letter.startswith("LOREM"))
print(letter.startswith("eiusmod"))

"""
     마찬가지로 대소문자 구분없이 사용하고 싶을 경우 lower()함수나 upper()함수를 활용하면 된다.
"""
print(letter.lower().startswith("lorem"))




# 009. endswith() | 지정한 문자로 문자열이 끝나는지 boolean형태로 반환
print(letter.endswith("aliqua."))
print(letter.endswith("CONSECTETUR"))

"""
     마찬가지로 대소문자 구분없이 사용하고 싶을 경우 lower()함수나 upper()함수를 활용하면 된다.
"""
print(letter.upper().endswith("ALIQUA."))




# 010. strip() | 문자열의 앞뒤로 불필요한 문자를 제거하여 string형태로 반환
stripLetter = " [1, 1.2, True, None, 1 + 2j] , "

# strip()함수 인자에 아무것도 입력하지 않으면 기본적으로 " "(공백)을 제거한다.
print(stripLetter.strip())

# strip()함수 인자에 지정할 문자들을 입력하면 한 글자(char)마다 인식해서 제거
print(stripLetter.strip("[] ,"))

# strip()함수 예시
"""
     001. strip()함수로 문자열 앞뒤의 불필요한 문자들을 제거하여 split()할 수 있는 상태로 변환
     002. split()함수로 list로 변환
     003. string에서 list형태로 변환이 되었으니 원하는 요소를 꺼냄
     004. 요소의 값이 기본적으로 string으로 되어있으니 원하는 타입형으로 형변환하여 사용
"""
unknownStringToList = stripLetter.strip("[] ,").split(",")
print(unknownStringToList)
print(type(unknownStringToList))

print(unknownStringToList[0])
print(type(unknownStringToList[0]))

print(int(unknownStringToList[0]))
print(type(int(unknownStringToList[0])))




# 011. replace() | 찾으려는 문자를 바꾸려는 문자로 모두 바꿈
# 첫번째 인자 | 찾으려는 문자
# 두번째 인자 | 바꾸려는 문자
print(letter.replace("l", "L"))




# 012. find() | 찾으려는 문자의 시작점 인덱스를 int로 반환
print(letter.find("IPSUM"))

"""
     주의 | 처음으로 찾은 문자의 인덱스 값만 반환(1회성)
"""
print(letter.find(","))




# 012. center() | 찾으려는 문자를 바꾸려는 문자로 모두 바꿈
# 첫번째 인자 | 허용하는 문자열의 총 길이
# 두번째 인자 | 채우려는 문자
"""
     허용하는 문자열의 총 길이가 원본 문자열의 길이보다 길다면 초과되는 공간에 지정한 문자로 채운다.
"""
print(letter.center(len(letter) + 1, "~"))
print(letter.center(len(letter) + 2, "~"))
print(letter.center(len(letter) + 3, "~"))
print(letter.center(len(letter) + 4, "~"))

"""
     허용하는 문자열의 총 길이가 원본 문자열의 길이보다 같거나 작다면 원본 String을 출력한다.
"""
print(letter.center(len(letter), "~"))
print(letter.center(len(letter) - 2, "~"))




# etc. 구글 > 파이썬 내장형 > ctrl + f 후 "문자열 메서드" > 그 이후에 상황에 알맞는 문자열 메서드를 찾아서 사용하면 된다.
"""
     참고로 파이썬 내장형 문서는 파이썬의 시스템적인 모든 것이 서술되어 있다.
     최신 버전의 문서를 참고하여 개발하는 것이 가장 좋다.
"""







# 문자열 포맷 ___________________________________________________________________________________________________________
python = "파이썬"
java = "자바"

# 001. 기본
print(python + java)
print(python + " " + java)




# 002. print()함수 포맷
# 여러개 인자(인자는 ","콤마로 구분한다. | 영어 표현식은 arg0, arg1, arg2...) | 자동으로 " "(공백)으로 구분해서 출력
print(python, java)

# sep | 구분 문자를 지정해줄 수 있다. | 기본값 = " "(공백)
print(python, java, sep=", ")

# end | 문자열의 마지막에 원하는 문자를 추가할 수 있다. | 기본값 = "\n"(줄바꿈)
print(python, java, sep=", ", end="는 프로그래밍 언어이다.\n")

# file | 출력된 값을 파일로 저장할 수 있다. 보통 로그값을 파일로 저장할 때 많이 사용한다.
fileName = "io.txt"
path = r"C:\Users\USER\OneDrive\바탕 화면" + "\\" + fileName
with open(path, 'w') as f:
     print(python, java, sep=", ", end="는 프로그래밍 언어이다.", file=f)

# flush | True로 설정할 경우 쓰레드에 따라 출력이 된다. 보통 로그값을 쓰레드의 진행속도에 따라 출력할 때 사용한다.
import time
for i in range(10):
    print(i, end=' ', flush=True) # False일 경우 한 프레임에 모두 출력됨.
    time.sleep(0.1)
print("\n")



# 003. String Format
# format() | 기본
print("프로그래밍 언어에는 {}, {} 등이 있다.".format(python, java))

# format() | 인덱스
print("프로그래밍 언어에는 {1}, {0} 등이 있다.".format(python, java))



# f-string | Formatted string literals | 파이썬 3.6 버전 이상 지원
print(f"프로그래밍 언어에는 {python}, {java} 등이 있다.")
print(f"프로그래밍 언어에는 {java}, {python} 등이 있다.")

"""
      당연히 포멧팅할 때 사용하는 변수의 타입이 꼭 string이 아니여도 된다.
"""

a = 1
b = 2.2
print(f"""
여기서 문제
{a} + {b} = {a+b}이다. | str(a) + " + " + str(b) + " = " + str(a+b) + "이다."와 같은 표현이다.
이런식으로 String에 다른 타입(Other Type)의 변수들을 유동적으로 포맷팅하여
결과적으로 유동적인 String값을 얻을 수 있다.

      장점
      001. 쉽고 빠르게 프로그래밍을 할 수 있다.
      002. 다른 타입의 변수를 굳이 String으로 형변환 하지 않아도 자동으로 된다.
""")

print(f"{a} + {b} = {a+b}이다.")
print(str(a) + " + " + str(b) + " = " + str(a+b) + "이다.")
print("\n")







# 탈출 문자(Escape Character) ___________________________________________________________________________________________________________
"""
      따옴표(', ") 문제 __________________________________________________________________________________________________________________
"""
# escapeCharacter = ''나'는 "너"와 다르다.' # Error
# escapeCharacter = "'나'는 "너"와 다르다." # Error

# '로 둘러쌓았을 경우 안에있는 '를 반드시 탈출 문자로 표현해야 한다.
escapeCharacter = '\'나\'는 "너"와 다르다.'
print(escapeCharacter)

# "로 둘러쌓았을 경우 안에있는 "를 반드시 탈출 문자로 표현해야 한다.
escapeCharacter = "'나'는 \"너\"와 다르다."
print(escapeCharacter)

"""
      둘러쌓인 따옴표와 내용물 안에 있는 따옴표가 같다면 시스템상으로 인지를 할 수 없다.
      그래서 '(작은 따옴표)와 "(큰 따옴표)는 상황에 맞게 탈출 문자(Escape Character)로 표현해줘야 한다.

      ___________________________________________________________________________________________________________________________________
      아까전에 Multiline Text안에는 '(작은 따옴표)와 "(큰 따옴표)를 탈출문자없이
      표현 할 수 있다라고 한 이유도 둘러싼 따옴표와 내용물의 따옴표가 다르기 때문이다.
      ___________________________________________________________________________________________________________________________________
"""

# r-string | Raw string | Raw = 날것의 | 문자열내의 이스케이프 문자를 있는 그대로 표현한다. | 보통 파일 path(경로)를 표현할 때 사용한다.

# r-string의 기본             | 탈출문자가 작동하지 않음
rawString = r"\n \t \' \" \\ (etc...)"

# 같은 내용이지만 출력값이 다름 | 탈출문자가 작동함
otherString = "\n \t \' \" \\ (etc...)"

print(f"{rawString}와 {otherString}은 다르게 출력된다.")



# Path(경로)로 사용할 경우
pathString = r"C:\Users\USER\OneDrive\바탕 화면\io.txt"
# 같은 표현
equalString = "C:\\Users\\USER\\OneDrive\\바탕 화면\\io.txt"

print(f"{pathString}와 {equalString}은 같은 표현이지만 더 쉽고 빠르게 개발할 수 있다.")