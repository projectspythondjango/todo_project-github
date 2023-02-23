from django.urls import path
from .import views
app_name='todo_app'
urlpatterns=[
    path('',views.add1,name='add1'),
    # path('details',views.details,name='details'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklist.as_view(),name='cbvhome'),
    path('detailpage/<int:pk>/',views.Taskdetail.as_view(),name='detailpage'),
    path('updatepage/<int:pk>/',views.Taskupdate.as_view(),name='updatepage'),
    path('deletepage/<int:pk>/',views.Taskdelete.as_view(),name='deletepage'),
    ]
