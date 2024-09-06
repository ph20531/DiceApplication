"""
____________________________________________________________________________________________________________________
Chapter001.자료형과 변수
____________________________________________________________________________________________________________________
"""
# Null 또는 값이 없다.
noneTypeValue = None

# 문자열 변수(String)
stringValue = "안녕하세요."

# 정수형 변수(Int)
intValue = 7
# 실수형 변수(Float)
floatValue = 0.5

# 참과 거짓(Boolean)
booleanValue = True

# complex : 복소수 = real(실수) + imaginary(허수 : 끝에 j를 붙이면 허수가 된다.)
complexVlaue = 5 + 7j

print(stringValue)
print(intValue)
print(floatValue)
print(booleanValue)
print(complexVlaue)

# type 명령어
print(type(None))
print(type("안녕하세요."))
print(type(3))
print(type(0.7))
print(type(False))

# complex : 복소수 = real(실수) + imaginary(허수 : 끝에 j를 붙이면 허수가 된다.)
print(type(2 + 3j))

# 복소수(complex)의 활용
complexValue1 = 1 + 2j
complexValue2 = 2 + 3j
print(complexValue1 + complexValue2)