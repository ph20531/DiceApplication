"""
____________________________________________________________________________________________________________________
Chapter002.네이밍 규칙과 형 변환
____________________________________________________________________________________________________________________
"""
# 네이밍규칙 ________________________________________________________________________________________________________

# 네이밍 규칙 1 | 변수 이름의 맨 앞자리는 "문자" 또는 "_"로 시작해야 한다.
name = None
_name = None

# 네이밍 규칙 2 | "네이밍 규칙 1"을 지켰다면 그 후에 "문자"나 "_"나 "숫자"로 구성해야 한다.
n = None
_ = None

# Error | 네이밍 규칙 1을 먼저 지키지 않으면 에러가 발생한다.
# 1 = None

n_1 = None
_n1 = None

n1 = None
_1 = None

# 네이밍 규칙 3 | 변수이름에는 "공백"이나 "특수문자"를 사용할 수 없다.

# Error | 공백 사용 시 에러가 발생한다.
# na me = None

# Error | 특수문자 사용 시 에러가 발생한다.
# na~me = None


# 네이밍 규칙 4 | 대소문자가 구분되기 때문에 다른 변수로 인식된다.
name = "소문자 변수"
Name = "대문자 변수"

print(name, Name)

# 네이밍 규칙 5 | keyword(예약어)를 변수이름으로 사용할 수 없다.
# ex) True, False, if, for, while, continue, break, class, ...

# Error | keyword(예약어) 자체로 변수를 만들면 에러가 발생한다.
# True = None

# 하지만 keyword(예약어) 뒤에 이름을 추가해주면 키워드가 아니므로 변수명으로 사용가능하다.
True1 = None


# 네이밍 규칙 6 | 변수명 표기법 "카멜", "파스칼", "스네이크", "헝가리안"

"""
1. 카멜 표기법(camel case)
     - 낙타 등처럼 내려갔다 올라가는 모양이라 하여 지어진 이름

     - 단어가 여러개 붙을 때, 앞 단어를 제외한 첫자를 대문자로 표기

     - java, C# 등의 언어들에서 권장 

       ex) dailyUserTable
"""
dailyUserTable = "camel case"

"""
2. 파스칼 표기법(pascal case)

     - 모든 단어의 앞자가 대문자로 시작(단어의 수와 상관 없음)

     - 네임스페이스, 이벤트, 프로퍼티, 클레스 네임을 지정할 때 주로 사용

     - 클래스 등에서 많이 사용

       ex) DailyUserTable
"""
DailyUserTable = "pascal case"

"""
3. 스네이크 표기법(snake case)

     - 모든 단어가 소문자로 표시

     - 다른 의미를 갖는 단어들의 조합에서 각 단어의 구분을 위하여 "_(언더바)"를 붙힘

     - 단어 사이의 "_(언더바)"때문에 뱀처럼 보인다고 해서 유래

     - 팟홀 표기법(pothole case) 또는 언더바 표기법(underbar case)라고도 불림

     - C++에서 권장

       ex) daily_user_table
"""
daily_user_table = "snake case"

"""
4. 헝가리안 표기법

     - 접두사에 자료형을 붙힘

     - 마이크로소프트 개발자 중 헝가리 프로그래머가 쓰던 변수 명명법

     - 현재는 자료형을 쉽게 알아 볼수 있는 다양한 방법들이 많기 때문에 권장하지 않음

       ex) strDailyUserTable
"""
strDailyUserTable = "string"
iDailyUserTable = 1
fDailyUserTable = 0.5

"""
5. 커스텀

     - 개발사만의 또는 개발 조직 자체적으로 사용하는 방식 또한 많이 사용

     ex) 접두사(두자리)_풀네임(단어)_약어...

            접두사 대문자, 단어의 첫글자 대문자, 약어 대문자

            ST_User_CD
"""

MM_Product_PR = 1000
MM_Vaccine_CD = "H$Syx2146ExWq"

# 네이밍 규칙 7 | 일반변수와 정적변수

# 정적변수(static variable) | 값이 절대로 바뀌면 안되는 변수의 경우
GAME_CODE_DATA = "qSyx^31W56xEq"

# 일반변수(variable) | 값이 언제든지 바뀔 수 있는 변수
gameCodeData = False

"""
     GAME_CODE_DATA = 게임쿠폰 고유번호
     gameCodeData = 게임쿠폰이 이미 사용되었는지 체크하는 용도
"""

if GAME_CODE_DATA == "qSyx^31W56xEq" and gameCodeData : 
    print("is allowed")
else:
    print("is not allowed")


# 형 변환 ________________________________________________________________________________________________________

# 001. int()
print("\n")

# 정수를 정수로 변환(의미없음)
intValue = int(1)
print(intValue)

# 실수를 정수로 변환
intValue = int(3.14)
print(intValue)

# 불리언을 정수로 변환
intValue = int(False)
print(intValue)

# 문자열을 정수로 변환
"""
      주의할 점
          001. intValue = int("a") | Error(표현된 문자열이 숫자가 아니기 때문)
          002. intValue = int("3.5") | Error(표현된 문자열이 숫자는 맞지만 변환하려는 타입(int)이 아니기 때문)
               - 이러한 경우에는 int(float("3.5")) 이런식으로 해결가능하다. | "3.5" > 3.5 > 3으로 형변환 되는 원리
"""
intValue = int("4")
print(intValue)




# 002. float()
print("\n")

# 실수를 실수로 변환(의미없음)
floatValue = float(1.3)
print(floatValue)

# 정수를 실수로 변환
floatValue = float(3)
print(floatValue)

# 불리언을 실수로 변환
floatValue = float(True)
print(floatValue)

# 문자열을 실수로 변환
"""
      주의할 점
          001. floatValue = float("a") | Error(표현된 문자열이 숫자가 아니기 때문)
          002. floatValue = float("1") | 이 경우에는 문제없이 작동한다.
               - 왜냐하면 실수 ⊃ 정수이기 때문이다.
"""
floatValue = float("3.14")
print(floatValue)




# 003. str()
print("\n")

# 정수를 문자열로 변환
stringValue = str(2)
print(stringValue)
print(type(stringValue))

# 실수를 문자열로 변환
stringValue = str(5.87)
print(stringValue)
print(type(stringValue))

# 불리언을 문자열로 변환
stringValue = str(False)
print(stringValue)
print(type(stringValue))

# 문자열을 문자열로 변환(의미없음)
stringValue = str("cake")
print(stringValue)
print(type(stringValue))




# 004. bool
print("\n")
      
"""
      요점정리
           False = 거짓 또는 값이 없다.
           True = 진실 또는 값이 있다.
"""

# None의 경우
boolValue = bool(None)
print(boolValue)

# 값이 없는 문자열의 경우
boolValue = bool("")
print(boolValue)

# 값이 있는 문자열의 경우
boolValue = bool("a")
print(boolValue)

# 값이 없는 정수의 경우
boolValue = bool(0)
print(boolValue)

# 값이 있는 정수의 경우
boolValue = bool(5)
print(boolValue)

# 값이 없는 실수의 경우
boolValue = bool(0.0)
print(boolValue)

# 값이 있는 실수의 경우
boolValue = bool(3.14)
print(boolValue)



# etc.