from celery.task import periodic_task
from datetime import timedelta
from .models import Account

@periodic_task(run_every=(timedelta(seconds=15)))
def refresh_holds():
    print("-----REFRESH HOLDS START----")
    accounts = Account.objects.filter(hold__gt=0)
    for account in accounts:
        print("refresh hold for \'{}\'".format(account.name))
        account.balance -= account.hold
        account.hold = 0
        account.save()
    print("-----REFRESH HOLDS COMPLETE----")
