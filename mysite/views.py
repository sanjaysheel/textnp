from django.http import HttpResponse
from django.shortcuts import render
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy
from spacy import displacy




def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newline = request.GET.get('newline','off')
    exsp = request.GET.get('exsp','off')
    capitalized = request.GET.get('capitalized','off')
    porterstmmer = request.GET.get('porterstmmer', 'off')
    snowballstemmer = request.GET.get('snowballstemmer', 'off')
    pos_neg = request.GET.get('pos_neg', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*~'''
        analyzed = ''
        for char in djtext.lower():
            if char not in punctuations:
                analyzed = analyzed + char
        # analyzed = djtext
        params = {'purpose': 'remove punctuations','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    elif fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'This is upper case','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    elif newline == 'on':
        analyzed = ''
        for char in djtext.lower():
            if char =='\n':
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'This is proper contain', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif exsp == 'on':
        analyzed = ''
        for index, char in enumerate(djtext.lower()):
            if djtext[index] == ' ' and djtext[index + 1] == ' ':
                pass
            else:
                analyzed = analyzed + char
                 
        params = {'purpose': 'This is proper contain', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params) 
    elif capitalized == 'on':
        analyzed = ''
        for index, char in enumerate(djtext.lower()) :
            if djtext[index] == '.':
                analyzed = analyzed + ' '
                if djtext[index+1]==' ' and djtext[index+2].isalpha():
                    analyzed = analyzed + djtext[index+1].capitalize()
            else:
                analyzed = analyzed + char
        params = {'purpose': 'This is proper contain', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif porterstmmer == 'on':
        analyzed = ''
        lst=[]
        lst1=[]
        for char in djtext.lower().split(' '):
            lst.append(char)
        ps=PorterStemmer()
        # lst1=ps.stem(lst)[:]
        for i in lst:
            s=ps.stem(i)
            lst1.append(s)

        print(lst1)
        # for i in ps:
        #     lst1.append(ps.stem(i))
        # analyzed = djtext
        params = {'purpose': 'stem','analyzed_text':lst1}
        return render(request, 'analyze.html',params)
    elif snowballstemmer == 'on':
        analyzed = ''
        words=[]
        from nltk.stem.snowball import SnowballStemmer
        st = SnowballStemmer(language="english")
        st1 = {}
        for char in djtext.lower().split(' '):
            words.append(char)
        for word in words:
            st1[word] = st.stem(word)

        # st= SnowballStemmer(language="english")
        # # lst1=ps.stem(lst)[:]
        # for i in lst:
        #     s = ps.stem(i)
        #     lst1.append(s)
        #
        print(st1)

        # for i in ps:
        #     lst1.append(ps.stem(i))
        # analyzed = djtext
        params = {'purpose': 'stem', 'analyzed_text': st1}
        return render(request, 'analyze.html', params)
    elif pos_neg == 'on':
        sid = SentimentIntensityAnalyzer()
        analyzed=sid.polarity_scores(djtext.lower())
        params = {'purpose': 'positive and negative', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("please chick in the cheakbox")          
  
  
  

# def home(request):
#     # return HttpResponse('Home')
#     return HttpResponse("<h1>home-page</h1><a href='/about'>this is about page</a>")
#     # return HttpResponse("<h1>about-page</h1><a href='/'>this is back page</a>")

# def about(request):
#     return HttpResponse("<h1>about-page</h1><a href='/back'>this is back page</a>")
#     # return HttpResponse("<h1>about-page</h1><a href='/back'>this is back page</a>")
