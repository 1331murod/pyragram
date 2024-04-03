from django.db import models





class Advertising(models.Model):
    title = models.TextField()
       
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "Reklamalar"
        verbose_name = "Reklama"


class Groups(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    groups = models.CharField(max_length = 400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.groups
    
    class Meta:
        verbose_name_plural = "Sms jo'natiladigan guruhlar"
        verbose_name = "Sms jo'natiladigan guruh"