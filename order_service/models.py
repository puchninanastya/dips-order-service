from django.db import models
from django.utils.timezone import now

class Order(models.Model):
    user_id = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="By user")
    order_date = models.DateField(
        blank=True,
        null=False,
        default=now,
        verbose_name="Order date")
    amount = models.PositiveIntegerField()
    is_paid = models.BooleanField(
        blank=True,
        null=False,
        default=False,
        verbose_name="Has been paid")

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

'''
    def __str__(self):
        return "{}".format(self.pk)
'''
