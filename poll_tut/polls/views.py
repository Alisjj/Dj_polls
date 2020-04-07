from django.shortcuts import render
from .models import Poll, Choice
from django.shortcuts import get_object_or_404

def poll_list(request):
    polls = Poll.objects.all()
    context = { 'polls': polls }
    return render(request, 'polls/polls_list.html', context)

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    context = { 'poll' : poll }
    return render(request, 'polls/polls_detail.html', context)

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/polls_detail.html', {'poll': poll, 'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))