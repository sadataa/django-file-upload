from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import AccountManager

class Account(AbstractBaseUser):

    class Types(models.TextChoices):
        EMPLOYEE         = "EMPLOYEE", "Employee"
        MANAGER          = "MANAGER", "Manager"

    default_type = Types.EMPLOYEE

    type = models.CharField(max_length=50, choices=Types.choices, default=default_type)
    username   = models.CharField(max_length=255, unique=True)
    email      = models.EmailField(unique=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    date_joined = models.DateTimeField(verbose_name='date join', auto_now_add=True)
    is_active  = models.BooleanField(default=True)
    is_staff   = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_perm(self, perm, obj=None):
        
        return True
    
    def has_module_perms(self, app_label):
    
        return True
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.default_type
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username

class ManagerMore(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, unique=True)

class EmployeeMore(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.user.username


class EmployeeMnagers(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Account.Types.EMPLOYEE)

class Employee(Account):
    default_type = Account.Types.EMPLOYEE

    objects = EmployeeMnagers()

    class Meta:
        proxy = True
    
    def blog_writer(self):
        return "I'm a Employee."
    
    @property
    def employeemore(self):
        return self.EmployeeMore

class TotalManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Account.Types.MANAGER)

class Manager(Account):
    default_type = Account.Types.MANAGER

    objects = TotalManager()

    class Meta:
        proxy = True

    def blog_manager(self):
        return "I'm a manager."

    @property
    def managermore(self):
        return self.ManagerMore