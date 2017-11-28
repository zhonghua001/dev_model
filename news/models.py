from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your models here.

class Column(models.Model):
    name = models.CharField('Column Name',max_length=256)
    slug = models.CharField('Column wwww',max_length=256)
    intro = models.TextField('Column Introduction',default='')

    def get_absolute_url(self):
        return reverse('column',args=(self.slug,))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Column'
        verbose_name_plural = 'Column'
        ordering = ['name']

class Article(models.Model):
    column = models.ManyToManyField(Column,verbose_name='Column\'s Article')
    title = models.CharField('title',max_length=200)
    slug = models.CharField('Website',max_length=100,db_index=True)
    author = models.ForeignKey(User,verbose_name='Author',null=True)
    # content = models.TextField(default='',blank=True)
    content = UEditorField('content',height=300,width=1000,
                           default=u'',blank=True,imagePath="uploads/images/",
                           toolbars='besttome',filePath='uploads/files/')
    published = models.BooleanField('Published ',default=True)
    pub_date = models.DateTimeField('Publish date',auto_now_add=True,editable=True)
    update_time = models.DateTimeField('Update date',auto_now=True,null=True)


    def get_absolute_url(self):
        return reverse('news',args=(self.slug,))

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = 'Course'



