from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import F
from .models import Review


def reviews(request):
    '''
    :param request: reviews
    :return: page with reviews for Stylist
    '''

    reviews_list = Review.objects.filter(stylist_id=10)
    for r in reviews_list:
        print("Review Name: {}".format(r.title))

    return render(request, 'reviews/reviews.html', {'reviews_list': reviews_list})


def comment(request):
    '''
    :param request: reviews
    :return: page with reviews for Stylist
    '''

    return render(request, 'reviews/leavecomment.html')


def upvote(request):
    '''
    :param request: reviews
    :return: page with reviews for Stylist
    '''

    vote = request.POST['vote']
    msg_id = request.POST['id']

    #review = Review.objects.filter(pk=msg_id).update(helpful_count=F('helpful_count') + 1)
    review = Review.objects.get(pk=msg_id)
    review.update_vote(vote)
    review.save()


    print("MSG ID: " + msg_id)
    return HttpResponse(200)
