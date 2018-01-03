from django.db import models
from django.utils.timezone import now

class Order(models.Model):
    user = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="By user")
    order_date = models.DateTimeField(
        blank=True,
        null=False,
        default=now,
        verbose_name="Order datetime")
    amount = models.PositiveIntegerField()
    is_paid = models.BooleanField(
        blank=True,
        null=False,
        default=False,
        verbose_name="Has been paid")

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return "id {}".format(self.pk)

class OrderCourse(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='courses',
        on_delete=models.CASCADE)
    course_id = models.IntegerField(
        blank=False,
        null=False)

    class Meta:
        verbose_name = "Order course"
        verbose_name_plural = "Order courses"

    def __str__(self):
        return 'order {} - course {}'.format(self.order.id, self.course_id)
