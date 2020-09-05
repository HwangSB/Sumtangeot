from django.db import models

# Create your models here.

class Friend(models.Model):
    # 사용 필드: 분류군, 등급, 국명, 학명, 이미지

    ''' 분류군 목록 '''
    GROUP_CHOICES = (
        ("포유류", "포유류"),
        ("조류", "조류"),
        ("양서파충류", "양서파충류"),
        ("어류", "어류"),
        ("곤충류", "곤충류"),
        ("무척추동물", "무척추동물"),
    )

    ''' 등급 목록 '''
    LEVEL_CHOICES = (
        ("1급", "1급"),
        ("2급", "2급"),
        ("3급", "3급"),
    )

    group = models.CharField(choices=GROUP_CHOICES, max_length=20)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=10)
    kor_name = models.CharField(max_length=30)
    scientific_name = models.CharField(max_length=100)
    image = models.ImageField(default='static/images/default_image.png')

    def __str__(self):
        return self.kor_name