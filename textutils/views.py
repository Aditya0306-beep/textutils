# #Linking the links to our website

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')



def analyze(request):
    # Get the Tezt
    djtext=request.POST.get('text','default')  #It return the value in the Pycharm terminal and get the data from html input text

    # Check Checkbox Values
    removepunc=request.POST.get('removepunc','Off')
    Uppercase=request.POST.get('Uppercase','Off')
    Lineremover=request.POST.get('Lineremover','Off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    # Check which checkbox is On
    if removepunc == "on":
        analyzed = ""
        punctions = ''''!@#$%^&*()_{}[]|\?<>~`'''
        for char in djtext:
            if char not in punctions:
                analyzed = analyzed + char
        params={'purpose':'Remove Punction','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif Uppercase=="on":
        analyzed=""
        for char in djtext:
            if char.islower():
                analyzed = analyzed + char.upper()
            else:
                analyzed =analyzed + char
        params = {'purpose': 'Converting to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif Lineremover=='on':
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':  #We have to pass both to remove the nre line into our text
                analyzed=analyzed+char
        params = {'purpose': 'New Line remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif extraspaceremover=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char

        params = {'purpose': 'Extra space Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif  charcounter=='on':
        analyzed=""
        c=0
        for char in djtext:
            c=c+1

        params = {'purpose': 'Character Counter', 'analyzed_text': f"No of character in your String is{c}"}
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse("Error")










