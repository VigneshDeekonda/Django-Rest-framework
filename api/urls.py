from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename='employee')

urlpatterns = [
    path('students/',views.studentsViews),
    path('students/<int:pk>/',views.studentDetailsViews),
    path('',include(router.urls)),
    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/',views.EmployeeDetails.as_view()),
    path('blogs/',views.blogView.as_view()),
    path('comments/',views.CommentView.as_view()),

    path('blogs/<int:pk>/',views.blogDetailsView.as_view()),
    path('comments/<int:pk>/',views.commentDetailsView.as_view()),
]