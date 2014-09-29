from copy import deepcopy
from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost

from .models import BannerImage

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(-2, "banner_image")


class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets


class BannerImageAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)
admin.site.register(BannerImage, BannerImageAdmin)
