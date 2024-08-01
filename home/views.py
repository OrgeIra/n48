# home/views.py
from django.shortcuts import render


from products.models import Category

def home_view(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def detail(request):
    return render(request, 'detail.html')

def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = CommentModelForm(request.Post)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', product_id=product.id)

    else:
        form = CommentModelForm()

    return render(request, 'detail.html', {'form': form})
