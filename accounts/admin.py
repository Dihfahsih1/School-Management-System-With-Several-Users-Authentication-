from django.contrib import admin
from accounts.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.site_header = 'MSMS Administration'


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(AccountRight)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Guardian)
admin.site.register(ClassInformation)
admin.site.register(SectionInformation)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Syllabus)
admin.site.register(HumanResource)
admin.site.register(Routine)
admin.site.register(Assignment)
admin.site.register(ExamGrade)
admin.site.register(ExamTerm)
admin.site.register(ExamSchedule)
admin.site.register(ExamSuggestion)
admin.site.register(Library)
admin.site.register(Transport)
admin.site.register(Route)
admin.site.register(Hostel)
admin.site.register(HostelRoom)
