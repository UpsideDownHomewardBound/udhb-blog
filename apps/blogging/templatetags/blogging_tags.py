from mezzanine import template
from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.generic.models import Keyword
from apps.gallery.models import Album

register = template.Library()


@register.as_tag
def recent_content(limit=5, tag=None, username=None, category=None):
    """
    Put a list of recently published blog posts into the template
    context. A tag title or slug, category title or slug or author's
    username can also be specified to filter the recent posts returned.
    Usage::
        {% blog_recent_posts 5 as recent_posts %}
        {% blog_recent_posts limit=5 tag="django" as recent_posts %}
        {% blog_recent_posts limit=5 category="python" as recent_posts %}
        {% blog_recent_posts 5 username=admin as recent_posts %}
    """
    blog_posts = BlogPost.objects.published().select_related("user")
    title_or_slug = lambda s: Q(title=s) | Q(slug=s)
    if tag is not None:
        try:
            tag = Keyword.objects.get(title_or_slug(tag))
            blog_posts = blog_posts.filter(keywords__keyword=tag)
        except Keyword.DoesNotExist:
            return []
    if category is not None:
        try:
            category = BlogCategory.objects.get(title_or_slug(category))
            blog_posts = blog_posts.filter(categories=category)
        except BlogCategory.DoesNotExist:
            return []
    if username is not None:
        try:
            author = User.objects.get(username=username)
            blog_posts = blog_posts.filter(user=author)
        except User.DoesNotExist:
            return []
    blog_post_list = list(blog_posts[:limit])
    albums = list(Album.objects.order_by('most_recent_image_taken')[:limit])
    all_content_candidates = blog_post_list + albums
    for c in all_content_candidates:
        print c, c.created
    latest_content = sorted(all_content_candidates, key=lambda c: c.created, reverse=True)[:limit]
    return latest_content
