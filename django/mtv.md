# django 입문

## 1. 명령어  
``` 
python -m [가상환경명] ex)myvenv  
source [가상환경명]/bin/activate  
source [가상환경명]/Script/activate    

pip install django  
django-admin startproject [프로젝트명]  
  
python manage.py runserver
```
## 2. mtv  
### Model / Template / View
i) Template
  + 사용자가 보이는 영역(front end)
  + template 언어  
  
ii) Model
  + 데이터베이스 (DB)  
  
iii) View
  + 전달받은 데이터를 처리하는 핵심 부분
 
iv) 과정  
검색창에 '당근' 검색 시 Template에서 입력, View로 '당근'이라는 정보 
