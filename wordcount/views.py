from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")


def count(request):
    fulltext = request.GET["fulltext"];

    worddictionary = {}

    for word in fulltext.split():
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    return render(request, 'count.html', {'fulltext': request.GET["fulltext"], 'wordscount': len(fulltext.split()),
                                          'worddictionary': worddictionary})


def about(request):
    return render(request, 'about.html')
