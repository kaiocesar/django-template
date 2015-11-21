from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	template = loader.get_template('customers/home.html')
	context = RequestContext(request, {
		'latest_question_list': {}
		})
	return HttpResponse(template.render(context))
