from django.db import models
from tinymce.models import HTMLField

class Block(models.Model):
    page = models.ForeignKey('Page', related_name='block', verbose_name='медиа данные',
                                 on_delete=models.CASCADE, null=True)
    title = models.CharField(verbose_name='название статьи', max_length=1047)
    counter = models.IntegerField(blank=True, default=0, verbose_name='counter')
    order_number = models.IntegerField(default=1, verbose_name='порядковый номер')
    #text
    text = HTMLField(verbose_name='текст',null=True,blank=True)
    #audio
    audio = models.FileField(upload_to='upload/audio', null=True,blank=True)
    bitrate = models.IntegerField(default=0, verbose_name='битрейт бит / сек',null=True,blank=True)
    #video
    video = models.URLField(null=True,blank=True)
    video_sub = models.URLField(null=True,blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ('order_number',)
        verbose_name = 'Block'
        verbose_name_plural = 'Block'

class Page(models.Model):
    order_number = models.IntegerField(default=1, verbose_name='порядковый номер')
    title = models.CharField(verbose_name='название страницы', max_length=1047)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order_number',)
        verbose_name = 'Page'
        verbose_name_plural = 'Page'

