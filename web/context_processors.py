from web.models import *

def categorys(request):
    if request.user.is_authenticated():
        list_categorys = category.objects.filter(created_by=request.user)
    else:
        list_categorys = []
    return {
        'list_categorys': list_categorys
    }