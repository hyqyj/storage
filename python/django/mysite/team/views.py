from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# Create your views here.
@csrf_exempt

def index(request):
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	#output = ", ".join([q.question_text for q in latest_question_list])
	template = loader.get_template("polls/index.html")
	context = {
		"latest_question_list":latest_question_list,
		"ADDR": request.META["REMOTE_ADDR"],
		"host": request.META["REMOTE_HOST"]
	}
	requestd = request
	return HttpResponse(template.render(context,request))
	#return HttpResponse(output)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, "polls/detail.html", {"question": question, "host": request.META["REMOTE_ADDR"]})
	#return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    #question = get_object_or_404(Question, pk=question_id)
    try:
    	question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
    	raise Http404("Question does not exist")
    return render(request, "polls/results.html", {"question": question, "host":request.method })

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    #return HttpResponse(request.POST["choice"])
    try:
    	selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
    	return render(
    			request,
    			"polls/detail.html",
    			{
    				"question":question,
    				"error_message":"You didn't select a choice.",
    				"yesorno": "no",

    			},
    		)
    else:
    	selected_choice.votes += 1
    	selected_choice.save()
    	return render(request, "polls/results.html", {"question":question})
