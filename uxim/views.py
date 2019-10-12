from django.http import HttpResponse
from django.shortcuts import render
#what render mean is simmilar to HttpResponse, but combine the request with html document and return things back.
#TemplateDoesNotExist error: 'cause I haven't actually set up django to look for the folder Templates 이건 서버 에러
from django.template.loader import get_template

def home_page(request):
	#request가 parmeter임.
	#return HttpResponse("<h1>Hello World</h1>")
	my_title = "Hello there...."
	#python's string format simmilar type code!
	#doc = "<h1>{title}</h1>".format(title = title)
	#중괄호를 두 개 사용한다는 점에 차이가 있음.
	#django_rendered_doc = "<h1>{{title}}</h1>".format(title = title)
	#What we're gonna show on our virtual environment
	#return 값에도 약간의 수정이 들어감. 
	#return render(request, "hello_world.html") -- before
	
	#14강
	#context = {"title": my_title}
	#template_name = "title.txt"
	#template_obj = get_template(template_name)
	#rendered_string = template_obj.render(context)
	#return render(request, "hello_world.html", {"title" : rendered_string})
	# former code) return render(request, "hello_world.html", {"title" : my_title})  #dictionary being appended!

	#16강: handling the logics in web pages
	context = {"title" : "my title"}
	if request.user.is_authenticated:
		#15강
		context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
	return render(request, "home.html", context)




def about_page(request):
	#1.return HttpResponse("<h1>About Us</h1>")
	return render(request, "about.html", {"title" : "About us"})

def contact_page(request):
	#1.return HttpResponse("<h1>Contact Us</h1>")
	return render(request, "hello_world.html", {"title" : "Contact us"})


def example_page(request):
	#rendering sth else: like .txt
	context           = {"title" : "Example"}
	template_name     = "hello_world.html"
	template_obj      = get_template(template_name)
	rendered_item     = template_obj.render(context)
	return HttpResponse(rendered_item)