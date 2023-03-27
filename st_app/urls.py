from django.urls import path

from st_app import views

urlpatterns = [
    path("",views.index,name="index"),
    path("index1", views.index1, name="index1"),
    path("loginpage", views.loginpage, name="loginpage"),
    path("base", views.base, name="base"),
    path("studentbase", views.studentbase, name="studentbase"),

    path("students_data", views.students_data, name="students_data"),
    path("students_data_view", views.students_data_view, name="students_data_view"),
    path("complaint", views.complaint, name="complaint"),
    path("view_complaint", views.view_complaint, name="view_complaint"),
    path("view", views.view, name="view"),
    path("reply_complaint/<int:id>/", views.reply_complaint, name="reply_complaint"),
    path("delete_data/<int:id>/", views.delete_data, name="delete_data"),
    path("delete_complaint/<int:id>/", views.delete_complaint, name="delete_complaint"),
    path("notification", views.notification, name="notification"),
    path("view_notification", views.view_notification, name="view_notification"),
    path("student_notification", views.student_notification, name="student_notification"),
    path("reply_notification/<int:id>/", views.reply_notification, name="reply_notification"),
    path("student_registration", views.student_registration, name="student_registration"),
    path("logout_view", views.logout_view, name="logout_view"),

]