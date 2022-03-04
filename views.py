#5th video onwards real stuff
#created by me -$ATY

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params ={'name':'saty','place':'mars'}
    return render(request, 'index.html', params)

def analyze(request):
    #get the text
    djtext = (request.POST.get('text', 'default'))
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.POST.get('fullcaps', 'off'))
    newlr = (request.POST.get('nlr', 'off'))
    esr = (request.POST.get('esr', 'off'))
    charcount = (request.POST.get('charcount', 'off'))
    print(djtext)
    print("removepunc is ",removepunc)
    print("fullcaps is",fullcaps)
    print("new line remover is",newlr)
    print("space remover is",esr)
    print("character counter is",charcount)
    #analyse the text
    punctuations = """!()-[]{}:;'"\,<>./?@#$%^&*_~"""
    analyzed=""
    if removepunc=="on":
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params ={'purpose':'remove punctuations','analyzed_text':analyzed}
        djtext=analyzed
    
    if fullcaps=="on":
        analyzed=djtext.upper()
        params ={'purpose':'UPPERCASE','analyzed_text':analyzed}
        djtext=analyzed
        
    
    if newlr=="on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char       
        params ={'purpose':'new line remover','analyzed_text':analyzed}
        djtext=analyzed
        
    
    if esr=="on":
        analyzed=""
        djtext=djtext.strip()
        for i in range(0,len(djtext)):
            if djtext[i] == " " and djtext[i+1]==" ":
                pass
            else:
                analyzed=analyzed+djtext[i]

        params ={'purpose':'extra space remover','analyzed_text':analyzed}
        djtext=analyzed
        
    
    if charcount=="on":
        count=0
        for i in djtext:
            count=count+1
        counter="total characters = "+str(count)

        analyzed=""
        for i in range(0,len(djtext)):
            analyzed=analyzed+djtext[i]

        params ={'purpose':'character counter','analyzed_text':analyzed,'counters':counter}
        djtext=analyzed
        


    if charcount!="on" and esr!="on" and newlr!="on" and fullcaps!="on" and removepunc!="on":
        analyzed=djtext
        params ={'purpose':'nothing','analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    
    return render(request, 'analyze.html', params)
