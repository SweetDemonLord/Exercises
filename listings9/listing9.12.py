class Alpha:
    def __init__(self,val):
        self.val = val
    # Method for the "equal" operator
    def __eq__(self,val):
        print("Alpha: 'equals'")
        return self.val == val
    # Method for the "not equal" operator
    def __ne__(self,val):
        print("Alpha: 'not equals'")
        return self.val != val
    # Method for the "less" operator
    def __lt__(self,val):
        print("Alpha: 'less'")
        return self.val < val
    # Method for "greater than or equal to" operator
    def __ge__(self,val):
        print("Alpha: 'greater or equals'")
        return self.val >= val
class Bravo:
    def __init__(self,val):
        self.val = val
    # Method for the "equal" operator
    def __eq__(self,val):
        print("Bravo: 'equals'")
        return self.val == val
# Creating objects and performing comparisons
A=Alpha(100)
print("Operations with object A")
print("[01] A==100:", A==100)
print("[02] A!=100:", A!=100)
print("[03] 200==A:",200==A)
print("[04] 200!=A:",200!=A)
print("[05] A<200:",A<200)
print("[06] 200>A:",200>A)
print("[07] A>=200:",A>=200)
print("[08] 100<=A:",100<=A)
B=Bravo(300)
print("Operations with object B")
print("[9] B==300:", B==300)
print("[10] B!=300:", B!=300)
print("[11] 400==B:",400==B)
print("Comparison of objects A and B")
print("[12] A==B:",A==B)
print("[13] B!=A:",B!=A)
print("[14] A!=B:",A!=B)