from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from fitnessapp import views

urlpatterns = [
    path('', views.login, name='login'),
    path('Forgot_password',views.Forgot_password, name='Forgot_password'),
    path('index/', views.index, name='index'),
    path('User_profile/',views.User_profile,name='User_profile'),
    path('User_edit_profile/',views.User_edit_profile,name='User_edit_profile'),
    path('about/', views.about, name='about'),
    path('classes/', views.classes, name='classes'),
    path('train/', views.train, name='train'),
    path('selecttrainer/', views.selecttrainer, name='selecttrainer'),
    path('shedule/', views.shedule, name='shedule'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'), 
    path('userpaymentpage/', views.userpaymentpage, name='userpaymentpage'),
    path('online_training/', views.online_training, name='online_training'),
    path('offline_training/', views.offline_training, name='offline_training'),
    path('onlin/', views.onlin, name='onlin'),
    path('onedit/<int:i_id>', views.onedit, name='onedit'),
    path('onlineedit/<int:oned_id>', views.onlineedit, name='onlineedit'),
    path('offlin/', views.offlin, name='offlin'),
    path('Usert_profile/',views.Usert_profile,name='Usert_profile'),
    path('Usert_edit_profile/',views.Usert_edit_profile,name='Usert_edit_profile'),
    path('offedit/<int:i_id>', views.offedit, name='offedit'),
    path('offlineedit/<int:offd_id>', views.offlineedit, name='offlineedit'),
    path('staffd/', views.staffd, name='staffd'),
    path('maint/', views.maint, name='maint'),
    path('admhome/', views.admhome, name='admhome'),
    path('admreg/', views.admreg, name='admreg'),
    path('admregedit/<int:i_id>',views.admregedit, name='admregedit'),
    path('admregistration/<int:reg_id>', views.admregistration, name='admregistration'),
    path('admintimetable/', views.admintimetable, name='admintimetable'),
    path('admin_view_timetable/', views.admin_view_timetable, name='admin_view_timetable'),
    path('admin_edit_timetable/<int:i_id>', views.admin_edit_timetable, name='admin_edit_timetable'),
    path('admin_editpage/<int:timet_id>', views.admin_editpage, name='admin_editpage'),
    path('delete_batch/<int:p_id>', views.delete_batch, name='delete_batch'),
    path('admin_userpayment/', views.admin_userpayment, name='admin_userpayment'),
    path('admin_payment/', views.admin_payment, name='admin_payment'),
    path('admin_pay_page/', views.admin_pay_page, name='admin_pay_page'),
    path('Trainee_logout/', views.Trainee_logout, name='Trainee_logout'),
    path('Trainer_logout/', views.Trainer_logout, name='Trainer_logout'),
    path('SuperAdmin_logout/', views.SuperAdmin_logout, name='SuperAdmin_logout'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

