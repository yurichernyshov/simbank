import uuid
from django.db import models
from decimal import Decimal


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    hold = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField()

    def __str__(self):
        return("Account, id: {}, name: {}, \nbalance: {}, \nhold: {}, \nstatus: {}".format(
            self.id, self.name, self.balance, self.hold, self.status))

    def add_to_balance(self, amount):
        self.balance += Decimal(float(amount))
        self.save()

    def subtract_from_balance(self, amount):
        v_amount = Decimal(float(amount))
        if (self.hold + v_amount <= self.balance):
            self.hold += v_amount
            self.save()
            pass
        else:
            return -1


