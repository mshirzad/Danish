# Generated by Django 2.1.15 on 2022-06-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220603_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='lessons',
            field=models.ManyToManyField(blank=True, related_name='book', to='core.Lesson'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='grade', to='core.Book'),
        ),
    ]
