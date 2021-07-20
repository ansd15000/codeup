# 연월일 입력받고 순서바꿔 출력
def q6019():
    a = input().split('.')
    print('-'.join(reversed(a)))

def q6020():
    print(input().replace('-',''))

# 연월일 입력받아 나누어 출력하기
# input = 200304
def q6022():
    start = 0
    a = input()
    for i in range(2, len(a)+1, 2):
        print(a[start:i])
        start = i

# 분 출력하기
# input = 17:23:57 or 6:00:00 or 4:4:4
def q6023():
    a = input()
    start = a.index(':') + 1
    end = a.rfind(':')
    print(a[start: end])

# 실수 합
def q6026():
    print(sum([float(input()) for _ in range(2)]))

# 10 -> 16
def q6027():
    # print(hex(int(input()))[2:])
    # print(f'{int(input()):x}') # 변환하는 또 다른 방법 
    # 직접 구현. 이게 제일 빠르네
    a = int(input())
    h = {
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f',
    }
    def convert(n):
        if n >= 10:
            return h[n]
        return str(n)
    l = []
    def z(n):
        if int(n / 16) == 0 :
            l.append(convert(n))
            return
        l.append(convert(n%16))
        n = int(n / 16)
        z(n)
    z(a)
    print(''.join(reversed(l)))

def q6029():
    print(f'{int(input(),16):o}') # 8진수 변환

def q6033():
    print(chr(ord(input())+1))

def q6043():
    a, b = map(float, input().split())
    print(f'{a/b:.3f}')

def q6045():
    a = list(map(int, input().split()))
    print(sum(a), f'{sum(a)/len(a):.2f}')

# 비트연산자. 2진수에서 자리수 이동시키는 정도가 뒤에 숫자로 입력함. not: ~, or: |, and: &, xor: ^
def q6046():
    print(int(input())<<1)

def q6047():
    a, b = map(int, input().split())
    print(a << b)

def q6048():
    a, b = map(int, input().split())
    print(a < b)

def q6064():
    a = map(int, input().split())
    print(min(a))

def q6079():
    a = int(input())
    res = 0
    i = 1
    while res < a:
        res+=i
        i+=1
    print(i-1)

    pass

def q6078():
    while True:
        a = input()
        print(a)
        if a == 'q': break

def q6082():
    for i in range(1, int(input()) + 1):
        a = i % 10
        if a == 0: 
            print(i, end=' ')
            continue
        if a % 3 == 0:
            print('X', end=' ')
        else: 
            print(i, end= ' ')

# 이딴걸 이따구로 어렵게 푼 내가 씹바보란거겠지
def q6083():
    rgb = list(map(int, input().split()))
    a = [0,0,0]
    cnt =1
    while a != list(map(lambda x:x-1, rgb)):
        if a[2] == rgb[2]-1 :
            if a[1] == rgb[1]-1:
                print(' '.join(map(str,a)))
                cnt+=1
                a[0]+=1
                a[1:] = [0,0]
                continue
            print(' '.join(map(str,a)))
            cnt+=1
            a[1]+=1
            a[2] = 0
            continue
        print(' '.join(map(str,a)))
        cnt+=1
        a[2] += 1
    print(' '.join(map(str,a)))
    print(cnt)

def q6083_2():
    r, g, b = map(int, input().split())
    for i in range(r):
        for j in range(g):
            for k in range(b):
                print(i,j,k)
    print(r*g*b)

def q6084():
    res = 1
    for i in map(int, input().split()):
        res*= i
    res /= (8 * 1024 ** 2) # mb
    print(f'{round(res,1)} MB')

# rgb = 24bit (각각 8bit, 256개)
def q6085():
    res = 1
    for i in map(int, input().split()):
        res*= i
    res /= (8 * 1024 ** 2) # mb
    print(f'{res:.2f} MB') # 알아서 반올림 해줌

def q6086():
    a = int(input())
    res = 0
    i = 1
    while res < a:
        res +=i
        i += 1
    print(res)

def q6087():
    for i in range(1, int(input())+1):
        if i % 3 != 0: print(i, end = ' ')

def q6088():
    a, d, n = map(int, input().split())
    for _ in range(n-1):
        a += d
    print(a)

def q6089():
    a, d, n = map(int, input().split())
    for _ in range(n-1):
        a *= d
    print(a)

def q6090():
    a, m, d, n = map(int, input().split())
    for _ in range(n-1):
        a = a *m + d
    print(a)

def q6091():
    a,b,c = map(int, input().split())
    d = 1
    while d%a!=0 or d%b!=0 or d%c!=0 : # 셋다 나눠지는 수 계산하기
        d += 1
    print(d)

# 시간 줄이기 ㅋㅋ; 입력값 3개일뿐이니까
def q6091():
    a = sorted(map(int, input().split()))
    res = 1
    if a[0] != 1 and list(map(lambda x: x % min(a), a)).count(0) == 3 :
        res = a[-1]
    elif (a[0] * a[2]) % a[1] == 0: 
        res = a[0] * a[2]
    elif (a[1] * a[2]) % a[0] == 0:
        res = a[1] * a[2]
    else:
        for i in a: res *= i
    print(res)

def q6092():
    n = int(input())
    res = [0]*23 # 23명 제한
    for i in map(int, input().split()):
        res[i-1] +=1
    print(' '.join(map(str,res)))

def q6093():
    n = int(input())
    print(' '.join(map(str, reversed(list(map(int, input().split()))))))

def q6095():
    a = [ [0]*19 for _ in range(19) ] # 빈 2차원 배열생성
    for _ in range(int(input())):
        i, j = map(int, input().split())
        a[i-1][j-1] = 1

    for i in a:
        print(' '.join(map(str,i)))

def q6096():
    a = []
    for _ in range(19):
        a.append(input().split())
    for _ in range(int(input())): # n번 반복
        x, y = map(int, input().split())
        for idx, v in enumerate(a[x-1]):
            if v == '0' : a[x-1][idx] = '1'
            else: a[x-1][idx] = '0'
        for i in range(19):
            if a[i][y-1] == '0' : a[i][y-1] = '1'
            else: a[i][y-1] = '0'
    for i in a:
        print(' '.join(i))

def q6097():
    x,y = map(int, input().split())
    a = [['0'] * y for _ in range(x)]
    for _ in range(int(input())):
        l, d, x, y = map(int,input().split())
        x -= 1
        y -= 1
        if d == 0: # 가로 
            for i in range(l): 
                a[x][y+i] = '1'
        else:
            for i in range(l): 
                a[x+i][y] = '1'

    for i in a:
        print(' '.join(i))

def q6098():
    a = [ input().split() for _ in range(10) ]
    start_x, start_y = 1, 1
    
    def move_right(x, y):
        while a[x][y] != '1':
            if a[x][y] == '2': 
                a[x][y] = '9'
                return None, None
            # elif a[x][y] == '0': a[x][y] = '9'
            else: 
                a[x][y] = '9'
            y += 1
        y -= 1
        x, y = move_down(x,y)
        if x is None: 
            return
        else:
            move_right(x, y)

    def move_down(x,y):
        while a[x][y+1] == '1':
            if a[x][y] == '2': 
                a[x][y] = '9'
                return None, None
            else:
                a[x][y] = '9'
            x+=1
            if x == 9: return None, None # 테두리에 닿았다면 끝.
        return x, y
    
    move_right(start_x, start_y)
    
    for i in a:
        print(' '.join(i))