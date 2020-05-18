from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from accounts.models import Account
from accounts.serializers import AccountSerializer
from decimal import Decimal

def SimbankAPIResponse(status, result, addition, description):
    return {"status": status,
            "result": result,
            "addition": addition,
            "description": description}

class PingView(APIView):
    def get(self, request):
        return Response(SimbankAPIResponse("200", "OK", "", "System works normally"))


class AddView(APIView):
    def put(self, request):
        v_id = request.data.get('id')
        v_amount = request.data.get('amount')
        try:
            v_account = Account.objects.get(id=v_id)
        except Account.DoesNotExist:
            return Response(SimbankAPIResponse("400", "NOK", "", "Account doesn't exist"))
        serializer = AccountSerializer(v_account)
        if v_account.status == False:
            return Response(SimbankAPIResponse("400", 
                                               "NOK",
                                               { "account": serializer.data },
                                               "Account status if False (not active)"))
        v_account.add_to_balance(v_amount)
        return Response(SimbankAPIResponse("200",
                                           "OK",
                                           { "account": serializer.data },
                                           "Account balance updated successfully"))

class SubtractView(APIView):
    def put(self, request):
        v_id = request.data.get('id')
        v_amount = request.data.get('amount')
        try:
            v_account = Account.objects.get(id=v_id)
        except Account.DoesNotExist:
            return Response(SimbankAPIResponse("400", "NOK", "", "Account doesn't exist"))
        serializer = AccountSerializer(v_account)
        if v_account.status == False:
            return Response(SimbankAPIResponse("400",
                                               "NOK",
                                               { "account": serializer.data },
                                               "Account status if False (not active)"))
        if v_account.subtract_from_balance(v_amount) == -1:
            return Response(SimbankAPIResponse("400", 
                                               "NOK", 
                                               { "account": serializer.data }, 
                                               "Balance is less than hold+subtract"))
        else:
            return Response(SimbankAPIResponse("200", 
                                               "OK", 
                                               { "account": serializer.data },
                                               "Amount was subtracted successfully"))

class StatusView(APIView):
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(SimbankAPIResponse("200", 
                                           "OK", 
                                           { "accounts": serializer.data }, 
                                           "System works normally"))

