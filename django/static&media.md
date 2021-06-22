## static & media  

 # static
 개발자가 개발할 때 미리 넣어둔 파일(img, js, css) 
  
 1.정적파일 : 미리 서버에 저장되어 있는 파일, 서버에 저장된 그대로 서비스해줌  
 2.동적파일 : 서버의 데이터들이 어느 정도 가공된 다음 보여지는 파일(방법에 따라 달라짐)
  ``` 
  #앱 내에서 static 폴더 생성
  #settings.py에서 static_url 코드 작성 후 terminal에서 "collecstatic" 입력
  html 파일 <body> 에 <% load static %>
  <img src="{% static '파일명' %}" alt=" " weight,height 조절가능 />
```
