from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # ← هذا السطر مهم

class UserSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    title = models.CharField(max_length=100, verbose_name="العنوان")
    description = models.TextField(verbose_name="الوصف")
    image = CloudinaryField('الصورة')  # ← استخدام CloudinaryField بدلاً من ImageField
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مشاركة المستخدم"
        verbose_name_plural = "مشاركات المستخدمين"
