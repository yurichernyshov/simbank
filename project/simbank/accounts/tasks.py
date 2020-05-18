from celery.task import periodic_task
from datetime import timedelta
from .models import Account

@periodic_task(run_every=(timedelta(minutes=10)))
def refresh_holds():
    accounts = Account.objects.filter(hold__gt=0)
    for account in accounts:
        account.balance -= account.hold
        account.hold = 0
        account.save()
