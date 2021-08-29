from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
                'shows': TVShow.objects.all()
              }
    return render(request, 'shows.html', context)


def shows_new(request):
    context = {
                'redirect': 'create',
                'networks': Network.objects.all()
              }
    return render(request, 'show_new.html', context)

def shows_create(request):
    network = Network.objects.get(id=request.POST['network'])
    newshow = TVShow.objects.create(title=request.POST['title'],
                                    network=network,
                                    release_date=request.POST['release_date'],
                                    description=request.POST['description']
                                   )
    return redirect(f'/shows/{newshow.id}')


def show(request, show_id):
    context = {
                'show': TVShow.objects.get(id=show_id)
              }
    return render(request, 'show.html', context)


def shows_new(request):
    context = {
                'title':    'Add A New TV Show',
                'action':   '/shows/create',
                'submit':   'Create',
                'networks': Network.objects.all(),
                'show':     {
                              'title':        '',
                              'network':      '',
                              'release_date': '',
                              'description':  '',
                            }
              }
    return render(request, 'show_edit.html', context)


def show_edit(request, show_id):
    context = {
                'title':    f'Edit Show {show_id}',
                'action':   f'/shows/{show_id}/update',
                'submit':   'Update',
                'networks': Network.objects.all(),
                'show':     TVShow.objects.get(id=show_id)
              }
    return render(request, 'show_edit.html', context)



def show_update(request, show_id):
    show = TVShow.objects.get(id=show_id)
    # Only update the db if any of the data changed
    if (show.title != request.POST['title'] or
        show.network.id != request.POST['network'] or
        show.release_date != request.POST['release_date'] or
        show.description != request.POST['description']):
            show.title = request.POST['title']
            show.network = Network.objects.get(id=request.POST['network'])
            show.release_date = request.POST['release_date']
            show.description = request.POST['description']
            show.save()
    return redirect(f'/shows/{show_id}')

def show_delete(request, show_id):
    context = {
                'show': TVShow.objects.get(id=show_id)
              }
    return render(request, 'delete.html', context)

def show_destroy(request, show_id):
    show = TVShow.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')
