from django.shortcuts import render
import wordcount.views

# Create your views here.
def index(request):
    return render(request, 'index.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_disctionary = {}
    

    for word in word_list:
        if word in word_disctionary:
            #Increase
            word_disctionary[word] += 1
        else:
            #add to the dictionary
            word_disctionary[word] = 1
    return render(request, 'count.html', {'fulltext':fulltext, 'total':len(word_list),})
