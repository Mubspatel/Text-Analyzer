# Created by me
from django.http import HttpResponse
from django.shortcuts import render


def index(req):
    return render(req, 'index.html')


def analyzer(req):
    text = req.POST.get('text', 'off')
    print(text)
    remove_punc = req.POST.get('remove_punc', 'off')
    punctuations = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uppercase = req.POST.get('uppercase','off')
    char_count = req.POST.get('char_count','off')
    remove_newline = req.POST.get('remove_newline','off')
    remove_space = req.POST.get('remove_space','off')
    analyzed = ""
    if remove_punc == 'on':
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'data': analyzed}
        return render(req, 'analyzer.html',params)
    elif uppercase == 'on':
        analyzed = text.upper()
        params = {'data': analyzed}
        return render(req, 'analyzer.html', params)
    elif remove_newline == 'on':
        for char in text:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'data': analyzed}
        return render(req, 'analyzer.html', params)
    elif remove_space == 'on':
        analyzed = "".join(text.split())
        params = {'data': analyzed}
        return render(req, 'analyzer.html', params)
    elif char_count == 'on':
        analyzed = ""
        analyzed = len(char_count)
        params = {'data',analyzed}
        return render(req, 'analyzer.html', params)
    else:
        return HttpResponse("Error")

