from django.db import models

class Final_User(models.Model):
    name = models.CharField(max_length=200, default=None, verbose_name=u'نام ورزشکار')
    seri1 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'سری اول')
    seri2 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'سری دوم')
    num11 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 11')
    num12 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 12')
    num13 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 13')
    num14 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 14')
    num15 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 15')
    num16 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 16')
    num17 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 17')
    num18 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 18')
    num19 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 19')
    num20 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 20')
    num21 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 21')
    num22 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 22')
    num23 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 23')
    num24 = models.IntegerField(default=None, null=True, blank=True, verbose_name=u'شماره 24')
    total = models.IntegerField(default=0, blank=True, verbose_name=u'مجموع')

    def calculate_total(self):
        num_fields = [
            self.seri1, self.seri2, 
            self.num11, self.num12, self.num13, self.num14, self.num15,
            self.num16, self.num17, self.num18, self.num19, self.num20,
            self.num21, self.num22, self.num23, self.num24
        ]
        return sum([field for field in num_fields if field is not None])

    def save(self, *args, **kwargs):
        self.total = self.calculate_total()
        super().save(*args, **kwargs)
