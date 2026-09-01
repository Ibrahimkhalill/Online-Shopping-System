from django.urls import path
from django.contrib.auth import views as auth_views
from.import views

urlpatterns =[
	path('register/',views.register,name="register"),
	
	path('login/',views.login,name="login"),
	path('logout/',views.logoutUser,name="logout"),
	path('reset_password/',auth_views.PasswordResetView.as_view(template_name='user/reset_password.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='user/reset_password_sent.html'),name='password_reset_done'),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
	path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),
]