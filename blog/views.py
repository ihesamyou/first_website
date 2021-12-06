from django.shortcuts import redirect, render
from .models import Article
from django.core.cache import cache
from .forms import CommentForm, ContactForm
from .models import Comment
from django.shortcuts import get_object_or_404
from django.contrib import messages


def home(request):
    context = {
        'articles': Article.objects.all(),
        'quote': cache.get('quote')
    }
    return render(request, 'blog/home.html', context)


def article(request, pk, cm=None):
    article_obj = get_object_or_404(Article, id=pk)

    if request.method == 'POST':

        if cm:
            reply_form = CommentForm(request.POST)
            comment_form = CommentForm()
            if reply_form.is_valid:
                new_reply = reply_form.save(commit=False)
                new_reply.article = article_obj
                new_reply.comment = reply_form.cleaned_data.get('comment')
                new_reply.author = request.user
                new_reply.parent = Comment.objects.get(pk=cm)
                new_reply.save()
                messages.success(request, f'نظر شما با موفقیت ثبت شد.')
                return redirect('article-detail', pk)

        else:
            comment_form = CommentForm(request.POST)
            reply_form = CommentForm()
            if comment_form.is_valid:
                new_comment = comment_form.save(commit=False)
                new_comment.article = article_obj
                new_comment.comment = comment_form.cleaned_data.get('comment')
                new_comment.author = request.user
                new_comment.save()
                messages.success(request, f'نظر شما با موفقیت ثبت شد.')
                return redirect('article-detail', pk)
    else:
        comment_form = CommentForm()
        reply_form = CommentForm()

    context = {
        'comment_form': comment_form,
        'reply_form': reply_form,
        'cm': cm,
        'article': article_obj,
        'comments': Comment.objects.filter(article=article_obj)
    }

    return render(request, 'blog/article_detail.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'پیغام شما با موفقیت ثبت شد.')

    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'blog/contact.html', context)
