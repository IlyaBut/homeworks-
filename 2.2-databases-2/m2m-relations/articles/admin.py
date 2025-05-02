from django.contrib import admin

from articles.models import Article,Tag, Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class RelationshipInlineFormSet(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') is True:
                count +=1
            if count > 1:
                raise ValidationError("is_main должен быть только один тег")
            elif count == 0:
                raise ValidationError("Назначте is_main")

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 8
    formset = RelationshipInlineFormSet

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


