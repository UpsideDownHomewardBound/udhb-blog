from copy import deepcopy
from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost
from mezzanine.pages.models import Page, RichTextPage
from mezzanine.pages.admin import PageAdmin

from .models import Theme

page_fieldsets = deepcopy(PageAdmin.fieldsets)
page_fieldsets[0][1]['fields'].insert(-2, "theme")

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(-2, "theme")


class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets

class MyPageAdmin(PageAdmin):
    fieldsets = page_fieldsets

admin.site.unregister(Page)
admin.site.register(Page, MyPageAdmin)

admin.site.unregister(RichTextPage)
admin.site.register(RichTextPage, MyPageAdmin)


class ThemeAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)
admin.site.register(Theme, ThemeAdmin)
