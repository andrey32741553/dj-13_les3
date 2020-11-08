from django import template
from datetime import datetime
import time


register = template.Library()


@register.filter
def format_date(value):
    time_diff = (int(time.time()) - int(value)) / 60
    if time_diff < 10:
        return 'только что'
    elif time_diff < 1440:
        return f'{int(time_diff / 60)} часов назад'
    elif time_diff >= 1440:
        return datetime.fromtimestamp(value).strftime('%Y-%m-%d')


@register.filter
def format_rating(value):
    if value < -5:
        return 'всё плохо'
    elif -5 <= value <= 5:
        return 'нейтрально'
    elif value > 5:
        return 'хорошо'


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'оставьте комментарий'
    elif 0 < value <= 50:
        return value
    else:
        return '50+'

@register.filter
def format_selftext(value, count: int):
    text = value.split(' ')
    if len(text) <= count * 2:
        return f"{' '.join(text)}"
    else:
        return f"{' '.join(text[:count])} ... {' '.join(text[-count:])}"
