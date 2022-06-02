from django.shortcuts import render
from .models import Product, Contact, Orders, OrderUpdate
import json


# Create your views here.
def index(request):
    cat_wise_obj = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        cat_wise_obj.append(Product.objects.filter(category=cat))
    params = {
        'objs': cat_wise_obj
    }
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            desc=desc
        )
        contact.save()
        thank = True
        return render(request, "shop/contact.html", {'thank': thank})
    return render(request, "shop/contact.html")


def tracker(request):
    if request.method == "POST":
        item, order = [], None
        thank = True
        order_id = request.POST.get('order_id', '')
        email = request.POST.get('email', '')
        try:
            update = OrderUpdate.objects.filter(order_id=order_id, email=email)
            order = Orders.objects.filter(id=order_id)[0].items_json
            for items in update:
                item.append({'update': items.update_desc, 'time': items.timestamp})
        except IndexError:
            item = []
        if item:
            thank = False
            order = json.loads(order)
        return render(request, "shop/tracker.html", {'item': item, 'thank': thank, 'order': order})
    return render(request, "shop/tracker.html")


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    cat_wise_obj = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query.lower(), item)]
        print(prod)
        if len(prod) != 0:
            cat_wise_obj.append(prod)
    params = {'objs': cat_wise_obj, 'msg': ""}
    if not cat_wise_obj:
        params = {'msg': "Did'nt Find Something Relevant!"}
    return render(request, 'shop/search.html', params)


def productView(request, id):
    product = Product.objects.filter(id=id)[0]
    recommended = Product.objects.filter(category=product.category)
    return render(request, "shop/prodview.html", {'product': product, 'recommended': recommended, 'id': id})


def catWiseProductView(request, cat):
    subcat_wise_obj = []
    subcatprods = Product.objects.filter(category=cat)
    subcats = {item.subcategory for item in subcatprods}
    for cate in subcats:
        subcat_wise_obj.append(Product.objects.filter(subcategory=cate, category=cat))
    return render(request, "shop/categorywiseprodView.html", {'products': subcat_wise_obj, 'cat': cat})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('items_json', '')
        f_name = request.POST.get('firstName', '')
        l_name = request.POST.get('lastName', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        country = request.POST.get('country', '')
        state = request.POST.get('state', '')
        pincode = request.POST.get('zip', '')
        amount = float(request.POST.get('amount', ''))
        order = Orders(
            items_json=items_json,
            f_name=f_name,
            l_name=l_name,
            email=email,
            address=address,
            phone=phone,
            country=country,
            state=state,
            pincode=pincode,
            amount=amount,
        )
        order.save()
        update = OrderUpdate(
            order_id=order.id,
            update_desc="The order has been placed",
            email=email
        )
        update.save()
        order_id = order.id
        thank = True
        print(items_json)
        return render(request, "shop/checkout.html", {'id': order_id, 'thank': thank})
    return render(request, "shop/checkout.html")
