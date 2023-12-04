from django.db import models

class Test(models.Model):
    savol = models.CharField(max_length=500,null=False,blank=False)
    variantA = models.CharField(max_length=250,null=False)
    variantB = models.CharField(max_length=250,null=False)
    variantC = models.CharField(max_length=250,null=False)
    variantD = models.CharField(max_length=250,null=False)

    def __str__(self) -> str:
        return self.savol


