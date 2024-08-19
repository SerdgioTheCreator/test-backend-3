from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from courses.models import Group
from users.models import Subscription


@receiver(post_save, sender=Subscription)
def post_save_subscription(sender, instance: Subscription, created, **kwargs):
    """
    Распределение нового студента в группу курса.

    """

    if created:
        user = instance.user
        course = instance.course

        group = Group.objects.filter(
            course=course
        ).annotate(
            students_count=Count('user')
        ).order_by(
            'students_count'
        ).first()

        if group:
            user.group = group
            user.save()

        # TODO
