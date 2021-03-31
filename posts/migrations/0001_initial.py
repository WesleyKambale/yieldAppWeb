# Generated by Django 3.1.7 on 2021-03-24 08:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('video', models.FileField(blank=True, null=True, upload_to='post_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mpeg', 'mp4', 'webm'], message='Videos have been limited to mp4,mpeg and webm only')])),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='post_images', validators=[django.core.validators.validate_image_file_extension])),
                ('likes', models.ManyToManyField(blank=True, related_name='Likes', to=settings.AUTH_USER_MODEL, verbose_name='Likes')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='postComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField(max_length=650)),
                ('comment_on', models.DateTimeField(auto_now_add=True)),
                ('comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
                ('comment_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('likes', models.ManyToManyField(blank=True, related_name='likecomment', to=settings.AUTH_USER_MODEL, verbose_name='Likes')),
            ],
        ),
        migrations.CreateModel(
            name='Commentreply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_body', models.TextField(max_length=200)),
                ('reply_on', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='likereply', to=settings.AUTH_USER_MODEL, verbose_name='Likes')),
                ('reply_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replier', to=settings.AUTH_USER_MODEL)),
                ('reply_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.postcomment')),
            ],
        ),
    ]
