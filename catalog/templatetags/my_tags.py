from django import template

register = template.Library()


@register.filter()
def show_img(img_url):
    if img_url:
        return f'/media/{img_url}'
    return "#"
