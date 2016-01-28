# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('started_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'quizzes',
            },
        ),
        migrations.CreateModel(
            name='QuizAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField()),
                ('correct', models.BooleanField()),
            ],
            options={
                'db_table': 'answers',
            },
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.ForeignKey(to='lyftloot.QuizAnswer')),
                ('question', models.ForeignKey(to='lyftloot.QuizQuestion')),
                ('quiz', models.ForeignKey(to='lyftloot.Quiz')),
            ],
            options={
                'db_table': 'user_answers',
            },
        ),
        migrations.AddField(
            model_name='quizanswer',
            name='question',
            field=models.ForeignKey(to='lyftloot.QuizQuestion'),
        ),
        migrations.AlterUniqueTogether(
            name='useranswer',
            unique_together=set([('quiz', 'question')]),
        ),
    ]
