from django.db import models
import uuid

# Create your models here.
class MucnhyTest(models.Model):
    munchy = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    
    def __str__(self):
        return self.munchy