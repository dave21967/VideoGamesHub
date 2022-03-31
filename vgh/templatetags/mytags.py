from django import template

register = template.Library()

def split(string, key):
    return string.split(key)

register.filter("split", split)