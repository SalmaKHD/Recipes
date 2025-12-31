from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager): # base object manager that comes with auth app
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name) # model created by manager
        user.set_password(password) # encrypted by default
        user.save(using=self._db)
        return user

    # for when createsuperuser is called
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True # automatically created by permissionmixin
        user.is_staff = False
        user.save(using=self._db)
        return user

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    ''' model for our users '''
    ''' will work with django admin and auth sysytem'''
    email = models.EmailField(max_length=255, unique=True) # must be unique in our table
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # for permissions
    is_staff= models.BooleanField(default=False) # for permissions

    objects =  UserProfileManager() # used to define manager for our model

    USERNAME_FIELD = 'email' # replace username field of auth with email field for auth
    REQUIRED_FIELDS = ['name'] # make it required

    def get_full_name(self):
        ''' get full name of user '''
        return self.name

    def __str__(self):
        return self.email