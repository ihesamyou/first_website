from django import forms
from .models import Currency


class FibonacciIndex(forms.Form):
    index = forms.IntegerField(
        label='nامین عدد دنباله:', required=False, max_value=1000)


class FibonacciUntil(forms.Form):
    values_until = forms.IntegerField(label='دنباله تا مقدار:', required=False, error_messages={
        'max_value': 'عدد ورودی بیش از حد بزرگ است.'}, max_value=26863810024485359386146727202142923967616609318986952340123175997617981700247881689338369654483356564191827856161443356312976673642210350324634850410377680367334151172899169723197082763985615764450078474174627)


class RialForm(forms.Form):
    rial_amount = forms.IntegerField(label='مقدار (ریال)', required=False,
                                     max_value=99999999999999999999999999999999999999,
                                     error_messages={
                                         'max_value': 'مقدار ورودی بیش از حد بزرگ است.'}
                                     )
    r_selected_currency = forms.ModelChoiceField(
        queryset=Currency.objects.all(), label='ارز', required=False)


class CurrencyForm(forms.Form):
    c_selected_currency = forms.ModelChoiceField(
        queryset=Currency.objects.all(), label='ارز', required=False)
    currency_amount = forms.FloatField(label='مقدار ارز مورد نظر', required=False,
                                       max_value=99999999999999999999999999999999999999,
                                       error_messages={
                                           'max_value': 'مقدار ورودی بیش از حد بزرگ است.'}
                                       )
