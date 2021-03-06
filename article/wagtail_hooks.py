from django.conf import settings
from django.utils.html import format_html
from wagtail.wagtailcore import hooks
from wagtail.wagtailcore.whitelist import attribute_rule


def blacklist_tag():
    def fn(tag):
        return tag.decompose()
    return fn


def unwrap_tag():
    def fn(tag):
        return tag.unwrap()
    return fn


@hooks.register('construct_whitelister_element_rules')
def whitelist_blockquote():
    return {
        'style': blacklist_tag(),
        'font': unwrap_tag(),
        'span': unwrap_tag(),
        'blockquote': attribute_rule({'class': True}),
        'p': attribute_rule({'class': True}),
        'h2': attribute_rule({'class': True}),
        'h3': attribute_rule({'class': True}),
        'h4': attribute_rule({'class': True}),
        'h5': attribute_rule({'class': True}),
        'iframe': attribute_rule({
            'style': True, 'src': True,
            'width': True, 'height': True
        }),
        'img': attribute_rule({
            'srcset': True, 'class': True,
            'alt': True, 'sizes': True,
            'width': True, 'height': True,
            'src': True
        }),
        'audio': attribute_rule({
            'class': True, 'src': True,
            'controls': True,
        }),
        'source': attribute_rule({
            'class': True,'src': True,
            'type': True,
        }),
    }

@hooks.register('insert_editor_js')
def editor_js():
    return format_html(
        """
        <script src="{0}article/js/slug.js"></script>
        <script>
            document.addEventListener("DOMContentLoaded", function() {{
                $('h2:contains("Content - Deprecated") ~ fieldset .hallo_rich_text_area .richtext').attr('contenteditable', false);
            }});
        </script>
        """,
        settings.STATIC_URL
    )

@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        """
        <link rel="stylesheet" href="{0}font-awesome/css/font-awesome.min.css">
        <link rel="stylesheet" href="{0}article/css/hallo-icons.css">
        <style>
        blockquote {{
	        color: #101010;
	        font-size: 1.6em;
	        border: none;
	        font-style: italic;
	        font-weight: bold;
	        margin: 10px 0;
	        padding: 10px;
	        text-align: center;
	        display: block;
        }}
        
        blockquote::before {{
            content: open-quote;
        }}
	    blockquote::after {{
	        content: close-quote;
        }}
        .center {{ text-align: center; }}
        .left {{ text-align: left; }}
        .right {{ text-align: right; }}
        .justify {{ text-align: justify; }}
        </style>
        """,
        settings.STATIC_URL
    )
