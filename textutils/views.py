#I have created this file - Kyoru
from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return render(request,'index.html')
    #return HttpResponse('''<h1>hello</h1><a  href="http://127.0.0.1:8000/capfirst">Capitalize first</a> <br><a href="http://127.0.0.1:8000/rempunc"> Remove punctuation</a><br><a href="http://127.0.0.1:8000/charcount">character count</a><br><a href="http://127.0.0.1:8000/spaceremover">spaceremover</a><br><a href="http://127.0.0.1:8000/charcount">character count(15)</a><br><a href="http://127.0.0.1:8000/newlineremover">_________</a><br>''')

def about(request):
    return HttpResponse("about<a href="/">back</a>")
def rempunc(request):
    #Get the text
    djtext=request.GET.get('text', 'default')
    print(djtext)
    #analyze the text
    return HttpResponse('Remove punctuation <a href="/">back</a>')
def capfirst(request):
    return HttpResponse("Capitalize First<a href='/'>back</a>")
def newlineremover(request):
    return HttpResponse("New line remover<a href='/'>back</a>")
def spaceremover(request):
    return HttpResponse("space remover<a href='/'>back</a>")
def charcount(request):
    return HttpResponse(f"character count ({len('character count')})<a href='/'>back</a>")
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    #Check checkbox values
    rempun=request.POST.get('rempun', '')
    fullcaps=request.POST.get('fullcaps','')
    newlineremover=request.POST.get('newlineremover','')
    extraspaceremover=request.POST.get('extraspaceremover','')
    charcounter=request.POST.get('charcounter','')
    #Check which checkbox is on
    d = {'purpose': [], 'analyzed_text': ''}
    if rempun == "on" or fullcaps =="on" or newlineremover=="on" or extraspaceremover=="on" or charcounter == "on":
            if rempun == "on":

                punctuation = '''!'"\,#$%&()*+-./:;<=>?@[]^_`{|}~'''
                analyzed = ""
                for i in djtext:
                    if i not in punctuation:
                        analyzed += i
                djtext=analyzed
                d['purpose'].append('Removed Punctuations')
                d['analyzed_text']=djtext
                # return render(request, 'analyze.html',d)
            if fullcaps =="on":
                analyzed=""
                for i in djtext:
                    analyzed+=i.upper()
                djtext = analyzed
                d['purpose'].append('CAPITALIZED')
                d['analyzed_text'] = djtext
                # d = {'purpose': 'CAPITALIZED', 'analyzed_text': analyzed}
#                 # return render(request, 'analyze.html', d)
            if newlineremover=="on":
                analyzed = ""
                for i in djtext:
                    if i!="\n" and i!="\r":
                        analyzed += i
                djtext = analyzed
                d['purpose'].append('New lines removed')
                d['analyzed_text'] = djtext
                # d = {'purpose': 'New lines removed', 'analyzed_text': analyzed}
                # return render(request, 'analyze.html', d)
            if extraspaceremover=="on":
                analyzed = ""
                for i, char in enumerate(djtext):
                    if djtext[i] == " " and djtext[i+1] == " ":
                        pass
                    else:
                        analyzed += char
                djtext = analyzed
                d['purpose'].append('Extra spaces removed')
                d['analyzed_text'] = djtext
                # d = {'purpose': 'Extra spaces removed', 'analyzed_text': analyzed}
                # return render(request, 'analyze.html', d)
            if charcounter == "on":
                analyzed = str(len(djtext))
                djtext = analyzed
                d['purpose'].append('Character count')
                d['analyzed_text'] += " " + "(" +str(len(djtext))+")"
                # d = {'purpose': 'Character count', 'analyzed_text': analyzed}
                # return render(request, 'analyze.html', d)

            return render(request, 'analyze.html', d)
    else:
        return HttpResponse("Error")
def ex1(request):
    s = '''<h1>Navbar</h1>
        <a  href="http://127.0.0.1:8000/capfirst">Capitalize first</a> <br>
        <a href="http://127.0.0.1:8000/rempunc"> Remove punctuation</a><br>
        <a href="http://127.0.0.1:8000/charcount">character count</a><br>
        <a href="http://127.0.0.1:8000/spaceremover">spaceremover</a><br>
        <a href="http://127.0.0.1:8000/charcount">character count(15)</a><br>
        <a href="http://127.0.0.1:8000/newlineremover">_________</a><br>'''
    return HttpResponse(s)
