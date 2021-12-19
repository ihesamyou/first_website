from django.shortcuts import render
from .forms import FibonacciIndex, FibonacciUntil, RialForm, CurrencyForm
from .fibonacci_sequence import fibonacci_index, fibonacci_until
from django.core.cache import cache


def fibonacci(request):
    """uses fibonacci_sequence module to calculate fibonacci sequence 
    in two different ways and will render the results on the fibonacci.html template."""

    if request.method == 'POST':
        f_index = FibonacciIndex(request.POST)
        f_until = FibonacciUntil(request.POST)

        if f_index.is_valid() and f_until.is_valid():
            index = f_index.cleaned_data['index']
            index_answer = fibonacci_index(index)
            values_until = f_until.cleaned_data['values_until']
            values_until_answer = fibonacci_until(values_until)
            context = {
                'f_index': f_index,
                'f_until': f_until,
                'index_answer': index_answer,
                'values_until_answer': values_until_answer
            }
            return render(request, 'features/fibonacci.html', context)
    else:
        f_index = FibonacciIndex()
        f_until = FibonacciUntil()
    return render(request, 'features/fibonacci.html', {'f_index': f_index, 'f_until': f_until})


def currency_converter(request):
    """
    A View with two forms. r_form is used for converting rial to other currencies and 
    c_form is used for converting other currencies to rial.
    since fields are not required in our forms, we check which of our forms are populated
    after form validation. context dictionary is populated according to conditionals.
    """

    if request.method == 'POST':
        r_form = RialForm(request.POST)
        c_form = CurrencyForm(request.POST)
        context = {}

        if r_form.is_valid() and c_form.is_valid():
            if r_form.cleaned_data['rial_amount']:
                r_selected_currency = r_form.cleaned_data['r_selected_currency']
                r_rate = cache.get(r_selected_currency)
                r_input = r_form.cleaned_data['rial_amount']
                r_answer = r_input/r_rate
                r_result = f"{r_input} ریال معادل {r_answer:.2f} {r_selected_currency} است.<br> هر {r_selected_currency} معادل {r_rate} ریال است."
                context['r_result'] = r_result

            if c_form.cleaned_data['currency_amount']:
                c_selected_currency = c_form.cleaned_data['c_selected_currency']
                c_rate = cache.get(c_selected_currency)
                c_input = c_form.cleaned_data['currency_amount']
                c_answer = c_input*c_rate
                c_result = f"{c_input:.2f} {c_selected_currency} معادل {int(c_answer)} ریال است.<br> هر {c_selected_currency} معادل {c_rate} ریال است."
                context['c_result'] = c_result

            context['r_form'] = r_form
            context['c_form'] = c_form
            return render(request, 'features/currency_converter.html', context)
    else:
        r_form = RialForm()
        c_form = CurrencyForm()

    context = {
        'r_form': r_form,
        'c_form': c_form
    }
    return render(request, 'features/currency_converter.html', context)
