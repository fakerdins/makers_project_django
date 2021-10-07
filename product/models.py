from django.db.models.deletion import CASCADE
import product
from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField
from django.contrib.auth import get_user_model


User = get_user_model()


class CreatedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    """ создание абстрактной модели для добавления поля создания продукта fields import StatusField
    нужен для  сокращения кода и его расширяемость"""
    class Meta:
        abstract = True

class Product(CreatedModel):
    STATUS = Choices("Available", "Not available")
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', null=True, blank=True)
    status = StatusField()
    description = models.TextField()

    # hello = models.Manager()

    class Meta:
        ordering = ['title', 'price']
    def __str__(self):
        return self.title

class ProductReview(CreatedModel):
    

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='reviews',
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews', null=True,
    )
    text = models.TextField()
    rating = models.PositiveIntegerField(default=1)

# product = ProductReview(product='edited post')