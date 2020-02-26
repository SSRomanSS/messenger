from django.db import models


class Message(models.Model):
    email = models.EmailField()
    message = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'email: "{self.email}". message_text: "{self.message}". message_id={self.pk}'

    class Meta(object):
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-time_create']
