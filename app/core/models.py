import os, uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

def pdf_file_path_generator(instance, filename):
    extension = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extension}'

    return os.path.join(f'uploads/core/pdf/', filename)

def audio_file_path_generator(instance, filename):
    extension = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extension}'

    return os.path.join(f'uploads/core/audio/', filename)

def video_file_path_generator(instance, filename):
    extension = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extension}'

    return os.path.join(f'uploads/core/video/', filename)

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('You must have an Email Address')

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_freelancer = False

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'


class Lesson(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=False, max_length=256) 
    pdf_pages = models.FileField(upload_to=pdf_file_path_generator, blank=False)
    audio_file = models.FileField(upload_to=audio_file_path_generator, blank=True)
    video_file = models.FileField(upload_to=video_file_path_generator, blank=True)
    # book = models.ForeignKey(Book, related_name='Lesson_Book', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} | {self.title}'


class Book(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=False, max_length=256) 
    lessons = models.ManyToManyField(Lesson, related_name='book', blank=True)
    # grade = models.ForeignKey(Grade, related_name='Book_Grade', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} | {self.title}'


class Grade(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=False, max_length=128) 
    books = models.ManyToManyField(Book, related_name='grade', blank=True)
    def __str__(self):
        return self.title





