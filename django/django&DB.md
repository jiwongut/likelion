### 장고와 데이터베이스
------------
## ORM (Object Relation Mapping)
------------
> ORM이란? 객체(Object)와 관계형 데이터베이스(Relation)를 sql 쿼리를 사용하지 않고 연결(Mapping)해주는 것을 뜻한다. 
> 장고(django)의 ORM을 이용하여 데이터베이스에서 데이터를 생성(Create)하고, 읽고(Read), 갱신하고(Update), 삭제(Delete)할 수 있다.  

## CRUD
# Read
```
앱 내에서 template 폴더 생성 후 views.py 파일을 생성한다.
---
from .models import Blog  

def home(request):
  blogs = Blog.objects.all() // Blog 내 모든 table 불러오기
  return render(request, 'home.html', {'blogs' : blogs}
---
urls.py에 path 추가하기
```
