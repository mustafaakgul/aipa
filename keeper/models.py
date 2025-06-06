from django.db import models
from django.contrib.auth.models import User


TRANSACTION_TYPE_CHOICES = [
    ('add', 'Add'),
    ('delete', 'Delete'),
    ('update', 'Update'),
]


class Keeper(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    size = models.IntegerField(default=1)
    status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    target_date = models.DateField(blank=True, null=True)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class KeeperTransaction(models.Model):
    keeper = models.ForeignKey(Keeper, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=255, choices=TRANSACTION_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.keeper} - {self.transaction_type}"
    

class KeeperDailyReminderAssistant(models.Model):
    keeper = models.ForeignKey(Keeper, on_delete=models.CASCADE)
    date = models.DateField()
    notification = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.keeper.name} - {self.date}"
    

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Feature(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    

class ProjectIncome(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.project.name} - {self.amount}"
    

class Capacity(models.Model):
    day = models.IntegerField()
    hour = models.IntegerField()
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
