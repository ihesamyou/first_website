# from django.shortcuts import redirect, render
# from django.urls import reverse
# from .models import Article
# from django.core.cache import cache
# from .forms import CommentForm, ContactForm
# from .models import Comment
# from django.shortcuts import get_object_or_404
# from django.contrib import messages
# from django.views.generic.edit import UpdateView, DeleteView
# from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def home(request):
#     """
#     Home page view. displays articles and a quote.
#     """
#     context = {
#         "articles": Article.objects.all().order_by("-date_posted"),
#         "quote": cache.get("quote"),
#         "quote_author": cache.get("quote_author"),
#     }
#     return render(request, "blog/home.html", context)


# def article(request, pk, cm=None):
#     """
#     Article view. pk is article's id and cm is id of a specific comment for replying.
#     shows details of an article including confirmed comments and a comment_form to submit
#     a new comment and a reply_form for a new reply to a comment if the cm argument is passed to the view.
#     """
#     article_obj = get_object_or_404(Article, id=pk)

#     if request.method == "POST":

#         if cm:
#             reply_form = CommentForm(request.POST)
#             comment_form = CommentForm()
#             if reply_form.is_valid:
#                 new_reply = reply_form.save(commit=False)
#                 new_reply.article = article_obj
#                 new_reply.comment = reply_form.cleaned_data.get("comment")
#                 new_reply.author = request.user
#                 new_reply.parent = Comment.objects.get(pk=cm)
#                 new_reply.save()
#                 messages.success(
#                     request,
#                     f"نظر شما با موفقیت ثبت شد و پس از تایید مدیر سایت نمایش داده خواهد شد.",
#                 )
#                 return redirect("article-detail", pk)

#         else:
#             comment_form = CommentForm(request.POST)
#             reply_form = CommentForm()
#             if comment_form.is_valid:
#                 new_comment = comment_form.save(commit=False)
#                 new_comment.article = article_obj
#                 new_comment.comment = comment_form.cleaned_data.get("comment")
#                 new_comment.author = request.user
#                 new_comment.save()
#                 messages.success(
#                     request,
#                     f"نظر شما با موفقیت ثبت شد و پس از تایید مدیر سایت نمایش داده خواهد شد.",
#                 )
#                 return redirect("article-detail", pk)
#     else:
#         comment_form = CommentForm()
#         reply_form = CommentForm()

#     context = {
#         "comment_form": comment_form,
#         "reply_form": reply_form,
#         "cm": cm,
#         "article": article_obj,
#         "comments": Comment.objects.filter(article=article_obj, confirmed=True),
#     }

#     return render(request, "blog/article_detail.html", context)


# class CommentUpdateView(
#     LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
# ):
#     """
#     View for updating comments.
#     doesn't give access to comment if the user is not the author.
#     """

#     model = Comment
#     fields = ["comment"]
#     template_name = "blog/comment_update.html"
#     success_message = "دیدگاه شما با موفقیت ویرایش شد."

#     def test_func(self):
#         comment = self.get_object()
#         return self.request.user == comment.author


# class CommentDeleteView(
#     LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
# ):
#     """
#     View for deleting comments.
#     doesn't give access to comment if the user is not the author.
#     """

#     model = Comment
#     fields = ["comment"]
#     template_name = "blog/comment_delete.html"

#     def test_func(self):
#         comment = self.get_object()
#         return self.request.user == comment.author

#     def get_success_url(self):
#         messages.success(self.request, "دیدگاه شما با موفقیت حذف شد.")
#         return reverse(article, kwargs={"pk": self.object.article.id})


# def contact(request):
#     """
#     Contact page view.
#     Uses ContactForm modelform to save user messages into ContactMessage model.
#     """
#     if request.method == "POST":
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             form.save()
#             messages.success(request, "پیام شما با موفقیت ثبت شد.")

#     form = ContactForm()
#     context = {"form": form}
#     return render(request, "blog/contact.html", context)
