# Generated by Django 2.0.4 on 2018-08-27 08:02

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1047, verbose_name='название статьи')),
                ('counter', models.IntegerField(blank=True, default=0, verbose_name='counter')),
                ('order_number', models.IntegerField(default=1, verbose_name='порядковый номер')),
                ('text', tinymce.models.HTMLField(blank=True, null=True, verbose_name='текст')),
                ('audio', models.FileField(blank=True, null=True, upload_to='upload/audio')),
                ('bitrate', models.IntegerField(blank=True, default=0, null=True, verbose_name='битрейт бит / сек')),
                ('video', models.URLField(blank=True, null=True)),
                ('video_sub', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Block',
                'ordering': ('order_number',),
                'verbose_name': 'Block',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(default=1, verbose_name='порядковый номер')),
                ('title', models.CharField(max_length=1047, verbose_name='название страницы')),
            ],
            options={
                'verbose_name_plural': 'Page',
                'ordering': ('order_number',),
                'verbose_name': 'Page',
            },
        ),
        migrations.AddField(
            model_name='block',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='block', to='mediapages.Page', verbose_name='медиа данные'),
        ),
    ]