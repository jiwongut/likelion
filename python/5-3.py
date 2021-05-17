#딕셔너리

pairs = {'잔나비' : 'she', '선우정아' : '도망가자', '아이유' : '어푸'}

#하나의 key-value를 추가하는 방법
pairs['이하이'] = '한숨'

#특정 key-value를 삭제하는 방법 del[]
del pairs['잔나비']

#key로 value 얻기 .get()
k = pairs.get('아이유')
print(k)