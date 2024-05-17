from django.db import models
from django.utils import timezone
from django.utils.text import slugify

category_type = (
    ('FullTime','Full Time'),
    ('PartTime','Part Time'),
    ('Remote','Remote'),
    ('Freelance','Freelance'),
    
)
experiences = (
    (1,'1-2 Years'),
    (2,'2-3 Years'),
    (3,'3-6 Years'),
    (4,'6-more..'),
    
)



class Jobs(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.TextField(max_length=500)
    description = models.TextField(max_length=50000)
    jobs_type = models.CharField(max_length=30,choices=category_type)
    experience = models.IntegerField(choices=experiences)
    date = models.DateTimeField(default=timezone.now)
    location = models.TextField(max_length=100)
    salary = models.CharField(max_length=100)
    category = models.ForeignKey('Category', related_name='jobs_Category', on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey('Company', related_name='jobs_company', on_delete=models.CASCADE, null=True, blank=True)
    logo = models.ImageField(upload_to ='Jobs_logo', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Jobs, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    logo = models.ImageField(upload_to ='Category_logo', null=True, blank=True)

    def __str__(self):
        return self.name



class Company(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.TextField(max_length=500)
    email = models.TextField(max_length=500)
    web = models.TextField(max_length=500)
    logo = models.ImageField(upload_to ='Company_logo', null=True, blank=True)

    def __str__(self):
        return self.name

