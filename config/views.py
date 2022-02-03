from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from steamscraper import SteamProfile, steam_profile_url_is_valid


def home(request):
    return render(request, 'home.html')

def results(request):
    steam_url = request.GET.get('steamURL')
    if steam_url and steam_profile_url_is_valid(steam_url):
        try:
            steam_profile = SteamProfile.from_url(steam_url)
            print(steam_profile)
            data = steam_profile.to_json()
            print(data)
            context = {'data': data}
            return render(request, 'results.html', context)
        except Exception as e:
            print(e)
            feedback = 'My code failed to scrape your data... Not your fault.'
            feedforward = 'Please try again 🙂'
            messages.error(request, f'{feedback} {feedforward}')
            return redirect('home')
    else:
        messages.error(request, 'You must enter a Steam Profile URL')
        return redirect('home')