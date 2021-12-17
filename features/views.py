from django.shortcuts import render
from .forms import FibonacciIndex, FibonacciUntil, CurrencyForm
from .fibonacci_sequence import fibonacci_index, fibonacci_until


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
    # if request.method == 'POST':
    #     f_index = FibonacciIndex(request.POST)
    #     f_until = FibonacciUntil(request.POST)

    #     if f_index.is_valid() and f_until.is_valid():
    #         index = f_index.cleaned_data['index']
    #         index_answer = fibonacci_index(index)
    #         values_until = f_until.cleaned_data['values_until']
    #         values_until_answer = fibonacci_until(values_until)
    #         context = {
    #             'f_index': f_index,
    #             'f_until': f_until,
    #             'index_answer': index_answer,
    #             'values_until_answer': values_until_answer
    #         }
    #         return render(request, 'features/fibonacci.html', context)
    # else:
    context = {
        'form': CurrencyForm
    }
    return render(request, 'features/currency_converter.html', context)
