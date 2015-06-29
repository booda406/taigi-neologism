from django.shortcuts import render
from django.http import HttpResponse
from queryChinese.models import ChineseWord
import random


def query(request, wordQ):

    theAnswer = ChineseWord.objects.filter(word = wordQ)

    if(len(theAnswer) >= 1):
        tmp = ""
        for answer in theAnswer:
            tmp = tmp + answer.word + ":" + answer.pronounce.split("/")[0]

        return HttpResponse(tmp, content_type='text/plain; charset=utf-8')

    else:
        return HttpResponse("", content_type='text/plain; charset=utf-8')

def question(request):

    theQuestion = ChineseWord.objects.all()
    # theQuestion = [o for o in theQuestion if len(o.word) >= 2]

    oneQuestion = None
    oneQuestion = random.choice(theQuestion)
    while(len(oneQuestion.word) < 2):
        oneQuestion = random.choice(theQuestion)

    tmp = ""
    tmp = tmp + oneQuestion.word + ":" + oneQuestion.pronounce.split("/")[0]

    return HttpResponse(tmp, content_type='text/plain; charset=utf-8')
