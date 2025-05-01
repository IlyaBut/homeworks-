from django.contrib import admin

from .models import Student, Teacher, SchoolStudentTeachers


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(SchoolStudentTeachers)
class SchoolStudentTeachersAdmin(admin.ModelAdmin):
    pass