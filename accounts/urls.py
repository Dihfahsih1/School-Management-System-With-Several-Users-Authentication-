from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetCompleteView, \
    PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView

urlpatterns = [

    # home
    url(r'^index/$', views.index, name='index'),
    # Register
    url(r'^register/$', views.register, name='register'),
    # login
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # logout
    url(r'^logout/$', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),

    url(r'^view_profile/$', views.view_profile, name="view_profile"),
    url(r'^view_profile/(?P<pk>\d+)/$', views.view_profile, name="view_profile_with_pk"),
    url(r'^edit_profile/$', views.edit_profile, name="edit_profile"),

    url(r'^change_password/$', views.change_password, name="change_password"),

    # /password_reset/
    url(r'^reset-password/$', PasswordResetView.as_view(template_name='accounts/reset_password.html'),
        {'email_template_name': 'accounts/reset_password_email'},
        name='reset-password'),
    # /password_reset_done/
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'),
        name='password_reset_done'),
    # /password_reset_confirm/
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/<token>/$',
        PasswordResetConfirmView.as_view(template_name='accounts/reset_password_confirm.html'),
        name='password_reset_confirm'),
    # /password_reset_complete/
    url(r'^reset-password/complete/$',
        PasswordResetCompleteView.as_view(template_name='accounts/reset_password_done.html'),
        name='password_reset_complete'),

    url(r'^user_rights$', views.user_rights, name="user_rights"),
    url(r'^edit_user_rights/(?P<pk>\d+)$', views.edit_user_rights, name="edit_user_rights"),

    url(r'^createclassinformation', views.createclassinformation, name="createclassinformation"),
    url(r'^editclassinformation/(?P<pk>\d+)', views.editclassinformation, name="editclassinformation"),
    url(r'^deleteclassinformation/(?P<pk>\d+)', views.deleteclassinformation, name="deleteclassinformation"),
    url(r'^viewclassinformation', views.viewclassinformation, name="viewclassinformation"),

    url(r'^createsectioninformation', views.createsectioninformation, name="createsectioninformation"),
    url(r'^editsectioninformation/(?P<pk>\d+)', views.editsectioninformation, name="editsectioninformation"),
    url(r'^deletesectioninformation/(?P<pk>\d+)', views.deletesectioninformation, name="deletesectioninformation"),
    url(r'^viewsectioninformation', views.viewsectioninformation, name="viewsectioninformation"),

    url(r'^createteacher', views.createteacher, name="createteacher"),
    url(r'^editteacher/(?P<pk>\d+)', views.editteacher, name="editteacher"),
    url(r'^deleteteacher/(?P<pk>\d+)', views.deleteteacher, name="deleteteacher"),
    url(r'^viewteachers', views.viewteachers, name="viewteachers"),

    url(r'^addsubject', views.addsubject, name="addsubject"),
    url(r'^editsubject/(?P<pk>\d+)', views.editsubject, name="editsubject"),
    url(r'^deletesubject/(?P<pk>\d+)', views.deletesubject, name="deletesubject"),
    url(r'^viewsubjects', views.viewsubjects, name="viewsubjects"),

    url(r'^addsyllabus', views.addsyllabus, name="addsyllabus"),
    url(r'^editsyllabus/(?P<pk>\d+)', views.editsyllabus, name="editsyllabus"),
    url(r'^deletesyllabus/(?P<pk>\d+)', views.deletesyllabus, name="deletesyllabus"),
    url(r'^viewsyllabus', views.viewsyllabus, name="viewsyllabus"),

    url(r'^addhumanresource', views.addhumanresource, name="addhumanresource"),
    url(r'^edithumanresource/(?P<pk>\d+)', views.edithumanresource, name="edithumanresource"),
    url(r'^deletehumanresource/(?P<pk>\d+)', views.deletehumanresource, name="deletehumanresource"),
    url(r'^viewhumanresource', views.viewhumanresource, name="viewhumanresource"),

    url(r'^addroutine', views.addroutine, name="addroutine"),
    url(r'^editroutine/(?P<pk>\d+)', views.editroutine, name="editroutine"),
    url(r'^deleteroutine/(?P<pk>\d+)', views.deleteroutine, name="deleteroutine"),
    url(r'^viewroutine', views.viewroutine, name="viewroutine"),

    url(r'^addassignment', views.addassignment, name="addassignment"),
    url(r'^editassignment/(?P<pk>\d+)', views.editassignment, name="editassignment"),
    url(r'^deleteassignment/(?P<pk>\d+)', views.deleteassignment, name="deleteassignment"),
    url(r'^viewassignment', views.viewassignment, name="viewassignment"),

    url(r'^addexamgrade', views.addexamgrade, name="addexamgrade"),
    url(r'^editexamgrade/(?P<pk>\d+)', views.editexamgrade, name="editexamgrade"),
    url(r'^deleteexamgrade/(?P<pk>\d+)', views.deleteexamgrade, name="deleteexamgrade"),
    url(r'^viewexamgrade', views.viewexamgrade, name="viewexamgrade"),

    url(r'^addexamterm', views.addexamterm, name="addexamterm"),
    url(r'^editexamterm/(?P<pk>\d+)', views.editexamterm, name="editexamterm"),
    url(r'^deleteexamterm/(?P<pk>\d+)', views.deleteexamterm, name="deleteexamterm"),
    url(r'^viewexamterm', views.viewexamterm, name="viewexamterm"),

    url(r'^addexamschedule', views.addexamschedule, name="addexamschedule"),
    url(r'^editexamschedule/(?P<pk>\d+)', views.editexamschedule, name="editexamschedule"),
    url(r'^deleteexamschedule/(?P<pk>\d+)', views.deleteexamschedule, name="deleteexamschedule"),
    url(r'^viewexamschedule', views.viewexamschedule, name="viewexamschedule"),

    url(r'^addexamsuggestion', views.addexamsuggestion, name="addexamsuggestion"),
    url(r'^editexamsuggestion/(?P<pk>\d+)', views.editexamsuggestion, name="editexamsuggestion"),
    url(r'^deleteexamsuggestion/(?P<pk>\d+)', views.deleteexamsuggestion, name="deleteexamsuggestion"),
    url(r'^viewexamsuggestion', views.viewexamsuggestion, name="viewexamsuggestion"),

    url(r'^addlibrarybook', views.addlibrarybook, name="addlibrarybook"),
    url(r'^editlibrarybook/(?P<pk>\d+)', views.editlibrarybook, name="editlibrarybook"),
    url(r'^deletelibrarybook/(?P<pk>\d+)', views.deletelibrarybook, name="deletelibrarybook"),
    url(r'^viewlibrarybook', views.viewlibrarybook, name="viewlibrarybook"),

    url(r'^addvehicle', views.addvehicle, name="addvehicle"),
    url(r'^editvehicle/(?P<pk>\d+)', views.editvehicle, name="editvehicle"),
    url(r'^deletevehicle/(?P<pk>\d+)', views.deletevehicle, name="deletevehicle"),
    url(r'^viewvehicle', views.viewvehicle, name="viewvehicle"),

    url(r'^addroute', views.addroute, name="addroute"),
    url(r'^editroute/(?P<pk>\d+)', views.editroute, name="editroute"),
    url(r'^deleteroute/(?P<pk>\d+)', views.deleteroute, name="deleteroute"),
    url(r'^viewroute', views.viewroute, name="viewroute"),

    url(r'^addhostel', views.addhostel, name="addhostel"),
    url(r'^edithostel/(?P<pk>\d+)', views.edithostel, name="edithostel"),
    url(r'^deletehostel/(?P<pk>\d+)', views.deletehostel, name="deletehostel"),
    url(r'^viewhostel', views.viewhostel, name="viewhostel"),

    url(r'^addroom', views.addroom, name="addroom"),
    url(r'^editroom/(?P<pk>\d+)', views.editroom, name="editroom"),
    url(r'^deleteroom/(?P<pk>\d+)', views.deleteroom, name="deleteroom"),
    url(r'^viewroom', views.viewroom, name="viewroom"),

    url(r'^addvisitor', views.addvisitor, name="addvisitor"),
    url(r'^editvisitor/(?P<pk>\d+)', views.editvisitor, name="editvisitor"),
    url(r'^deletevisitor/(?P<pk>\d+)', views.deletevisitor, name="deletevisitor"),
    url(r'^viewvisitor', views.viewvisitor, name="viewvisitor"),

    url(r'^addsalarygrade', views.addsalarygrade, name="addsalarygrade"),
    url(r'^editsalarygrade/(?P<pk>\d+)', views.editsalarygrade, name="editsalarygrade"),
    url(r'^deletesalarygrade/(?P<pk>\d+)', views.deletesalarygrade, name="deletesalarygrade"),
    url(r'^viewsalarygrade', views.viewsalarygrade, name="viewsalarygrade"),

    url(r'^adddiscount', views.adddiscount, name="adddiscount"),
    url(r'^editdiscount/(?P<pk>\d+)', views.editdiscount, name="editdiscount"),
    url(r'^deletediscount/(?P<pk>\d+)', views.deletediscount, name="deletediscount"),
    url(r'^viewdiscount', views.viewdiscount, name="viewdiscount"),

    url(r'^addfeetype', views.addfeetype, name="addfeetype"),
    url(r'^editfeetype/(?P<pk>\d+)', views.editfeetype, name="editfeetype"),
    url(r'^deletefeetype/(?P<pk>\d+)', views.deletefeetype, name="deletefeetype"),
    url(r'^viewfeetype', views.viewfeetype, name="viewfeetype"),

    url(r'^addfeecollection', views.addfeecollection, name="addfeecollection"),
    url(r'^editfeecollection/(?P<pk>\d+)', views.editfeecollection, name="editfeecollection"),
    url(r'^deletefeecollection/(?P<pk>\d+)', views.deletefeecollection, name="deletefeecollection"),
    url(r'^viewfeecollection', views.viewfeecollection, name="viewfeecollection"),

    url(r'^addincome', views.addincome, name="addincome"),
    url(r'^editincome/(?P<pk>\d+)', views.editincome, name="editincome"),
    url(r'^deleteincome/(?P<pk>\d+)', views.deleteincome, name="deleteincome"),
    url(r'^viewincome', views.viewincome, name="viewincome"),

    url(r'^addexpenditure', views.addexpenditure, name="addexpenditure"),
    url(r'^editexpenditure/(?P<pk>\d+)', views.editexpenditure, name="editexpenditure"),
    url(r'^deleteexpenditure/(?P<pk>\d+)', views.deleteexpenditure, name="deleteexpenditure"),
    url(r'^viewexpenditure', views.viewexpenditure, name="viewexpenditure"),

    url(r'^addevents', views.addevents, name="addevents"),
    url(r'^editevents/(?P<pk>\d+)', views.editevents, name="editevents"),
    url(r'^deleteevents/(?P<pk>\d+)', views.deleteevents, name="deleteevents"),
    url(r'^viewevents', views.viewevents, name="viewevents"),

    url(r'^addnotice', views.addnotice, name="addnotice"),
    url(r'^editnotice/(?P<pk>\d+)', views.editnotice, name="editnotice"),
    url(r'^deletenotice/(?P<pk>\d+)', views.deletenotice, name="deletenotice"),
    url(r'^viewnotice', views.viewnotice, name="viewnotice"),

    url(r'^addnews', views.addnews, name="addnews"),
    url(r'^editnews/(?P<pk>\d+)', views.editnews, name="editnews"),
    url(r'^deletenews/(?P<pk>\d+)', views.deletenews, name="deletenews"),
    url(r'^viewnews', views.viewnews, name="viewnews"),

    url(r'^addholiday', views.addholiday, name="addholiday"),
    url(r'^editholiday/(?P<pk>\d+)', views.editholiday, name="editholiday"),
    url(r'^deleteholiday/(?P<pk>\d+)', views.deleteholiday, name="deleteholiday"),
    url(r'^viewholidays', views.viewholidays, name="viewholidays"),

    url(r'^addprofile', views.addprofile, name="addprofile"),
    url(r'^editprofile/(?P<pk>\d+)', views.editprofile, name="editprofile"),
    url(r'^deleteprofile/(?P<pk>\d+)', views.deleteprofile, name="deleteprofile"),
    url(r'^viewprofile', views.viewprofile, name="viewprofile"),

    url(r'^addschool', views.addschool, name="addschool"),
    url(r'^editschool/(?P<pk>\d+)', views.editschool, name="editschool"),
    url(r'^deleteschool/(?P<pk>\d+)', views.deleteschool, name="deleteschool"),
    url(r'^viewschools', views.viewschools, name="viewschools"),

    url(r'^addstudent', views.addstudent, name="addstudent"),
    url(r'^editstudent/(?P<pk>\d+)', views.editstudent, name="editstudent"),
    url(r'^deletestudent/(?P<pk>\d+)', views.deletestudent, name="deletestudent"),
    url(r'^viewstudents', views.viewstudents, name="viewstudents"),

    url(r'^addguardian', views.addguardian, name="addguardian"),
    url(r'^editguardian/(?P<pk>\d+)', views.editguardian, name="editguardian"),
    url(r'^deleteguardian/(?P<pk>\d+)', views.deleteguardian, name="deleteguardian"),
    url(r'^viewguardians', views.viewguardians, name="viewguardians"),

    # The home page
    url(r'^home', views.home, name='home'),
]
