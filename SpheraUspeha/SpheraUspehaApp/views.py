from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, TlgrmUser
from .forms import orderForm
import telebot
from .TlgrmBot import TOKEN



class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'SpheraUspehaApp/index.html', context={
            'page_obj': page_obj
        })

class Product(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        ads = Post.objects.all()[:5]
        return render(request, 'SpheraUspehaApp/product.html', context={
            'post': post,
            'ads': ads
        })

class OrderView(View):
    def get(self, request, *args, **kwargs):
        form = orderForm()
        return render(request, 'SpheraUspehaApp/order.html', context={
            'form': form,
            'title': 'Сделать заказ'
        })

    def post(self, request, *args, **kwargs):
        bot = telebot.TeleBot(TOKEN)
        form = orderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']
            tlgrmUsers = TlgrmUser.objects.all()
            for tlgrmUser in tlgrmUsers:
                bot.send_message(tlgrmUser.tlgrmUser, f'Получена заявка на обратный звонок. \nИмя:{name} \nЭл.почта: {email} \nНомер телефона: {number} \nКомментарий: {message}')
            return render(request, 'SpheraUspehaApp/thank.html')

class thankView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'SpheraUspehaApp/thank.html')

class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        resultOfSearch = ''
        if query:
            resultOfSearch = Post.objects.filter(
                Q(h1__icontains=query) | Q(content__icontains=query) | Q(description__icontains=query)
            )
        return render(request, 'SpheraUspehaApp/search.html', context={
            'posts': resultOfSearch,
	    'count': len(resultOfSearch)
        })