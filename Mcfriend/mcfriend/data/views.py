from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import coupon,following
def profile(request):
	"""
	coupons = request.user.coupon.all()
	context = {
	'coupons':coupons,
	}
	return render(request,'data/profile.html',context)"""
	if request.user.is_authenticated():
		return redirect('/user/'+request.user.username)
	else:
		return redirect('/')

def userlist(request):
	users = User.objects.order_by('-last_login')

	context = {
	'users':users,
	}
	return render(request,'data/userlist.html',context)

def user(request,user_username):
	user_id = User.objects.get(username=user_username).id
	user = get_object_or_404(User,pk=user_id)
	user_coupon = user.coupon.order_by('-pub_date')
	context = {
	'user':user,
	'user_coupon':user_coupon,
	}
	return render(request,'data/user.html',context)

def load_coupon(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/login')

	coupon_list = coupon.FOOD_LIST
	context={
	'coupon_list':coupon_list,
	}
	return render(request,'data/load_coupon.html',context)

def add(request):
	print("oh")
	c=request.user.coupon.create(food=request.POST['choice'],comment=request.POST['comment'])
	c.save()
	return redirect('/')
def follow(request,user_id,action):
	if user_id and action:
		try:
			user = User.objects.get(id=user_id)
			if action == 'follow':
				following.objects.get_or_create(follower=request.user,target=user)
			else:
				following.objects.filter(follower=request.user,target=user).delete()
			return redirect('/list/')
		except User.DoesNotExist:
			return redirect('/list/')
	return redirect('/list/')
