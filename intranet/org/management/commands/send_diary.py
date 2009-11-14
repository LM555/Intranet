#!/usr/bin/env python

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        import datetime
        import sys
        
        from django.db.models import Q
        from django.core.mail import send_mail
        
        from intranet.org.models import Scratchpad, Diary, Lend
        
        now = datetime.date.today() - datetime.timedelta(1)
        result = ['Kiberpipa, dnevno porocilo: %d-%d-%d\n\n' % (now.year, now.month, now.day)]
        result.append('Dnevniki:\n\n')

        diarys = Diary.objects.filter(pub_date__year=now.year, pub_date__month=now.month, pub_date__day=now.day)
        if not diarys:
            sys.exit(0)

        for diary in diarys:
            result.append('[ %s - %s - %s - %s ]\n --\n %s \n--\n %s\n\n' % (
                diary.date, diary.author, diary.task.__unicode__(), diary.length, diary.log_formal, diary.log_informal))

        result.append('=== Kracarka:\n\n%s\n\n' % Scratchpad.objects.all()[0].content)
        result.append('=== Preteceni reverzi\n')

        for lend in Lend.objects.filter(returned=False):
            result.append('%s - %s posodil %s (%s dni)\n' % (lend.what, lend.to_who, lend.from_who, lend.days_due().days))

        result = ''.join(result)
        send_mail('<sth smart s> %d-%d-%d' % (now.year, now.month, now.day), result, 'intranet@kiberpipa.org', ['pipa-org@list.kiss.si'])

