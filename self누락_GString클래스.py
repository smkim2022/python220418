# 전역변수
str = "Not Class Member"

# 파이썬은 명확하게 코딩하는 것이 좋다!
# 클래스를 정의
class GString:
    def __init__(self):
        self.str = "" 
    # setter
    def set(self, msg):
        self.str = msg
    # getter
    def print(self):
        #버그 발생!, self 를 안붙이면 전역변수 가져온다.
        #print(str)
        print(self.str)

g = GString()
g.set("First Message")
g.print()
