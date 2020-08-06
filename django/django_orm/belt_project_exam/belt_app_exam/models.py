from django.db import models
import re, bcrypt


class UserManager(models.Manager):
	def registrationValidator(self, forminfo):
		validationErrors = {}
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if len(forminfo['email']) <1:
			validationErrors ['EmailRequired'] = "Email addresss should be valid."
		elif not EMAIL_REGEX.match(forminfo['email']):
			validationErrors['emailformat'] = "Email is invalid"
		else:
			usersWithEmail = User.objects.filter(email = forminfo['email'])
			print(usersWithEmail)
			if len(usersWithEmail)> 0:
				validationErrors['emailtaken'] = "Email is already taken, use another Email."

		if len(forminfo['password'])<8:
			validationErrors ['password'] = "Password should be at least 8 characters."
		if (forminfo['password']) != forminfo ['confirm']:
			validationErrors ['confirm'] = "confirm password must match."
		
		return validationErrors 

	def loginValidator(self, forminfo):
		errors = {}
		if len(forminfo['email']) <1:
			errors['email'] = "Email addresss should be valid."
		usersWithEmail = User.objects.filter(email = forminfo['email'])
		print(usersWithEmail)
		if len(usersWithEmail)== 0:
			errors['emailnotfound'] = "Email wasn't found, please register first."
		else:
			user = usersWithEmail[0]
			
			if not bcrypt.checkpw(forminfo['password'].encode(), user.password.encode()):
				errors ['password'] = 'password does not match'
		
		return errors
	
	def quoteValidator(self, forminfo):
		errors = {}
		if len (forminfo['quotedby']) <2:
			errors['quotedby'] = 'Quoted By needs at least 2 characters.'
		if len (forminfo['quote']) <10:
			errors['quote'] = 'Message needs at least 10 characters. '

		return errors



class User(models.Model):
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Post(models.Model):
	user = models.ForeignKey(User, related_name="post", on_delete=models.CASCADE)
	post = models.CharField(max_length=225)
	quoted_by = models.CharField(max_length=225, null = True)
	# name = models.ManyToManyField(User, related_name="email")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Favorite(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	objects = UserManager()

