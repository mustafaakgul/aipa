from django.contrib import admin
from .models import Keeper, Project, Feature, KeeperTransaction, KeeperDailyReminderAssistant, ProjectIncome, Capacity


@admin.register(Keeper)
class KeeperAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Keeper._meta.fields]
    list_display_links = ["id"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at", "deleted_at", "is_active"]

    class Meta:
        model = Keeper

    
@admin.register(KeeperTransaction)
class KeeperTransactionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in KeeperTransaction._meta.fields]
    list_display_links = ["id"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at", "deleted_at"]

    class Meta:
        model = KeeperTransaction


@admin.register(KeeperDailyReminderAssistant)
class KeeperDailyReminderAssistantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in KeeperDailyReminderAssistant._meta.fields]
    list_display_links = ["id"]
    search_fields = ["id"]
    list_filter = ["created_at"]

    class Meta:
        model = KeeperDailyReminderAssistant


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields]
    list_display_links = ["id"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at", "deleted_at"]

    class Meta:
        model = Project


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Feature._meta.fields]
    list_display_links = ["id"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at", "deleted_at"]

    class Meta:
        model = Feature

    
@admin.register(ProjectIncome)
class ProjectIncomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProjectIncome._meta.fields]
    list_display_links = ["id"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at", "deleted_at"]

    class Meta:
        model = ProjectIncome
        

@admin.register(Capacity)
class CapacityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Capacity._meta.fields]
    list_display_links = ["id"]
    search_fields = ["id"]
    list_filter = ["created_at", "updated_at", "deleted_at"]

    class Meta:
        model = Capacity
        