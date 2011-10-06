from attachments.conf.settings import MAX_QUOTA


def max_quota(request):
    return {
        'MAX_QUOTA': MAX_QUOTA
    }
