# I have created this file - Shwet

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

 #   return HttpResponse("Home <a href='/spaceremover'>SR</a> <a href='/capfirst'>CF</a> <a href='/charcounts'>CC</a>")

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc == "on":
        punctuations = '''.,?!'":;...-[]()/{}\<>@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
      #  return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppse Case', 'analyzed_text': analyzed}
        djtext = analyzed
     #   return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
     #   return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
     #   return render(request, 'analyze.html', params)

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)

