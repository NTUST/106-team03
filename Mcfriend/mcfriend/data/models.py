from django.db import models
from django.contrib.auth.models import User
from datetime import date
class coupon(models.Model):
	user = models.ForeignKey(User,null=True,related_name='coupon')
	
	comment = models.CharField(max_length=200,blank=True)
	FOOD_CHOICE = (
        ('Spicy_chicken_filet','勁辣雞腿堡 買一送一'),
        ('French_Fries','大薯 買一送一'),
        ('McFlurry','冰炫風'),
        ('Happy_sticker','歡樂貼'),
    )
	FOOD_LIST = ['Spicy_chicken_filet','French_Fries','McFlurry','Happy_sticker']
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