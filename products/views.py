from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CommentForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.author = request.user
            comment.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = CommentForm()

    context = {
        'product': product,
        'comments': comments,
        'form': form,
    }
    return render(request, 'products/product_detail.html', context)
