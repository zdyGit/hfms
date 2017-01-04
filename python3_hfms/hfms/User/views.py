from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect  
import simplejson
from django.http import HttpResponse 
from User import models
from datetime import datetime
import hashlib


# Create your views here.
def index(request):
	return render(request,'index.html')

def home(request):
	return render(request,'home.html')

def Login(request):
	uid = request.GET["uid"]
	pwd = request.GET["pwd"]
	pwd = MD5(pwd)
	users = models.Sys_User.objects.filter(userID=uid,pwd=pwd)
	if len(users)>0:
		# request.session["user"] = users[0].id
		# request.session["loginDateTime"] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
		request.session.set_expiry(120) 
		sc = "window.location.href = '/home/'"
	else:
		sc  ="alert('login failed')"
	return HttpResponse(sc)

def register(request):
	return render(request,'register.html')

def userInfo_insert(request):
	res = {}
	res["state"] = True
	print(request.POST["csrfmiddlewaretoken"])
	try:
		postData = request.POST["userInfo"]
		postData = simplejson.loads(postData)
		user = models.Sys_User()
		user.userID = postData["userID"]
		user.userName = postData["userName"]
		user.pwd = postData["confirmPWD"]
		user.createDate = datetime.today()
		if len(models.Sys_User.objects.filter(userID = user.userID))>0:
			res["state"] = False
			res["message"] = "User has been exists"
		else:
			user.pwd = MD5(user.pwd)
			uid = user.save()
	except Exception as e:
		res["state"] = False
		res["message"] = str(e)
	if res["state"] == True:
		res["message"] = "window.location.href = '/'"
	return HttpResponse(simplejson.dumps(res))

def active(request):
	# if request.session.get("user","none") == "none":
	# 	return HttpResponse("false")
	return HttpResponse("true")

def MD5(s):
	m = hashlib.md5(s.encode(encoding="utf-8"))
	return m.hexdigest()

