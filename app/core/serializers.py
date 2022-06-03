from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from core.models import Grade, Book, Lesson

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('title', 'pdf_pages', 'audio_file', 'video_file',)

class BookSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(required=True, many=True)
    class Meta:
        model = Book
        fields = ('id', 'title', 'grade', 'lessons',)

class GradeSerializer(serializers.ModelSerializer):
    books = BookSerializer(required=True, many=True)
    class Meta:
        model = Grade
        fields = ('id', 'title', 'books',)

