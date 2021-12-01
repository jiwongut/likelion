#문자열
#터미널 출력 시 python 파일명

str = "멋쟁이 사자처럼"
print(str[0]) #index
print('yes')

#문자열의 길이 len()
print(len(str))

#문자열 내에서 특정 문자 등장 횟수 count()
print(str.count('사'))

#문자열 (특정 기준으로) 나누기 split()
print(str.split()) #공백을 기준으로
print(str.split(',')) #쉼표를 기준으로

#특정 문자의 인덱스 찾기 find(), index()
print(str.find('사'))
print(str.index('사'))
