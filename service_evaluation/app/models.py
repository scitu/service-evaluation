from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Evaluation(models.Model):
    SCORE_ONE = 1
    SCORE_TWO = 2
    SCORE_THREE = 3
    SCORE_FOUR = 4
    SCORE_FIVE = 5
    EVAL_CHOICES = (
        (SCORE_FIVE, 'มากที่สุด'),
        (SCORE_FOUR, 'มาก'),
        (SCORE_THREE, 'ปานกลาง'),
        (SCORE_TWO, 'น้อย'),
        (SCORE_ONE, 'น้อยที่สุด'),
    )

    PERFORMANCE_LABEL = 'ความรวดเร็วในการเปิดเว็บแอพพลิเคชั่น'
    EASE_OF_USE_LABEL = 'ความสะดวกและการใช้งานง่ายในการค้นหาข้อมูล'
    CORRECTNESS_LABEL = 'ความถูกต้องของข้อมูล'
    COMMENT_LABEL = 'ความคิดเห็นเพิ่มเติม'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=64)
    created_date = models.DateTimeField(auto_now_add=True)
    performance_score = models.IntegerField(choices=EVAL_CHOICES)
    ease_of_use_score = models.IntegerField(choices=EVAL_CHOICES)
    correctness_score = models.IntegerField(choices=EVAL_CHOICES)
    comment = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'service')
