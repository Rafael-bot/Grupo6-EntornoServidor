from django.shortcuts import render


# Create your views here.
def personalPosts(request):
    context = {}
    return render(request, 'Posts/personalPosts/personalPosts.html', context=context)


def publicPosts(request):
    context = {}
    return render(request, 'Posts/publicPosts/publicPosts.html', context=context)


def comments(request):
    context = {}
    return render(request, 'Posts/comments/comments.html', context=context)
