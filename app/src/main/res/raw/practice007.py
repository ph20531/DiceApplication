"""
____________________________________________________________________________________________________________________
Chapter007.딕셔너리(Dictionary)
____________________________________________________________________________________________________________________
"""

# 딕셔너리 속성 _____________________________________________________________________________________________________

# 001. 딕셔너리의 기본
"""
     Dictionary = {Key1:Value1, Key2:Value2, Key3:Value3, Key4:Value4 ...}
     Pair = Key:Value | Pair == Item == 키-값 == 쌍
"""
dictValue = {"Key1":None, "Key2":2.2, "Key3":True, "Key4":'c', "Key5":"cake", "Key6":1 + 2j}
print(dictValue) # print | {'Key1': None, 'Key2': 2.2, 'Key3': True, 'Key4': 'c', 'Key5': 'cake', 'Key6': (1+2j)}




# 002. 비어있는 딕셔너리 선언
"""
     Dictionary = {}
"""
dictValue = {}
print(dictValue)       # print | {}
print(type(dictValue)) # <class 'dict'>




# 003. Key와 Value의 타입형(Any)
"""
     여기서 중요한 점은 Key도 Value도 어떤 타입형(Any type)이든 가능하다.
     그리고 Key와 Value가 같아도 상관없다.
"""
dictValue = {None:None, 2.2:2.2, True:True, 'c':'c', "cake":"cake", 1 + 2j:1 + 2j}
print(dictValue) # print | {None: None, 2.2: 2.2, True: True, 'c': 'c', 'cake': 'cake', (1+2j): (1+2j)}




# 004. Key끼리의 중복이 허용되지 않음
"""
     다만 Key끼리는 중복이 허용되지 않는다.
     그렇기 때문에 가장 마지막에 선언된 Item만 값이 남게 된다.
"""
dictValue = {"Key":None, "Key":2.2, "Key":True, "Key":'c', "Key":"cake", "Key":1 + 2j}
print(dictValue) # print | {'Key': (1+2j)}




# 005. Key가 서로 다르다면 Value는 같아도 상관없다.
"""
     왜냐하면 Value는 사용되는 값일 뿐이기 때문에 중복되도 상관이 없다.
"""
dictValue = {"Key1":1, "Key2":1, "Key3":1, "Key4":1, "Key5":1, "Key6":1}
print(dictValue) # print | {'Key1': 1, 'Key2': 1, 'Key3': 1, 'Key4': 1, 'Key5': 1, 'Key6': 1}




# 006. 딕셔너리의 접근법
"""
     Dictionary[Key]
"""
dictCake = {"Name":"엄마는 외계인 케이크", "Price":12000, "Flavor":"초콜렛", "IsSoldOut": False}
print(dictCake["Name"])      # print | 엄마는 외계인 케이크
print(dictCake["Price"])     # print | 12000
print(dictCake["Flavor"])    # print | 초콜렛
print(dictCake["IsSoldOut"]) # print | False




# 007. 새로운 요소 추가
"""
     Dictionary[New Key] = New Value
"""
dictValue = {"Key1":1, "Key2":2}
# print(dictValue["Key3"]) # print | Error | 존재하지 않는 Key에 접근해서 에러가 발생한다.

# 하지만 새 Key에 새 Value를 추가해주면 새 요소가 추가되기 때문에 에러가 발생하지 않는다.
dictValue["Key3"] = 3
print(dictValue)         # print | {'Key1': 1, 'Key2': 2, 'Key3': 3}
print(dictValue["Key3"]) # print | 3




# 008. 해당 Key의 Value를 수정
"""
     Dictionary[Key] = New Value
"""
dictValue = {"Key1":1, "Key2":2, "Key3":3}
dictValue["Key2"] = True
print(dictValue) # print | {'Key1': 1, 'Key2': True, 'Key3': 3}




# 009. 해당 Key를 이용하여 Item 삭제
"""
     del Dictionary[Key]
"""
dictValue = {"Key1":1, "Key2":2, "Key3":3}
del dictValue["Key2"]
print(dictValue) # print | {'Key1': 1, 'Key3': 3}




# 010. Key가 딕셔너리 안에 있는지 확인
dictValue = {"Key1":1, "Key2":2, "Key3":3}
print("Key1" in dictValue) # print | True
print("Key4" in dictValue) # print | False








# 딕셔너리 함수 _____________________________________________________________________________________________________

dictCup = {"Name":"다이소 스탠다드 컵", "Color":"노란색", "Price":3000, "Texture":"도자기", "Amount":3}


# 001. keys() | 모든 Key 얻기 | 객체 dict_keys로 반환
keys = dictCup.keys()
print(keys)       # print | dict_keys(['Name', 'Color', 'Price', 'Texture', 'Amount'])
print(type(keys)) # print | <class 'dict_keys'>

"""
     원래는 리스트"[]"로 반환을 했었는데 메모리 낭비를 줄이기 위해 dict_keys객체로 반환된다고 한다.
     내장형 함수인 list()를 이용하여 간단히 변경할 수 있다.
"""
print(list(keys)) # print | ['Name', 'Color', 'Price', 'Texture', 'Amount']






# 002. values() | 모든 Value 얻기 | 객체 dict_values로 반환
values = dictCup.values()
print(values)       # print | dict_values(['다이소 스탠다드 컵', '노란색', 3000, '도자기', 3])
print(type(values)) # print | <class 'dict_values'>

"""
     원래는 리스트"[]"로 반환을 했었는데 메모리 낭비를 줄이기 위해 dict_values객체로 반환된다고 한다.
     내장형 함수인 list()를 이용하여 간단히 변경할 수 있다.
"""
print(list(values)) # print | ['다이소 스탠다드 컵', '노란색', 3000, '도자기', 3]






# 003. items() | 모든 Item 얻기 | 객체 dict_items로 반환
items = dictCup.items()
print(items)       # print | dict_items([('Name', '다이소 스탠다드 컵'), ('Color', '노란색'), ('Price', 3000), ('Texture', '도자기'), ('Amount', 3)])
print(type(items)) # print | <class 'dict_items'>

"""
     원래는 리스트"[]"로 반환을 했었는데 메모리 낭비를 줄이기 위해 dict_items객체로 반환된다고 한다.
     내장형 함수인 list()를 이용하여 간단히 변경할 수 있다.

     dict_items의 Item은 Key와 Value를 동시에 표현해야 하기 때문에 Tuple로 구성되어 있다.
"""
print(list(items)) # print | [('Name', '다이소 스탠다드 컵'), ('Color', '노란색'), ('Price', 3000), ('Texture', '도자기'), ('Amount', 3)]






# 004. get() | Key로 Value 가져오기 | 만약 존재하지 않는 Key에 접근할 경우 Default_Value를 반환
dictValue = {"Key1":1, "Key2":2, "Key3":3}
# print(dictValue["Key4"]) # print | Error | 존재하지 않는 Key에 접근해서 에러가 발생한다.

"""
     하지만 get()함수를 이용하면 에러가 발생되지 않으며
     존재하지 않는 Key에 접근했을 경우 DefaultValue를 반환한다.

     따라서 안전하게 사용할 수 있다.
     _________________________________________________________________________________
     Dictionary.get(접근하려는 Key, 존재하지 않는 Key에 접근했을 경우 반환할 DefaultValue)
"""
value = dictValue.get("AccessKey", "DefaultValue")
print(value) # print | DefaultValue

# 예시
value = dictValue.get("Key4", None)
print(value)     # print | None

value = dictValue.get("Key1", None)
print(value)     # print | 1

# 주의할 점은 원본 Dictionary는 수정되지 않는다.
print(dictValue) # print | {'Key1': 1, 'Key2': 2, 'Key3': 3}






# 005. clear() | 딕셔너리의 모든 데이터 삭제
dictValue = {"Key1":1, "Key2":2, "Key3":3}
dictValue.clear()
print(dictValue) # print | {}





# 006. update() | Dictionary의 데이터를 갱신
"""
    dictCup["Price"] = 7000
    이런식으로 한개의 Item씩 갱신을 시켜줘도 되지만
    update()함수를 이용하면 여러개의 Item들을 한꺼번에 갱신시켜줄 수 있다.
    __________________________________________________________________
    구체적인 기능
         001. 기존의 Item은 수정
         002. 새로운 Item은 추가
"""
dictCup = {"Name":"다이소 스탠다드 컵", "Color":"노란색", "Price":3000, "Texture":"도자기", "Amount":3}
dictCup.update({"Name": "다이소 고급 도자기 컵", "Price": 5000, "Amount":5, "Place":"쇼핑몰"})
print(dictCup) # print | {'Name': '다이소 고급 도자기 컵', 'Color': '노란색', 'Price': 5000, 'Texture': '도자기', 'Amount': 5, 'Place': '쇼핑몰'}





# 007. copy() | Dictionary의 깊은 복사
""" Dictionary의 얕은 복사"""
dictA = {}
dictB = dictA
dictB["Key1"] = 1
print(dictB) # print | {'Key1': 1}
print(dictA) # print | {'Key1': 1}

""" Dictionary의 깊은 복사"""
dictA = {}
dictB = dictA.copy()
dictB["Key1"] = 1
print(dictB) # print | {'Key1': 1}
print(dictA) # print | {}





# 008. pop() | 해당 Key에 대한 Value를 반환 후 삭제
dictCup = {"Name":"다이소 스탠다드 컵", "Color":"노란색", "Price":3000, "Texture":"도자기", "Amount":3}
popped_value = dictCup.pop("Color")
print(popped_value) # print | 노란색
print(dictCup)      # print | {'Name': '다이소 스탠다드 컵', 'Price': 3000, 'Texture': '도자기', 'Amount': 3}





# 009. popitem() | 마지막 Item을 반환 후 삭제
dictCup = {"Name":"다이소 스탠다드 컵", "Color":"노란색", "Price":3000, "Texture":"도자기", "Amount":3}
random_key_value = dictCup.popitem()
print(random_key_value) # print | ('Amount', 3)

random_key_value = dictCup.popitem()
print(random_key_value) # print | ('Texture', '도자기')

random_key_value = dictCup.popitem()
print(random_key_value) # print | ('Price', 3000)

print(dictCup)          # print | {'Name': '다이소 스탠다드 컵', 'Color': '노란색'}

"""
     여기서 중요한 점
     _________________________________________________________________________________________
     Dictionary의 popitem()함수는 파이썬 3.7 이전 버전의 경우에는 임의로 Item을 pop하는 기능이었다.

     만약 파이썬 3.12에서 개발 중인데 파이썬 3.7 이전 버전으로 만들어진 라이브러리를 사용하면
     기능이 다른 Dictionary의 popitem()함수로 인해 문제가 발생할 수 있다.

     따라서 사용하려는 라이브러리나 개발 환경에 맞게 파이썬 버전을 설정하는 것이 중요하다.
"""







# 010. fromkeys() | Key로 이루어진 시퀀스로 Dictionary생성
"""
     주의할 점
         사용하기에 앞서 fromkeys()함수는 정적(클래스)함수로 사용하는 것이 좋다.
     _______________________________________________________________________________________________________________________
     정적 함수와 클래스 함수는 차이가 있지만 일단은 비슷한 원리로 사용된다고만 알아두자.
     _______________________________________________________________________________________________________________________
     정적(클래스) 함수
     dict.fromkeys() | 클래스에 직접 접근하여 사용하는 함수 | 여기서 dict는 인스턴스가 아니라 클래스이다.

     인스턴스 함수
     dictValue = {}
     dictValue.fromkeys() | 생성된 인스턴스에 접근하여 사용하는 함수 | 여기서 dictValue는 인스턴스이다.

     _______________________________________________________________________________________________________________________
     물론
     dictValue = {}
     dictValue = dictValue.fromkeys()
     이런식으로 인스턴스 함수의 값을 대입해서 사용해도 되지만

     dictValue = {}
     dictValue = dict.fromkeys()
     이런식으로 정적(클래스)함수를 사용하면 시스템적으로도 더 효율적이고 코드도 깔끔하다.
"""

"""
     NewDictionary = dict.fromkeys(Key | Key로 이루어진 시퀀스, Value | 공통으로 지정해 줄 기본 값 | 생략 시 None이 기본 값)
"""
# 리스트로 생성
dictValue = dict.fromkeys(["Key1", "Key2", "Key3"])
print(dictValue) # print | {'Key1': None, 'Key2': None, 'Key3': None}

# Tuple로 생성
dictValue = dict.fromkeys(("Key1", "Key2", "Key3"))
print(dictValue) # print | {'Key1': None, 'Key2': None, 'Key3': None}

# String으로 생성
dictValue = dict.fromkeys("ABCDEF")
print(dictValue) # print | {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}

# Range로 생성
dictValue = dict.fromkeys(range(10))
print(dictValue) # print | {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}

# dict_keys로 생성
dictCup = {"Name":"다이소 스탠다드 컵", "Color":"노란색", "Price":3000, "Texture":"도자기", "Amount":3}
dictValue = dict.fromkeys(dictCup.keys())
print(dictValue) # print | {'Name': None, 'Color': None, 'Price': None, 'Texture': None, 'Amount': None}

# ... 이 밖에도 Key를 가진 시퀀스라면 모두 가능하다.

"""
     두번째 인자는 Value인데 공통적으로 하나만 입력 가능하며 기본값은 None이다.
"""
dictValue = dict.fromkeys(["Key1", "Key2", "Key3"])
print(dictValue) # print | {'Key1': None, 'Key2': None, 'Key3': None} | 생략했으니 Value가 None으로 채워짐

dictValue = dict.fromkeys(["Key1", "Key2", "Key3"], "Default Value")
print(dictValue) # print | {'Key1': 'Default Value', 'Key2': 'Default Value', 'Key3': 'Default Value'}

dictValue = dict.fromkeys(["Key1", "Key2", "Key3"], 0)
print(dictValue) # print | {'Key1': 0, 'Key2': 0, 'Key3': 0}

dictValue = dict.fromkeys(["Key1", "Key2", "Key3"], False)
print(dictValue) # print | {'Key1': False, 'Key2': False, 'Key3': False}

"""
     첫번째 인자에는 ["Key1", "Key2", "Key3"]를 넣고
     두번째 인자에는 [1, 2, 3]를 넣어서
     {'Key1': 1, 'Key2': 2, 'Key3': 3}으로 구성된 딕셔너리가 생성된다고 생각할 수 있지만
     결과는 {'Key1': [1, 2, 3], 'Key2': [1, 2, 3], 'Key3': [1, 2, 3]}가 나온다.

     따라서 두번째 인자는 Value의 기본 값일 뿐이다.
"""
dictValue = dict.fromkeys(["Key1", "Key2", "Key3"], [1, 2, 3])
print(dictValue) # print | {'Key1': [1, 2, 3], 'Key2': [1, 2, 3], 'Key3': [1, 2, 3]}








# 011. setdefault() | Dictionary의 기본 값을 설정
"""
     기능
         001. Key가 Dictionary에 있으면 해당 Value를 반환
         002. Key가 Dictionary에 없으면 Key와 기본 값을 가진 Item을 추가
         003. default의 기본값은 None

     setdefault(key, default=None)
"""
dictValue = {"Key1":1, "Key2":2, "Key3":3}
print(dictValue.setdefault("Key1")) # print | 1
print(dictValue) # print | {'Key1': 1, 'Key2': 2, 'Key3': 3}

print(dictValue.setdefault("Key4")) # print | None | default를 생략
print(dictValue) # print | {'Key1': 1, 'Key2': 2, 'Key3': 3, 'Key4': None} | Key4가 존재하지 않으니까 추가

print(dictValue.setdefault("Key5", 5)) # print | 5
print(dictValue) # print | {'Key1': 1, 'Key2': 2, 'Key3': 3, 'Key4': None, 'Key5': 5} | Key5가 존재하지 않으니까 추가

# setdefault()함수로 데이터를 수정할 수 없다.
print(dictValue.setdefault("Key4", 4)) # print | None
print(dictValue) # print | {'Key1': 1, 'Key2': 2, 'Key3': 3, 'Key4': None, 'Key5': 5}

# 만약 수정하려면 이전에 배웠던 것들을 활용하면 된다.
"""
     dictValue["Key4"] = 4
     print(dictValue)

     또는

     dictValue.update({"Key4":4})
     print(dictValue)
"""





# 012. len() | Dictionary의 길이를 int형으로 반환
dictValue = {"Key1":1, "Key2":2, "Key3":3}
length = len(dictValue)
print(length) # print | 3