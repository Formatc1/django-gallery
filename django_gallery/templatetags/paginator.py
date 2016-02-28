from django import template

register = template.Library()


@register.filter(name='page_filter')
def page_filter(pages_iter, actual_page):
    margin = 2
    num_pages = len(pages_iter)

    pages = []
    if actual_page - margin < 3:
        pages += list(range(1, actual_page))
    else:
        pages += [1, None]
        pages += list(range(actual_page - margin, actual_page))

    if actual_page + margin > num_pages - 2:
        pages += list(range(actual_page, num_pages + 1))
    else:
        pages += list(range(actual_page, actual_page + margin + 1))
        pages += [None, num_pages]

    return pages
