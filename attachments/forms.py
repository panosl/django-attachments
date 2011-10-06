from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from attachments.models import Attachment
from attachments.conf import settings


class AttachmentForm(forms.ModelForm):
    attachment_file = forms.FileField(label=_('Upload attachment'))

    def clean(self):
        data = self.cleaned_data.get('attachment_file')
        try:
            allowed_types = tuple(settings.ALLOWED_TYPES.split(' '))
            if not data.name.lower().endswith(allowed_types):
                raise forms.ValidationError(_('Filetype not allowed.'))
        except AttributeError:
            pass
        if settings.MAX_QUOTA and data._size > settings.MAX_QUOTA:
            raise forms.ValidationError(_('You are exceeding your allowed space.'))
        return self.cleaned_data
            
    class Meta:
        model = Attachment
        fields = ('attachment_file',)

    def save(self, request, obj, *args, **kwargs):
        self.instance.creator = request.user
        self.instance.content_type = ContentType.objects.get_for_model(obj)
        self.instance.object_id = obj.id
        super(AttachmentForm, self).save(*args, **kwargs)
