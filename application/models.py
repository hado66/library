from django.db import models

# Create your models here.
class Test(models.Model):
    """
    测试实体类
    保证数据库连接正常
    """
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'test'