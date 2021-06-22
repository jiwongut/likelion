# 장고와 데이터베이스
------------
## ORM (Object Relation Mapping)
------------
> ORM이란? 객체(Object)와 관계형 데이터베이스(Relation)를 sql 쿼리를 사용하지 않고 연결(Mapping)해주는 것을 뜻한다. 
> 장고(django)의 ORM을 이용하여 데이터베이스에서 데이터를 생성(Create)하고, 읽고(Read), 갱신하고(Update), 삭제(Delete)할 수 있다.  

## CRUD
### Read
```
앱 내에서 template 폴더 생성 후 views.py 파일을 생성한다.  

--- in views.py
from .models import Blog  

def home(request):
  blogs = Blog.objects.all() // Blog 내 모든 table 불러오기
  return render(request, 'home.html', {'blogs' : blogs}
---
urls.py에 path 추가하기
home.html에서 key값 추가하기
---
{% for blog in blogs %}
  {{blogs}}
{% end for %}
```
### Create
```
new() : new.html을 보여줌  
create() : 데이터베이스에 저장  

--- in views.py
def new(request):
return render(request,'new.html')
  
def create(request):
new_blog = Blog() // 새로운 object 생성
new_blog.title = request.POST['title']
new_blog.writer = request.POST['writer']

```

#### *** get() : 데이터를 얻기 위한 요청, url에 데이터가 보임  
#### *** post() : 데이터를 생성하기 위한 요청, url에 데이터가 안보임, csrf 공격에 방지  

### Update
```
edit() : edit.html을 보여줌
update() : 데이터베이스에 적용
*수정할 데이터의 id값을 받아야 함!  
---
def update(request, id):
update_blog = Blog.objects.get(id= id)
update_blog.title = request.POST['title']
new_blog.writer = request.POST['writer']

update_blog.save() // 저장 꼭 해주기
```
### Delete
```
def delete(request,id):
delete_blog = Blog.objects.get(id= id)
delete_blog.delete() // 삭제 메소드
return redirect('home')
```
