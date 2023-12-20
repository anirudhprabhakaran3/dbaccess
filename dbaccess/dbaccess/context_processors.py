from django.conf import settings


def version_information(request):
    return {
        "VERSION": settings.VERSION,
        "RELEASE_DATE": settings.RELEASE_DATE
    }
