from re import sub, search

from django import template
from django.utils.html import urlize
from django.conf import settings

register: template.Library = template.Library()

DOMAIN_NAME: str = getattr(settings, 'DOMAIN_NAME')
WEB_PROTO: str = getattr(settings, 'WEB_PROTO')

@register.filter
def strip_markdown(value: str) -> str:
    """
    Removes all instances of markdown format
    from a given string.
    """
    return (value
        .replace('_ _', ''
        ).replace('`', ''
        ).replace('**', ''
        ).replace('~~', ''
        ).replace('__', ''))

@register.filter
def strip_tags(value):
    """
    Removes all instances of unformatted Discord
    usernames and channels from a given string, as
    well as convert .gg urls to .com.
    
    This will also remove any HTML tags present.
    """
    cleaned_value = sub(r'<.*?>', '', value)

    return (cleaned_value
        .replace('@everyone', ''
        ).replace('▬', ''
        ).replace('.gg', '.com'))

@register.filter
def https_to_discord(value):
    """
    Changes instances of "https://discord" to 
    "discord://discord" to force the link to open
    in the Discord App if installed. Will make all
    anchor targets be "_blank" to open in new tab.
    Runs default "urlize" filter internally before
    modification
    """
    initial = sub(r'https://discord', 'discord://discord', urlize(value))
    anchor = search(r'<a href="\S+"\S+>', initial)
    
    if anchor:
        blank_anchor = anchor.group(0).replace('<a', '<a target="_blank"')
        anchor_end = search(r'</a>', initial)
        anchor_end_icon = anchor_end.group(0
            ).replace('</a>', (f' <img class="new_tab_icon" '
                            f'src="{WEB_PROTO}://{DOMAIN_NAME}'
                            '/static/image/new_tab_black.svg"></a>'))
        return (initial
            .replace(anchor.group(0), blank_anchor)
            .replace(anchor_end.group(0), anchor_end_icon))
    
    return initial
