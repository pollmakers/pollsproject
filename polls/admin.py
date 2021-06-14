from django.contrib import admin

# Register your models here.
from .models import Question, Choice


admin.site.register(Choice)
@admin.action(description='Mark selected question as active')
def make_active(modeladmin, request, queryset):
    queryset.update(active=True)

@admin.action(description='Mark selected question as inactive')
def make_inactive(modeladmin, request, queryset):
    queryset.update(active=False)

class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('question_text',)}
    #fields = ('pub_date','question_text')
    list_display = ('id','active','pub_date','question_text')
    actions = [make_active,make_inactive]
    #actions_selection_counter = True
    ordering = ['-pub_date','-active']

admin.site.register(Question, QuestionAdmin)

