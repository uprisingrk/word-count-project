from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()
    worddictionary = {}
    for word in wordcount:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    return render(request, 'count.html', {'fulltext': fulltext, 'totword': len(wordcount), 'word_dictionary': worddictionary})


def detail(request):
    return render(request, 'detail.html')
