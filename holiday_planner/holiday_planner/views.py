from django.shortcuts import render


# def home(request):
#     """ By default django looks at 'plans/templates/plans'"""
#     return render(request, 'home.html')

def home(request):
    """ Passing user friends as context """
    if request.user.is_authenticated:
        friends = Friend.objects.friends(request.user)
        return render(request, 'plans/home.html', context={"friends": friends})
    return render(request, 'plans/home.html')



