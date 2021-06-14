from django.contrib import admin

# Register your models here.
from .models import Question, Choice


admin.site.register(Choice)

# Register custom actions
@admin.action(description='Mark selected question as active')
def make_active(modeladmin, request, queryset):
    queryset.update(active=True)

@admin.action(description='Mark selected question as inactive')
def make_inactive(modeladmin, request, queryset):
    queryset.update(active=False)

class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('question_text',)}
    #fields = ('pub_date','question_text')
    list_display = ('id','pub_date','question_text')
    actions = [make_active,make_inactive]
    ordering = ['-pub_date','-active']

admin.site.register(Question, QuestionAdmin)