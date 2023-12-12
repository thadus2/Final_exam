#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201807 이름 : 박승훈

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_strung, target):
    if(my_strung.find(target) > -1):    #find 함수는 찾는 문자열이 처음 나온 위치를 반환합니다.
        answer = 1                      #찾는 문자열이 해당 문자열 내에 없으면 -1을 반환하므로 find가 1보다 큰 경우를
    else:                               #target이 my_strung 내에 있다고 판단, 1을 리턴. 아닐 경우
        answer = 0                      #target이 my_strung 내에 없다고 판단, 0을 리턴.
    return answer

strung = "Life is too short, you need python."
tag1 = "you"
tag2 = "love"

print(solution(strung,tag1))            #strung 내에 찾는 문자열이 있는 경우
print(solution(strung,tag2))            #strung 내에 찾는 문자열이 없는 경우
# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = {                           #모스부호 해석표가 딕셔너리로 주어짐
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z' , '---.' : ' '}
    answer = ''
    split = letter.split()              #주어진 문자열 letter가 기본값 ' '을 기준으로 list로 split됨
    for trans in split:                 #새로운 문자열 trans로 split 안의 모든 변수를 반복함 ex)... -> - -> .
        answer += morse[trans]          #morse 딕셔너리 안에 trans 에 대응되는 원소를 answer에 추가해줌. ex)... -> s
    return answer

letter="... - . .- .-.. ---. - .... . ---. ... .... --- .--"
print(solution(letter))                 #출력 결과 : steal the show

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.
def solution(age):
    if age>1000 or age<0:                       #age의 범위를 제한함
        print("잘못된 입력입니다.(0<age<=1000)")
        return 0
    prg = {                                     #각 숫자 나이에 대응되는 알파벳 나이를 딕셔너리로 구현함
        '0' : 'a' , '1' : 'b' , '2' : 'c' ,
        '3' : 'd' , '4' : 'e' , '5' : 'f' ,
        '6' : 'g' , '7' : 'h' , '8' : 'i' , '9' : 'j' }
    answer = ''
    age = " ".join(str(age)).split()            #입력받은 숫자 age를 문자열로 변경 후, 공백 " "을 추가시킨 후 list로 변경함
    for ret in age:                             #문자열 ret를 age 리스트의 원소만큼 반복함 ex)9 -> 2 -> 8
        answer += prg[ret]                      #prg 딕셔너리 안에 ret에 대응되는 원소를 answer에 추가함 ex)0 -> a, 9 -> j
    return answer

age = 928
print(solution(age))                            #출력 결과 : jci

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    if(r1>r2):                              #원 r1이 원 r2보다 커야하므로 조건을 걸었음
        print("r1이 r2보다 작아야합니다.")
        return 0
    answer = 0
    for y in range (r2):                    #y를 0부터 r2 원 반지름까지 반복함
        if(y>=r1):                          #y가 r1 반지름보다 클 경우
            x1 = 1                          #x1 = 1
        else:
            x1 = (r1 ** 2 - y ** 2) ** 0.5  #아닐 경우 x1 좌표는 피타고라스를 이용하여 구함
        x2 = int((r2 ** 2 - y ** 2) ** 0.5) #x2 좌표는 r2 원의 x좌표를 피타고라스를 이용하여 구함
        answer += int(x2 - x1) + 1          #원 사이의 점 갯수는 두 원의 x좌표 차이 + 1임
    return answer * 4                       #1사분면 내의 점을 구하고, x4를 하여 4사분면 만큼 점 갯수를 구하였음

print(solution(2,3))                 #출력 결과 : 20

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    numbers = list(map(str, numbers))                               #주어진 numbers 리스트의 모든 원소를 문자열로 바꾸어줌
    for i in range (len(numbers)):
        for j in range(i+1,len(numbers)):                           #각 원소들의 크기를 비교하기 위한 반복문
            if (numbers[i] + numbers[j] < numbers[j] + numbers[i]): #i번째 원소와 j번째 원소를 조합하여 만든 문자열 크기 비교
                numbers[i], numbers[j] = numbers[j], numbers[i]     #ex) 17과 2의 조합 172와 217을 비교하여 정렬
    answer = ''.join(numbers)                                       #리스트를 구분 없이 하나의 문자열로 합침
    return answer

numbers = [8, 30, 17, 2, 23]
print(solution(numbers))                                      #출력 결과 : 83023217