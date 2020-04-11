from django import template
register = template.Library()

# register function as a decorator (if no name assigned, uses function name)
#@register.filter(name='cutout')
@register.filter()
def cutout(value,arg):
    #cuts out all values of arg from string
    return value.replace(arg,'')

#register.filter('cutout',cutout)
