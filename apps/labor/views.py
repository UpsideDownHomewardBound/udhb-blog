from apps.labor.models import LaborAnnouncement


def all_announcements(request):
    announcements = LaborAnnouncement.objects.all()

    return render('labor_announcements.html',
        {'announcements': announcements}
    )