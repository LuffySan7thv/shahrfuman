from django.shortcuts import render
from categories.models import Category

def home(request):
    # دریافت دسته‌بندی‌های سطح اول (ریشه)
    root_categories = Category.objects.filter(parent__isnull=True, is_active=True)

    # دریافت دسته‌بندی خدمات شهری (با اسم دقیق)
    service_root = Category.objects.filter(name='خدمات شهری', is_active=True).first()
    
    # اگر خدمات شهری وجود داشت، زیرمجموعه‌هایش رو بگیر
    if service_root:
        services = service_root.children.filter(is_active=True)
    else:
        services = []

    # دریافت محلات و روستاها
    neighborhoods = Category.objects.filter(category_type='neighborhood', is_active=True)
    villages = Category.objects.filter(category_type='village', is_active=True)

    context = {
        'root_categories': root_categories,
        'services': services,
        'neighborhoods': neighborhoods,
        'villages': villages,
    }
    return render(request, 'home.html', context)
