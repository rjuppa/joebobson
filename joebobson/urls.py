from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap
from filebrowser.sites import site
from joebobson import settings
from joeblog.views import index, contact

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}

blog_urls = [
    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^blog/tags/', include('zinnia.urls.tags')),
    url(r'^blog/feeds/', include('zinnia.urls.feeds')),
    url(r'^blog/random/', include('zinnia.urls.random')),
    url(r'^blog/authors/', include('zinnia.urls.authors')),
    url(r'^blog/categories/', include('zinnia.urls.categories')),
    url(r'^blog/comments/', include('zinnia.urls.comments')),
    url(r'^blog/', include('zinnia.urls.entries')),
    url(r'^blog/', include('zinnia.urls.archives')),
    url(r'^blog/', include('zinnia.urls.shortlink')),
    url(r'^blog/', include('zinnia.urls.quick_entry')),
    url(r'^contact/', index, name='index')
]


urlpatterns = patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/tinymce/', include('tinymce.urls')),
    url(r'^tinymce/zinnia/', include('zinnia_tinymce.urls')),
    url(r'^', include(blog_urls, namespace='zinnia')),

)

urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': sitemaps}),)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)