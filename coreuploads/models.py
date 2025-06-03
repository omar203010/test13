from django.db import models
from django.contrib.auth.models import User

class UserSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    title = models.CharField(max_length=100, verbose_name="العنوان")
    description = models.TextField(verbose_name="الوصف")
    image = models.ImageField(upload_to='uploads/', verbose_name="الصورة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مشاركة المستخدم"
        verbose_name_plural = "مشاركات المستخدمين"
