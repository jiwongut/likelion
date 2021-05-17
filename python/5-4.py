#제어문 - if문(분기문)

#예제 1
#85점 이상 pass, 아니면 fail
score = int(input("점수를 입력하세요: "))
if(score>=85):
    print("pass")
else:
    print("fail")

#예제 2
activity = input("동아리 뭐야?: ")
if(activity=="멋쟁이사자처럼"):
    print("어, 너도야?")
else:
    print("그렇구나...")

#예제 3
#5000이상: 아웃백/ 3000이상: 학식/ 1000이상: 컵라면/ ㅠㅠ: 공기밥
#else if = elif
money = int(input("돈 얼마있어?: "))
if(money>=5000):
    print("아웃백 가자")
elif(money>=3000):
    print("학식 먹자")
elif(money>=1000):
    print("컵라면 먹자")
else:
    print("ㅠㅠ 공기밥 먹자...")