from django.db import models

class Inspection(models.Model):
    PLACE = [
        ('管理棟ＣＰＵ室', '管理棟ＣＰＵ室'),
        ('工場棟2F 外注ｴﾘｱ', '工場棟2F 外注ｴﾘｱ'),
        ('倉庫７', '倉庫７'),
        ('管理棟2F EPS1', '管理棟2F EPS1'),
        ('鍵返却', '鍵返却'),
    ]

    USERS = [
        ('疋田','疋田'),
        ('若狭','若狭'),
        ('⻄田（紀）','⻄田（紀）'),
        ('伊藤','伊藤'),
        ('上本','上本'),
        ('遠藤','遠藤'),
        ('⻄田（⼤）','⻄田（⼤）'),
    ]

    itemslist = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    count = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=50, choices=PLACE, null=True)
    checkTarget = models.CharField(max_length=50, blank=True,null=True)
    checkDetail = models.CharField(max_length=50, blank=True,null=True)
    manufacturerModel = models.TextField(max_length=100, blank=True,null=True)
    method = models.CharField(max_length=50,default='', blank=True,null=True)
    normalState = models.TextField(max_length=255,blank=True)
    username = models.CharField(max_length=60, choices=USERS, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.itemslist)

    class Meta:
        ordering = ['itemslist']
    

# Create your models here.
