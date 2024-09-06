"""
____________________________________________________________________________________________________________________
Chapter003.연산자와 인덱스 & 슬라이싱
____________________________________________________________________________________________________________________
"""

# 연산자 ___________________________________________________________________________________________________________

# 001. 산술 연산자
# +   |   더하기
print(5+2)

# -   |   빼기
print(5-2)

# *   |   곱하기
print(5*2)

# /   |   나누기(값이 출력)
print(5/2)

# **   |  거듭제곱
print(5**3)

# //   |  몫(몫이 출력)
print(5//2)

# %    |  나머지(나머지가 출력)
print(5%2)




# 002. 대입 연산자
"""
     사용법
         변수 (산술연산자)= 피연산자 | 변수 = 변수 (산술연산자) 피연산자
"""
# +=  |   더하기
num = 0
num += 1
print(num)

# -=  |   빼기
num = 0
num -= 1
print(num)

# *=  |   곱하기
num = 2
num *= 2
print(num)

# /=  |   나누기(값이 출력)
num = 5
num /= 2
print(num)

# **=  |  거듭제곱
num = 5
num **= 3
print(num)

# //=  |  몫(몫이 출력)
num = 5
num //= 2
print(num)

# %=   |  나머지(나머지가 출력)
num = 5
num %= 2
print(num)



"""
     증감연산자 | 파이썬에서는 제공하지 않음.
         ++i(전위연산자 : 해당 줄에서 처리), i++(후위연산자 : 다음줄에서 처리) | i=i+1
         --i(전위연산자 : 해당 줄에서 처리), i--(후위연산자 : 다음줄에서 처리) | i=i-1
"""



# 003. 비교 연산자
# >   |   크다
print(5>2)
print(5>5)

# >=  |   크거나 같다
print(5>=2)
print(5>=5)

# <   |   작다
print(5<2)
print(5<5)

# <=  |   작거나 같다
print(5<=2)
print(5<=5)

# ==  |   같다
print(1==1)
print(5==2)

# !=  |   같지 않다
print(1!=1)
print(5!=2)




# 004. 논리 연산자
# and   |   둘다 참이면 True
print(3<5 and 7>5) # True and True = True
print(3<5 and 7<5) # True and False = False
print(3>5 and 7<5) # False and False = False

# or    |   하나라도 참이면 True
print(3<5 or 7<5) # True or False = True
print(3>5 or 7>5) # False or True = True
print(3>5 or 7<5) # False or False = False
print(3<5 or 7>5) # True or True = True

# not   |   반전 값 출력
print(not 3<5) # not True = False
print(not 3>5) # not False = True




# 005. 멤버 연산자
# in       |   포함
print("c" in "cake")

# not in   |   미포함
print("c" not in "cake")







# 인덱스 & 슬라이싱 _________________________________________________________________________________________________

# 001. 리스트이란?
"""
들어가기 전에
     변수 = 하나의 값만 저장할 수 있다.
     리스트 = 여러개의 값을 저장할 수 있다.
     
"""

# 변수__________________________________
intVariable = 12345
# Error | 리스트가 아니라 int형 변수
# print(intVariable[0])

floatVariable = 1234.5
# Error | 리스트가 아니라 float형 변수
# print(floatVariable[0])

boolVariable = True
# Error | 리스트가 아니라 bool형 변수
# print(boolVariable[0])


# 리스트__________________________________
intList = [1, 2, 3, 4, 5]
print(intList[0])

floatList = [1.1, 2.2, 3.3, 4.4, 5.5]
print(floatList[0])

boolList = [True, False, False, True]
print(boolList[0])




# C언어에서의 개념________________________________________________________________________________________________________________________________
# 주의사항 | C언어의 배열(Array)과 파이썬의 리스트(List)는 다르다. 하지만 기초적으로 비슷하게 사용되기 때문에 설명을 위해 잠시 List를 Array라고 표현했다.
"""
     string의 유래
         참고로 C언어에서는 char형 변수가 존재하는데
         char형 변수의 배열형이 charArray이고 여기서 효율적으로 사용할 수 있도록 객체화시킨 형태가 string이다.

         _______________________________________________________________________________________________

         핵심 요약 | char(문자) > charArray(문자열) > string(효율적으로 사용하도록 객체화시킨 문자열)
         _______________________________________________________________________________________________
         
         char      = 변수     |  'c'
         charArray = 배열     |  ['c', 'a', 'k', 'e']
         string    = 객체     |  "cake"
         _______________________________________________________________________________________________

         하지만 string의 등장으로 char를 따로 사용하지는 않는다.
"""

# char      | 문자(변수)
charVariable = 'c'
print(charVariable)

# charArray | 문자열(배열)
charArray = ['c', 'a', 'k', 'e']
print(charArray[0])

# string    | 문자열(객체화시킨 배열)
stringObject = "cake"
print(stringObject)

# ________________________________________________________________________________________________________________________________________________




# 다차원 리스트____________________________

# 1차원 리스트 | 기본 리스트
oneDimensionalList = [1, 2, 3, 4, 5]
print(oneDimensionalList[0])

# 2차원 리스트
twoDimensionalList = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]
print(twoDimensionalList[1][0])

# 3차원 리스트
threeDimensionalList = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]
print(threeDimensionalList[2][0])

# ... 무한 차원의 리스트을 생성할 수 있다.



# 리스트 안에 다른 타입의 값을 넣을 수 있다.
mixList = [None, 1, 2.2, True, 'c', "cake", 1 + 2j]
print(mixList)

# 리스트 안에 리스트 값을 넣을 수 있다.
listInList = [[1, 2, 3, 4, 5], [1.1, 2.2, 3.3, 4.4, 5.5], [True, False, False, True], "cake"]
print(listInList[1][0])




# 002. 인덱스
"""
list
________________________________________________________________________________________________________
     리스트의 구조
         [p]  [y]  [t]  [h]  [o]  [n]
          0    1    2    3    4    5
         -6   -5   -4   -3   -2   -1

         [] : 요소(element)
         0~5, -1~-6 : 인덱스(index)
         p~n : 값(value)

         _______________________________________________________________________________________________
         주소(address)란?
             값을 저장할 수 있는 물리적인 메모리의 시스템적인 주소 | 0x7ffc7e53ab80
             참고로 C언어에서는 포인터(pointer)를 이용하여 요소(element)의 주소(address)를 알아낼 수 있다.

         포인터(pointer)란?
             C언어에서 사용되며 요소(element)의 주소(address)를 알아내는 지시자이다.

         _______________________________________________________________________________________________
         소프트웨어(software) | 요소(element) = 값(value)
         하드웨어(hardware)   | 주소(address)
________________________________________________________________________________________________________
"""
list = "python"

# 첫번째 인덱스는 0부터 시작한다.
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])

# 마지막 인덱스와 -1은 같은 표현이다.
print(list[5])
print(list[-1])

# -1부터 1씩 감소하는 인덱스도 가능하다.
print(list[-1])
print(list[-2])
print(list[-3])
print(list[-4])
print(list[-5])
print(list[-6])



# 002. 슬라이싱
"""
     사용법
         list[start:end]
         start부터 end직전까지
"""
print(list[3:6]) # 인덱스 3부터 6직전인 5까지 슬라이싱

# start부터 끝까지 슬라이싱을 하고싶은 경우
print(list[2:])

# 맨 처음부터 end직전까지 슬라이싱을 하고싶은 경우 
print(list[:3])

# 맨 처음부터 끝까지 슬라이싱을 하고싶은 경우
print(list[:])
print(list)

"""
     string객체와 list객체의 차이점
         string | python
         list   | ['p', 'y', 't', 'h', 'o', 'n']
         list   | [1, 2, 3, 4, 5, 6]
         list   | [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
         list   | [True, False, True, True, False, False]
         list   | [None, 1, 2.2, True, 'c', "cake", 1 + 2j]
"""