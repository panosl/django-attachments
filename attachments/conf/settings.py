from django.conf import settings


ALLOWED_TYPES = getattr(settings, 'ATTACHMENTS_ALLOWED_TYPES', None)
MAX_QUOTA = getattr(settings, 'ATTACHMENTS_MAX_QUOTA', 0)
