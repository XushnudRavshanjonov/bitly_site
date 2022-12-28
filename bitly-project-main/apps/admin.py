from django.contrib.admin import register, ModelAdmin
from models import Message

@register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('subject', 'email', 'written_at', 'message_100')
    list_filter = ('subject', 'email', 'written_at')

    def message_100(self, obj):
        return obj.message[:100]