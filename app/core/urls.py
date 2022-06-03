from django.urls import path, include

from rest_framework.routers import DefaultRouter

from core import views


router = DefaultRouter()

router.register('grades', views.GradeReadOnlyViewSet)
router.register('books', views.BookReadOnlyViewSet)
router.register('lessons', views.LessonReadOnlyViewSet)

app_name = 'core'

urlpatterns = [
    path('', include(router.urls))
]
