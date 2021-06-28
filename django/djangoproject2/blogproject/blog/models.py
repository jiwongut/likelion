from django.db import models

class Blog(models.Model):#모듈 안 Model class를 상속
    title = models.CharField(max_length=200)#제한이 있는 문자열
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()#제한이 없는 문자열
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
