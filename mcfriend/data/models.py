from django.db import models
from django.contrib.auth.models import User
from datetime import date
class coupon(models.Model):
	user = models.ForeignKey(User,null=True,related_name='coupon')
	
	comment = models.CharField(max_length=200,blank=True)
	FOOD_CHOICE = (
        ('Fillet_O_Fish', '麥香魚'),
        ('French_Fries', '中薯'),
        ('McNugget','麥克雞塊'),
    )
	FOOD_LIST = ['Fillet_O_Fish','French_Fries','McNugget']
	food = models.CharField(max_length=50,choices=FOOD_CHOICE,blank=False)
	# DATE
	pub_date = models.DateTimeField('date published',blank=True,auto_now_add=True)

	#image = models.ImageField(null=True,blank=False)
	def __str__(self):
		return self.user.username+"------"+self.food+"------"+str(self.pub_date)


class following(models.Model):
	follower = models.ForeignKey(User,null=True,related_name='target')
	target = models.ForeignKey(User,null=True,related_name='follower')
	def __str__(self):
		return self.follower.username + "___follows___" +self.target.username

User.add_to_class('following',models.ManyToManyField('self',through=following,related_name='followers',symmetrical=False))