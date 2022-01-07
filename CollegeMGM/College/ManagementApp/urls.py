from django.urls import path
from .import views

urlpatterns=[
    path('dep/',views.department,name='add_dept'),
    path('stud/',views.student,name='add_stud'),
    path('pro/',views.prof,name='add_pro'),
    path('showstud/',views.showstud,name='show_stud'),
    path('showprof/',views.showprof,name='show_prof'),
    path('showdep/',views.showdep,name='show_dept'),
    path('delstud/<int:i>/',views.deletestud,name='del_stud'),
    path('delpro/<int:i>/',views.deleteprof,name='del_pro'),
    path('deldep/<int:i>/',views.deletedep,name='del_dep'),
    path('updstu/<int:i>/',views.updatestud,name='upd_stud'),
    path('updpro/<int:i>/',views.updatepro,name='upd_pro'),
    path('upddep/<int:i>/',views.updatedep,name='upd_dep'),

]