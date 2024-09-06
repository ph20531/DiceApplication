"""
____________________________________________________________________________________________________________________
Chapter005.리스트(List)
____________________________________________________________________________________________________________________
"""

# 리스트 사용법 _____________________________________________________________________________________________________

# 001. 비어있는 리스트 선언이 가능하다.
listValue = []
print(listValue)




# 002. 해당 인덱스에 값을 수정할 수 있다.
listValue = [1, 2.3, "cake"]
listValue[1] = True
print(listValue)




# 003. 해당 인덱스의 값을 제거할 수 있다.
listValue = [1, 2.3, "cake"]
del listValue[1]
print(listValue)

# 슬라이싱을 활용해서 제거 가능하다.
listValue = [1, 2.3, "cake"]
del listValue[0:2] # 0~1번지 까지 값을 제거
print(listValue)




# 004. 리스트도 슬라이싱이 가능하다.
listValue = [5, 1.5, "cup"]
print(listValue[0:2])




# 005. 리스트안에 해당 값이 포함되어있는지 알아낼 수 있다.
listValue = [8, 3.2, "java"]
print("java" in listValue) # Boolean 값으로 반환




# 006. 리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)




# 007. 리스트 반복하기(*)
a = [1, 2, 3]
b = a * 3
print(b)







# 리스트 함수 _______________________________________________________________________________________________________

# 001. len() | length = 길이 | 리스트의 길이를 int로 반환
"""
     len() 함수는 인덱서의 길이를 알아낼 수 있는 시스템 함수이다.
     String이나 List등의 인덱서를 가진 객체의 내부 함수가 아니다.

     내부 함수의 경우 <해당하는 객체.함수()>의 형태로 사용한다.
     하지만 len()의 경우 내부함수가 아니기 때문에 <len(인덱서 객체)>의 형태로 사용한다.
"""
listMethod = [None, 1, 2.2, True, 'c', "cake", 1 + 2j]
print(len(listMethod))




# 002. append() | 추가하다 | 리스트의 맨 마지막에 값을 추가한다.
listMethod = []
print(listMethod)

listMethod.append(False) # 마지막에 값을 추가
print(listMethod)

listMethod.append(3.2) # 마지막에 값을 추가
print(listMethod)




# 003. remove() | 제거하다 | 리스트에서 첫번째로 나오는 지정해준 값을 제거한다.
listMethod = [1, 2, 3, 1, 2, 3]

listMethod.remove(2) # 첫번째로 나오는 값 제거
print(listMethod)

listMethod.remove(2) # 첫번째로 나오는 값 제거
print(listMethod)




# 004. extend() | 확장하다 | 리스트1에 리스트2의 값을 추가하여 확장시켜준다.
list1 = [1, 2, 3]
list2 = [True, 1.5, "cake"]

list1.extend(list2) # list1에 list2값을 확장시킴
print(list1) # list1은 확장이 되었지만
print(list2) # list2는 값으로만 쓰였기 때문에 변화가 없다.




# 005. insert() | 삽입하다 | 원하는 위치에 원하는 값을 삽입시켜준다.
listMethod = [1, 2, 3]
listMethod.insert(1, "cake") # 무조건 지정해준 인덱스에 지정해준 값이 삽입된다.

# 값을 차지하고 뒤에 값들은 인덱스가 밀려난다.
print(listMethod)

listMethod.insert(9999, True) # 만약에 지정해준 위치가 인덱서의 길이(lenth)를 넘어버리면 자동으로 리스트의 마지막 위치에 값을 삽입한다.
print(listMethod)

listMethod.insert(-9999, False) # 만약에 지정해준 위치가 0(최소 인덱스)보다 낮으면 자동으로 리스트의 첫번째 위치에 값을 삽입한다.
print(listMethod)




# 006. sort() | 정렬하다 | 정렬할 수 있는 값을 순서대로 정렬해준다. | 예를들어 숫자나 알파벳이 해당
# 숫자의 경우
listMethod = [5, 3, 1, 4, 2]
listMethod.sort()
print(listMethod)

# 문자의 경우
listMethod = ["e", "c", "a", "d", "b"] # 알파벳 가능
listMethod.sort()
print(listMethod)

listMethod = ["e", "C", "A", "d", "b"] # 대소문자별로 정렬
listMethod.sort()
print(listMethod)

listMethod = ["ㅁ", "ㄷ", "ㄱ", "ㄹ", "ㄴ"] # 한글도 가능
listMethod.sort()
print(listMethod)

listMethod = ["문", "도", "김", "류", "나"] # 연락처 앱과 같은 기능
listMethod.sort()
print(listMethod)




# 007. reverse() | 뒤집다 | 리스트의 값을 역순으로 뒤집는다.
listMethod = [None, 1, 2.2, True, 'c', "cake", 1 + 2j]
listMethod.reverse()
print(listMethod)




# 008. index() | 인덱스 | 지정해준 값의 인덱스값을 int로 반환
listMethod = [None, 1, 2.2, True, 'c', "cake", 1 + 2j]
print(listMethod.index('c')) # 'c'값은 리스트에서 4번째 인덱스에 있기 때문에 정수 4를 반환

# Error | 만약 리스트안에 없는 값을 찾으려고 하면 에러가 발생한다.
# print(listMethod.index(False))




# 009. pop() | 꺼내다 | 리스트의 맨 마지막 요소를 반환하고 그 요소는 삭제한다.
# 파라미터를 생략하면 기본적으로 마지막 요소가 pop
listMethod = [1, 2, 3, 4, 5]
print(listMethod.pop()) # 기본적으로 마지막 값을 꺼내서 5가 출력
print(listMethod) # 5를 꺼내서 출력했으니 리스트에서는 값이 사라짐

# 파라미터에 인덱스 값을 입력해주면 해당 위치의 요소가 pop
listMethod = [1, 2, 3, 4, 5]
print(listMethod.pop(2)) # 지정해준 위치의 값을 꺼내서 3이 출력
print(listMethod) # 3을 꺼내서 출력했으니 리스트에서는 값이 사라짐




# 010. count() | 개수를 세다 | 지정해준 값의 총 수를 세서 int로 반환
listMethod = ['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd']
print(listMethod.count('a')) # 리스트 안에 'a'값은 1개
print(listMethod.count('b')) # 리스트 안에 'b'값은 2개
print(listMethod.count('c')) # 리스트 안에 'c'값은 3개
print(listMethod.count('d')) # 리스트 안에 'd'값은 4개

print(listMethod.count('z')) # 리스트 안에 'z'값은 없기 때문에 0개




# 011. copy() | 복사하다 | 깊은 복사를 통해 아예 별개의 리스트로 만들어준다.
# 기본적으로 리스트B에 리스트A를 대입하면 얕은 복사가 되어 값이 공유가 된다.
listA = []
listB = listA

listB.append(True)
print(listA) # B의 값을 바꾸고 A를 출력했더니 값이 똑같이 바뀜
print(listB)

listA.append(False)
print(listB) # 마찬가지로 A의 값을 바꾸고 B를 출력했더니 값이 똑같이 바뀜
print(listA)

"""
      따라서 깊은 복사라는 개념이 필요하다.
      깊은 복사를 통해 값을 대입해줄 수 있도록 도와주는 함수가 바로 copy()함수다.
"""

listA = []
listB = listA.copy() # 리스트A의 값을 깊은 복사해서 리스트B에 대입

listB.append(True)
print(listB) # 깊은 복사를 통해 값을 대입했기 때문에 따로 관리가 된다.
print(listA)

listA.append(False)
print(listA) # 깊은 복사를 통해 값을 대입했기 때문에 따로 관리가 된다.
print(listB)

"""
      따라서 리스트의 경우 얕은 복사와 깊은 복사의 개념을 잘 이해해서 사용해야 한다.

     < 요약 >
         리스트끼리 일반적으로 대입하면 얕은 복사          | 얕은 복사 = 값이 공유
         리스트끼리 copy()를 이용하여 대입하면 깊은 복사   | 깊은 복사 = 값이 따로 관리
"""




# 012. clear() | 전혀 없다 | 리스트 안에 있는 모든 값을 모두 제거한다.
listMethod = [None, 1, 2.2, True, 'c', "cake", 1 + 2j]
print(listMethod)

listMethod.clear()
print(listMethod) # 비어있는 리스트가 되어 버린다.






"""
     Notice.
     _____________________________________________________________________________________________

     오늘 수업에서 리스트의 내부 함수는 모두 알려주었지만 상황에 따라 쓰임법은 검색해서 공부하는게 좋다.
     _____________________________________________________________________________________________
"""