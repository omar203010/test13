from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح التشفير - لا تستخدمه كما هو في الإنتاج
SECRET_KEY = 'django-insecure-oyts=q0c78p+3f6h8ki(dz(z^%q5c+8%-pq15u9v+14@_k)m_9'

# وضع التصحيح - فعّل فقط أثناء التطوير
DEBUG = True

ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'coreuploads',  # تطبيقك الأساسي
    'cloudinary',
    'cloudinary_storage',
]

# الميدل وير
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ملف روابط المشروع
ROOT_URLCONF = 'test13.urls'

# إعداد القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# إعداد WSGI
WSGI_APPLICATION = 'test13.wsgi.application'

# قاعدة البيانات SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# تحقق كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# الملفات الثابتة (CSS، JS، إلخ)
STATIC_URL = 'static/'

# Cloudinary لتخزين الوسائط
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dodhp4xho',
    'API_KEY': '417429323829795',
    'API_SECRET': 'c_jU4PDFK18grf4Zq0eo0sXn8H0',
}

# تهيئة Cloudinary بشكل صريح لتجنب الأخطاء
cloudinary.config(
    cloud_name='dodhp4xho',
    api_key='417429323829795',
    api_secret='c_jU4PDFK18grf4Zq0eo0sXn8H0'
)

# نوع معرف القاعدة الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
