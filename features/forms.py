from django import forms
from .models import Currency


class FibonacciIndex(forms.Form):
    index = forms.IntegerField(
        label='nامین عدد دنباله:', required=False, max_value=1000)


class FibonacciUntil(forms.Form):
    values_until = forms.IntegerField(label='دنباله تا مقدار:', required=False, error_messages={
        'max_value': 'عدد ورودی بیش از حد بزرگ است.'}, max_value=26863810024485359386146727202142923967616609318986952340123175997617981700247881689338369654483356564191827856161443356312976673642210350324634850410377680367334151172899169723197082763985615764450078474174627)


class CurrencyForm(forms.Form):
    rial = forms.FloatField(label='مقدار (ریال)', error_messages={
                            'required': 'Please enter your name',
                            'invalid': 'Enter your name'})
    selected_currency = forms.ModelChoiceField(
        queryset=Currency.objects.all(), label='ارزها', error_messages={
            'required': 'این مقدار الزامی است.',
            'invalid_choice': 'این مقدار الزامی است.'
        })
