from django.shortcuts import render

def welcome(request): #welcome이라는 함수 호출시 welcome.html 표시
	return render(request, "welcome.html")

def hello(request):
	userName = request.GET['name'] #welcome의 input박스에 있는 값 호출
	return render(request, 'hello.html', {'userName' : userName})