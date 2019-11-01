from django.db import models

# Create your models here.
class Grades(models.Model):
    grade_name = models.CharField(max_length=20)
    grade_crate_data = models.DateTimeField()
    grade_gril_num   = models.IntegerField()
    grade_boy_num   = models.IntegerField()
    grade_isDelete   = models.BooleanField(default=False)

    def __str__(self):
        return "%s-%d-%d" %(self.grade_name,self.grade_gril_num,self.grade_boy_num)


class Students(models.Model):
    student_name = models.CharField(max_length=20)
    student_gender = models.BooleanField(default=True)
    student_age   = models.IntegerField()
    student_contend   = models.CharField(max_length=20)
    student_isDelete   = models.BooleanField(default=False)

    #关联外键  
    #django 2.x 版本中必须添加on_delete=models.CASCADE
    
    student_grade1 = models.ForeignKey("Grades",on_delete=models.CASCADE,default = '')
    """def __str__(self):
        return "%s-%d-%d" %(self.grade_name,self.grade_gril_num,self.grade_boy_num)"""
