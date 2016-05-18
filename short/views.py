from django.http import HttpResponse
from django.shortcuts import redirect,render,get_object_or_404
from .models import Shorts

# Create your views here.


def visit_link(request,link):
	sen=get_object_or_404(Shorts,outgoingurl1=link)
	sen1=sen.incomingurl
	return redirect(sen1)


def short_home(request):
	
	q,qq,e=0,0,0
	z,zz='',''
	if 'in1' and 'out1' in request.GET :
		in1 = request.GET["in1"]
		out1=request.GET["out1"]
		#print (in1)
		#print (out1)
		#print('span')
		if in1 is "":
			print("in1  empty") 
		elif out1 is  "":
			#print('noe')
			q=0
		else:
			try:
				ob=Shorts.objects.get(outgoingurl1=out1)
			except:
				ob=None
			if ob is None:
				Shorts.objects.create(incomingurl=in1,outgoingurl1=out1)
			else:
				e=1
			
			q=1
			z=in1
			zz=out1
	if 'in1' in  request.GET and q==0:
		#print('no')

		in1 = request.GET["in1"]
		if in1 is "":
			print("in1 is empty")
		else:
					#print(in1)
			from random import choice
			from string import ascii_uppercase
			out1=''.join(choice(ascii_uppercase) for i in range(3))
			while 1:
				try:
					ob=Shorts.objects.get(outgoingurl1=out1)
				except:
					ob=None
				if ob is None:
					break
				out1=''.join(choice(ascii_uppercase) for i in range(3))

		#print(out1)
			Shorts.objects.create(incomingurl=in1,outgoingurl1=out1)
			z=in1
			zz=out1
			qq=1


	print(z)
	print(zz)
	print(qq)
	context = {
	 "e":e,
		"z":z,
		"zz":zz,
		"q":q,
		"qq":qq,
		
	}


	return render(request,"index.html",context)
	
