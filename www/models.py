from django.db import models

from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()

class Article(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'draft', "Brouillon"
        PUBLISHED = 'published', "Publié"
        CLOSED = 'closed', "Fermé"
        
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    
    title = models.CharField(max_length=255)
    content = models.TextField("Contenu", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(
        verbose_name="Date de publication",
        default=timezone.now, blank=True
    )
    
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
    )
    
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
    )
    
    thumb = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    cover = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['title']
        
        
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        
