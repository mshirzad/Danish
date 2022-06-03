from django.db.models.query_utils import Q

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from core.models import Grade, Book, Lesson
from core.serializers import GradeSerializer, BookSerializer, LessonSerializer

# mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet

class GradeReadOnlyViewSet(ReadOnlyModelViewSet):

    serializer_class = GradeSerializer
    queryset = Grade.objects.all()


class BookReadOnlyViewSet(ReadOnlyModelViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all()

class LessonReadOnlyViewSet(ReadOnlyModelViewSet):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        keyword = self.request.query_params.get('keyword')

        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | 
                Q(book__title__icontains=keyword) 
            )

        return queryset
