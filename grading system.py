print("Enter your marks in 5 subjects")
mark_one=int(input())
mark_two=int(input())
mark_three=int(input())
mark_four=int(input())
mark_five=int(input())
tot=mark_one+mark_two+mark_three+mark_four+mark_five
avg=tot/5

if avg>=91 and avg<100:
    print("the score is A1")

elif avg>=81 and avg<91:
    print("the score is A2")

elif avg>=71 and avg<81:
    print("the score is B1")

elif avg>=61 and avg<71:
    print("the score is B2")
elif avg>=51 and avg<61:
    print("the score is C1")

elif avg>=41 and avg<51:
    print("the score is C2")
elif avg>=31 and avg<41:
    print("the score is D1")
elif avg>21 and avg<31:
    print("the score is D2")
elif avg>=11 and avg<21:
    print("the score is E1")
elif avg>=0 and avg<11:
    print("the score is E2")
else:
    print("not valid input")    