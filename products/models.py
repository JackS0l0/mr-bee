from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
class Products(models.Model):
    name=models.CharField('Məhsulun adı',max_length=200,unique=True)
    price=models.DecimalField('Qiyməti', max_digits=10, decimal_places=2,default=0)
    img=models.URLField('Görüntüsü',default='')
    date=models.DateTimeField('Tarix',default=timezone.now)
    desc=RichTextField('Məumat',default='')
    def __str__(self):
        return f'{self.name} {self.price}'
    class Meta:
        verbose_name='Məhsul'
        verbose_name_plural='Məhsullar'