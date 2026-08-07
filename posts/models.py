from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

class Post(models.Model):
    POST_TYPES = [
        ('text', 'متن'),
        ('image', 'عکس'),
        ('video', 'ویدئو'),
    ]

    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="کاربر"
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        verbose_name="دسته‌بندی"
    )
    post_type = models.CharField(
        max_length=10, 
        choices=POST_TYPES,
        verbose_name="نوع پست"
    )
    title = models.CharField(
        max_length=200, 
        blank=True,
        verbose_name="عنوان"
    )
    content = models.TextField(
        blank=True,
        verbose_name="متن پست"
    )
    location_type = models.CharField(
        max_length=10,
        choices=[('شهر', 'شهر'), ('روستا', 'روستا')],
        blank=True,
        null=True,
        verbose_name="نوع مکان (فقط بنگاه)"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    likes_count = models.IntegerField(default=0, verbose_name="تعداد لایک")
    comments_count = models.IntegerField(default=0, verbose_name="تعداد کامنت")

    def __str__(self):
        return f"{self.get_post_type_display()} - {self.created_at.strftime('%Y/%m/%d')}"

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست‌ها"
        ordering = ['-created_at'] # جدیدترین اول


class Media(models.Model):
    MEDIA_TYPES = [
        ('image', 'تصویر'),
        ('video', 'ویدئو'),
    ]

    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='media',
        verbose_name="پست"
    )
    file = models.FileField(
        upload_to='posts/%Y/%m/%d/',
        verbose_name="فایل"
    )
    media_type = models.CharField(
        max_length=10, 
        choices=MEDIA_TYPES,
        verbose_name="نوع رسانه"
    )
    order = models.IntegerField(default=0, verbose_name="ترتیب نمایش")

    def __str__(self):
        return f"{self.media_type} - {self.post.id}"

    class Meta:
        verbose_name = "رسانه"
        verbose_name_plural = "رسانه‌ها"
        ordering = ['order']

