from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ONETIMEPAYMENTApi() # issue here
confirmation_number = 'confirmation_number_example' # str | Payment reference number. The number is returned when the payment is successfully added. Format: 999-99-99.
delete_request = swagger_client.PaymentDeleteRequest() # PaymentDeleteRequest | deleteRequest

try:
    # Cancel Payment by Confirmation Number
    api_response = api_instance.delete_payment_using_delete(confirmation_number, delete_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ONETIMEPAYMENTApi->delete_payment_using_delete: %s\n" % e)
