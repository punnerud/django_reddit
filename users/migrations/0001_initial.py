# Generated by Django 4.0.4 on 2022-05-29 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RedditUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default=None, max_length=35, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=35, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('about_text', models.TextField(blank=True, default=None, max_length=500, null=True)),
                ('about_html', models.TextField(blank=True, default=None, null=True)),
                ('gravatar_hash', models.CharField(blank=True, default=None, max_length=32, null=True)),
                ('display_picture', models.BooleanField(null=True)),
                ('homepage', models.URLField(blank=True, default=None, null=True)),
                ('twitter', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('github', models.CharField(blank=True, default=None, max_length=39, null=True)),
                ('comment_karma', models.IntegerField(default=0)),
                ('link_karma', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
