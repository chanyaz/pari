import factory
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from wagtail.wagtailcore.models import Page


class ContentTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContentType
        django_get_or_create = ('app_label', 'model')

    app_label = "wagtailcore"
    model = "page"


class PageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Page
        django_get_or_create = ('title', 'path')

    path = factory.Sequence(lambda n: u'0001000{}'.format(n))  # 00010003
    depth = 2
    numchild = 0
    title = "Peoples Archive of rural india"
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    live = True
    has_unpublished_changes = False
    seo_title = " "
    show_in_menus = False
    search_description = " "
    go_live_at = '2011-10-24 12:43'
    expire_at = '2050-12-31 12:43'
    expired = False
    content_type = factory.SubFactory(ContentTypeFactory)
    locked = False
    latest_revision_created_at = '2011-10-24 12:43'
    first_published_at = '2011-10-24 12:43'

    @classmethod
    def _setup_next_sequence(cls):
        return getattr(cls, 'starting_seq_num', 3)
