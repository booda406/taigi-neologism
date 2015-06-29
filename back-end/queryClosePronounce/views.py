from django.shortcuts import render
from django.http import HttpResponse
from queryClosePronounce.models import Pronounce
from difflib import SequenceMatcher


def similar(strA, strB):
	return SequenceMatcher(None, strA, strB).ratio()


def hello_world(request):
    return HttpResponse("Hello taigiGameDB!", content_type='text/plain; charset=utf-8')


def query(request, pronounceQ):

    # cut off if pronounceQ is too short
    # if(len(pronounceQ) <= 1):
        # return HttpResponse("Query is too short", content_type='text/plain; charset=utf-8')

    # the string for returning
    theAnswer = ""

    allPronounce = Pronounce.objects.all()

    # The rank for all simlarities(pronounce, pronounceQ)
    # Higher is better
    theRank = {}

    # singlePronounce contains its pronounce and matching chinese chracters
    for singlePronounce in allPronounce:
		tmp = similar(pronounceQ, singlePronounce.pronounce)
		if(tmp > 0.6):
			theRank[singlePronounce.pronounce] = tmp

    # sorting ranking and append result to theAnswer
	# and use "," to seperate the char!!!!  thx Julia
    for theKey, theSimilarity in sorted(theRank.iteritems(), key = lambda (k, v) : (v, k), reverse=True):
		theAnswer = theAnswer + allPronounce.get(pronounce = theKey).chineses + ","

	# clear last ","
    if(theAnswer[-1] == ","):
		theAnswer = theAnswer[0:-1]

	# let's split and join >w<
    theChSet = list(set(theAnswer.split(",")))

    # confirm the number of words is greater than 20
    theSetLen = len(theChSet)
    if (theSetLen < 20):
        theAnswer = ""
        theRank = {}
        for singlePronounce in allPronounce:
            tmp = similar(pronounceQ, singlePronounce.pronounce)
            if(tmp > 0.4):
                theRank[singlePronounce.pronounce] = tmp
        for theKey, theSimilarity in sorted(theRank.iteritems(), key = lambda (k, v) : (v, k), reverse=True):
            theAnswer = theAnswer + allPronounce.get(pronounce = theKey).chineses + ","
        if(theAnswer[-1] == ","):
            theAnswer = theAnswer[0:-1]
        theChSet = list(set(theAnswer.split(",")))


    comma = ","
    theAnswer = comma.join(theChSet)

    if(theAnswer == ""):
        return HttpResponse("", content_type='text/plain; charset=utf-8')
    else:
        return HttpResponse(theAnswer, content_type='text/plain; charset=utf-8')
