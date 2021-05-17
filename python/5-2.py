#리스트

li = [3,1,'배',4,'고파',5,1]
st = [1,2,3,5,4]

#indexing slicing 
print(li[3]) #4 반환
print(li[0:2]) #3,1 반환

#리스트의 길이 len()
print(len(li))

#리스트 오름차순 정렬 sort()
st.sort()
print(st)

#리스트 내 특정 원소의 인덱스 .index()
print(li.index('배'))

#리스트 내 특정 원소의 개수 .count()
print(li.count(2))