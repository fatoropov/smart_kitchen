from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from products.models import Product
from dinnerware.models import Dinnerware


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    dorm_number = models.CharField(max_length=3,
                                   blank=True)
    room_number = models.CharField(max_length=4,
                                   blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'


class UserProducts(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='product_user_id',
                                on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,
                                   related_name='product_id',
                                   on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


class UserDinnerware(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='dinnerware_user_id',
                                on_delete=models.CASCADE)
    dinnerware_id = models.ForeignKey(Dinnerware,
                                      related_name='dinnerware_id',
                                      on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


class Contact(models.Model):
    user_from = models.ForeignKey('auth.User',
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User',
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'


# Add following field to User dynamically
user_model = get_user_model()
user_model.add_to_class('following',
                        models.ManyToManyField('self',
                                               through=Contact,
                                               related_name='followers',
                                               symmetrical=False))
