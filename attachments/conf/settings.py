from django.conf import settings


ALLOWED_TYPES = getattr(settings, 'ATTACHMENTS_ALLOWED_TYPES', '')
