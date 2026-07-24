# 영어 타자 프로그램

#word.txt
#섞는다 random.shuffle()
#임의로 하나 추출 random.choice
#time.time() 현재 시간을 실수 형태로 리턴

#Q1. then
# input()
#input결과에 따라서 정답!!  or 오타!!

#문제 5문제 출제
# 정답 개수

# 게임 시간 출력
# 출력문 = > 게임 시간 : 10초, 정답개수:3개

# 3개이상 정답인 경우 합격 or 불합격


# start = time.time()



# import random
# import time

# with open(r"C:\source\pythonsource\ch1\data\word.txt", "r", encoding="utf-8") as f:
#     word_list = [line.strip() for line in f]

# random.shuffle(word_list)
# random.choice(word_list,5)
# q_count = 0
# correct_count = 0

# while q_count <= 5:


    
    

# end = time.time()


import time
import random
n, corr_cnt = 1, 0
#n : 반복횟수 카운트, corr_cnt : 정답 개수 카운트
start = time.time()

words = []

with open(r"C:\source\pythonsource\ch1\data\word.txt","r",encoding="utf-8")as f:
    for word in f:
        words.append(word.strip())

# print(wrods)
while n <= 5:
    random.shuffle(words)
    q = random.choice(words)
    print(f"Q{n}")

    print(q)

    answer = input()
    if answer == q.strip():
        print("정답!!")
        corr_cnt += 1 
    else:
        print("오타")

        #문제 개수 추가
    n += 1

#끝난 시간
end = time.time()
et = end - start
et = fomat(et,".3f")

print(f"게임시간 : {et}초, 정답 개수: {corr_cnt}개")
if corr_cnt >= 3:
    print("합격")
else:
    print("불합격")
