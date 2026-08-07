from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    مدل دسته‌بندی درختی برای تمام بخش‌های سایت
    """
    
    # ========== انتخاب‌های نوع دسته‌بندی ==========
    TYPE_CHOICES = [
        ('sight', 'مکان دیدنی'),
        ('neighborhood', 'محله'),
        ('village', 'روستا'),
        ('service', 'خدمات شهری'),
        ('service_sub', 'زیرمجموعه خدمات'),
    ]
    
    # ========== فیلدها ==========
    name = models.CharField(max_length=100, verbose_name="نام")
    slug = models.SlugField(max_length=120, unique=True, blank=True, verbose_name="اسلاگ")
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='children',
        verbose_name="دسته والد"
    )
    category_type = models.CharField(
        max_length=20, 
        choices=TYPE_CHOICES, 
        verbose_name="نوع دسته‌بندی"
    )
    order = models.IntegerField(default=0, verbose_name="ترتیب نمایش")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    
    # ========== متدها ==========
    def save(self, *args, **kwargs):
        """وقتی ذخیره میشه، اسلاگ رو از اسم تولید کن"""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        """نمایش اسم دسته در پنل ادمین"""
        return self.name
    
    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ['order', 'name']


