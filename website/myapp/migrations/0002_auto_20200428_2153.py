# Generated by Django 2.2 on 2020-04-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionForm',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
