from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from datetime import datetime
import hashlib
import random

def root(request):
    seasons = [1, 2, 3, 4, 5, 6, 7]
    season1 = []
    season2 = []
    season3 = []
    season4 = []
    season5 = []
    season6 = []
    season7 = []

    # creates a list of each episode in each season
    for i in range(1, 26):
        print i
        season1.append(i)

    for i in range(1, 22):
        season2.append(i)

    for i in range(1, 26):
        season3.append(i)

    for i in range(1, 26):
        season4.append(i)

    for i in range(1, 26):
        season5.append(i)

    for i in range(1, 26):
        season6.append(i)

    for i in range(1, 26):
        season7.append(i)

    random.shuffle(seasons)
    season = seasons[1]
    print "Season: %d" % season

    if season == 1:
        random.shuffle(season1)
        e = season1[1]
    elif season == 2:
        random.shuffle(season2)
        e = season2[1]
    elif season == 3:
        random.shuffle(season3)
        e = season3[1]
    elif season == 4:
        random.shuffle(season4)
        e = season4[1]
    elif season == 5:
        random.shuffle(season5)
        e = season5[1]
    elif season == 6:
        random.shuffle(season6)
        e = season6[1]
    else:
        random.shuffle(season7)
        e = season7[1]

    return HttpResponse("Season: " + str(season) + ", Episode: " + str(e) ) 
