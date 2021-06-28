# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index2.html')

def analyze(request):
    #Get the text
    djtext=request.POST.get('text','default')
    #Check checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    countingcharacter=request.POST.get('countingcharacter','off')
    #Check which checkbox is on
    if removepunc=="on":
        # analyzed=djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed ExtraSpace', 'analyzed_text': analyzed}
        djtext = analyzed
    if(countingcharacter=="on"):
        analyzed = 0
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                if char != "\n":
                    if char!=" ":
                        analyzed = analyzed + 1
        params = {'purpose': 'Counting number of characters', 'analyzed_text': analyzed}
        djtext = analyzed
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze2.html', params)
