"""
____________________________________________________________________________________________________________________
Chapter009.반복문(for, while)
____________________________________________________________________________________________________________________
"""

# range 객체 ________________________________________________________________________________________________________

"""
     range 객체
     _______________________________
     생성자
     range(start = 0, stop, step=1)

     start | 시작 값
     stop  | 끝 값
     step  | 스텝
"""
for i in range(10): # 0 ~ 9까지
    print(i, end = " | ") # print | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

print("")

for i in range(1, 11): # 1 ~ 10까지 # print | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
    print(i, end = " | ")

print("")

for i in range(3, 10, 3): # 3 ~ 9까지 3씩 증가
    print(i, end = " | ") # print | 3 | 6 | 9 |

print("")







# for문 ________________________________________________________________________________________________________

"""
     for문
     _______________________________
     for [element]... in [iterable]:
         [Todo Stub]
"""
# range ___________________________________________________________________________________
for e in range(10):
    print(e, end=" | ") # print | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

print("")

# string ___________________________________________________________________________________
for e in "hello":
    print(e, end=" | ") # print | h | e | l | l | o |

print("")

# list ___________________________________________________________________________________
for e in ["A", 2, True, 2 + 3j, 1.2]:
    print(e, end=" | ") # print | A | 2 | True | (2+3j) | 1.2 |

print("")

# tuple ___________________________________________________________________________________
for e in ("A", 2, True, 2 + 3j, 1.2):
    print(e, end=" | ") # print | A | 2 | True | (2+3j) | 1.2 |


print("")

# set ___________________________________________________________________________________
# set는 순서가 보장되는 sequence타입이지만 반복가능한 객체인 iterable이라서 for문 사용이 가능하다.
# 하지만 순서가 뒤죽박죽이라 굳이 이렇게 사용하지는 않음
set = {"감자", "토마토", "사과", "바나나"}
for e in set:
    print(e, end=" | ") # print | 사과 | 바나나 | 감자 | 토마토 |

print("")

# set값을 정렬해서 사용하려면 이런 방법도 있다.
# set > list > sort
list = list(set)
list.sort()
for e in list:
    print(e, end=" | ") # print | 감자 | 바나나 | 사과 | 토마토 |

print("")

# dict ___________________________________________________________________________________
dictionary = {"Apple":1000, "Banana":2000, "Melon":3000, "Kiwi":4000, "Tomato":5000}
for e in dictionary:
    print(e, end=" | ") # print | Apple | Banana | Melon | Kiwi | Tomato |

print("")

# dict는 for문을 사용하면 기본적으로 key가 [element]로 넘어간다.
# 사실상 dict.keys()를 사용한 것과 같은 결과물을 얻을 수 있다.
for e in dictionary.keys():
    print(e, end=" | ") # print | Apple | Banana | Melon | Kiwi | Tomato |

print("")

# 따라서 value들만 얻고 싶을 경우 dict.values()를 이용해주면 된다.
for e in dictionary.values():
    print(e, end=" | ") # print | 1000 | 2000 | 3000 | 4000 | 5000 |

print("")

# 원리를 생각해보면 dict.items()도 가능하다.
for e in dictionary.items():
    print(e, end=" | ") # print | ('Apple', 1000) | ('Banana', 2000) | ('Melon', 3000) | ('Kiwi', 4000) | ('Tomato', 5000) |

print("")

for e in dictionary.items():
    print(type(e), end=" | ") # dict_items(list((tuple, tuple, tuple))) 구조로 되어 있기 때문에 [element]는 최소단위인 tuple이 된다.

print("")

for e in dictionary.items():
    print(f"e[0] = {e[0]}, e[1] = {e[1]}", end=" | ") # [element]는 tuple이니까 인덱스[0]에는 key가 인덱스[1]은 value가 존재한다.

print("")

# 하지만 파이썬은 굉장히 유연한 프로그래밍 언어이기 때문에 [element]가 여러개 올 수 있다.
# dict.items()의 [element]를 1개로 받았을 때는 tuple로 받았지만,
# dict.items()의 [element]를 2개로 받았을 때는 key와 value로 나누어서 받게 된다.
for k, v in dictionary.items():
    print(k, v, end=" | ") # print | Apple 1000 | Banana 2000 | Melon 3000 | Kiwi 4000 | Tomato 5000 |

print("")


# 만약 for문에서 [element]없이 사용하고 싶을 경우 _를 사용하면 된다.
for _ in range(10):
    print("0", end=" | ") # print | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

print("")



# while문 ________________________________________________________________________________________________________
"""
     while문
     _____________________________________________________
     while [condition]:
        [Todo Stub]
     _____________________________________________________
     while문은 [condition]이 True일 경우에 실행된다.
     반대로 생각해본다면 [condition]이 False일 경우 종료된다.
"""

# 로직 001
i = 0
while i < 10:
    print(i, end=" | ") # print | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
    i+=1

print("")

# 로직 002
i = 0
while i < 10:
    i+=1
    print(i, end=" | ") # print | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |

print("")

# 로직 003
i = 10
while i > 0:
    print(i, end=" | ") # print | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
    i-=1

print("")

# 로직 004
i = 10
while i > 0:
    i-=1
    print(i, end=" | ") # print | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |

print("")

# 로직 005
i = 0
while i < 10:
    print(i, end=" | ") # print | 0 | 3 | 6 | 9 |
    i+=3

print("")


# 무한루프
"""
     자칫 프로그래밍을 잘못할 경우 무한루프에 빠질 수 있다.
     물론 무한루프 또한 활용이 가능하다.
"""
"""
while True:
    print("무한루프")
"""