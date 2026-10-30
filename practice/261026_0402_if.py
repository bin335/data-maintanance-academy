# 조건문
# if 기본 구조 - 콜론과 들여쓰끼 (코드 블록)
# 형식:
# if 조건식:
#  실행할 코드 (들여쓰기) -> 자동으로 들여쓰기 적용됨
temp = 85
if temp>80:              # 콜론: 블록 시작 신호
    print("온도 주의")    # 들여쓰기 안 -> 조건 참일 때만 실행
    print("점검 요망")    
print("측정 종료")        # 들여쓰기 끝 -> 조건과 무관하게 항상 실행

# else - 조건이 거짓일 때
# 형식:
# if 조건문:   
#   참일 때 코드
# else:        
#   거짓일 때 코드

score = 55
if score >= 60:
    print('합격')
else:
    print('불합격')

print('실습1: 조건 하나로 나이 판정하기')
age= 18
if age>=19:
    print('성인입니다.')
else:
    print('미성년자입니다.')


# elif
# 형식:
# if ... elif ... else (위에서부터 검사, 처음 참인 곳만 실행)

score = 82
if score >= 90:
    print('우수')
elif score>=70:
    print('보통')
else:
    print('미흡')

print('실습2: 여러갈래로 점수 등급 판정하기')
score= 69
if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
else:
    print('F')

# 논리 연산자 and or not / 범위 조건
temp=45
print(temp>=20 and temp <=60)

if 20<= temp <= 60:
    print('정상범위')

print('실습3: 설비 온도 상태 판정하기')
temp= 70
if temp>80:
    print('위험')
elif temp>60: 
    print('주의')
else:
    print('정상')

print('실습4: 두 조건을 모두 만족하는지 검증하기')
id= input('id: ')
pw= int(input('pw: '))

if id== 'admin' and pw==1234:
    print('로그인 성공')
else:
    print('로그인 실패')

print('실습5: 세 값으로 설비 종합 상태 판정하기') 
temp= int(input('온도: '))
vib= float(input('진동: '))
current= int(input('전류: '))

if temp>80 or vib>4.0:
    print('위험: 즉시정지')
else:  # 중첩if: 아래에 나오는 조건문은 else에 귀속되는 코드기에, 반드시 들여쓰기 -> Tab 들여쓰기
    if current>60 and temp>70:
        print('주의: 부하점검')
    elif vib>2.5:
        print('주의: 진동관찰')
    else:
        print('정상')