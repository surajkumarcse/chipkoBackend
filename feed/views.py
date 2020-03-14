from django.shortcuts import render

# Create your views here.
def collectFeed(request):
    return render(request, 'feed/index.html', {})

def cauverycalling(request):
    return render(request, 'feed/organisationProfile.html', {})

def teamtrees(request):
    return render(request, 'feed/organisationProfile2.html', {})