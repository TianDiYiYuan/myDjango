#coding=UTF-8
from django.contrib import admin

# Register your models here.
from .models import Grades,Students
#自定也管理页面

class StudentsAdd(admin.TabularInline):#StackedInline
    model = Students
    extra = 2#两个学生



class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsAdd]
    #列表页属性
    list_display = ['pk','grade_name','grade_crate_data','grade_gril_num','grade_boy_num','grade_isDelete']
    list_filter  = ['grade_name']
    search_fields = ['grade_name']
    list_per_page = 5
    
    #添加、修改页属性
    #fields = ['grade_gril_num','grade_boy_num','grade_isDelete','grade_name','grade_crate_data']
    fieldsets = [
        ("num",{"fields":['grade_gril_num','grade_boy_num']}),
         ("base",{"fields":['grade_isDelete','grade_name','grade_crate_data']}),
    ]
from .models import Grades,Students
#自定也管理页面

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.student_gender:
            return "男"
        else:
            return "女"
    #设置页面列的名称
    gender.short_description = "性别"
    #列表页属性
    list_display = ['pk','student_name',gender,'student_age','student_contend','student_isDelete']
    list_per_page = 10
    

    actions_on_bottom = True
    actions_on_top    = True
    """list_filter  = ['grade_name']
    search_fields = ['grade_name']
    
    
    #添加、修改页属性
    #fields = ['grade_gril_num','grade_boy_num','grade_isDelete','grade_name','grade_crate_data']
    fieldsets = [
        ("num",{"fields":['grade_gril_num','grade_boy_num']}),
         ("base",{"fields":['grade_isDelete','grade_name','grade_crate_data']}),
    ]"""

#注册
admin.site.register(Grades, GradesAdmin)

#admin.site.register(Students,StudentsAdmin)