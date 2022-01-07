from django.db import models

class Dept(models.Model):
    did=models.IntegerField(primary_key=True)
    dep_name=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.dep_name}"


class Prof(models.Model):
    pid=models.ManyToManyField(Dept,related_name='dep_pro')
    prof_name=models.CharField(max_length=20)
    sub=models.CharField(max_length=20)



    def __str__(self):
        return f"{self.prof_name,self.sub}"

class Student(models.Model):
    sid=models.ForeignKey(Dept,related_name='dep_stu',on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    rollno=models.IntegerField()


