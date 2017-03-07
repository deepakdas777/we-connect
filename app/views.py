from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Item,Comment
from .forms import ItemForm, UserForm, CommentForm, LikesForm,UnlikeForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views.generic import View
from django.contrib import messages

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
@login_required
def item_list(request):
    items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/item_list.html', {'items': items})
@login_required
def add_comment_to_post(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.item = item
            comment.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = CommentForm()
    return render(request, 'app/add_comment_to_post.html', {'form': form})
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('item_detail', pk=comment.item.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    item_pk = comment.item.pk
    comment.delete()
    return redirect('item_detail', pk=item_pk)
@login_required
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'app/item_detail.html', {'item': item})

def register(request):
    items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return render(request, 'registration/login.html', {'items': items})

    else:
        form = UserForm()
    return render(request, 'app/register.html', {'form': form})        


@login_required
def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.image = request.FILES['image']
            file_type = item.image.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'item': item,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'app/item_edit.html', context)
            item.published_date = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'app/item_edit.html', {'form': form})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.user != request.user :
        messages.success(request, "Post owned by another user, You are having read permission only")
        return render(request,"app/denied.html",{})
    else:
        if request.method == "POST":
            form = ItemForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user
                item.image = request.FILES['item_logo']
                file_type = item.image.url.split('.')[-1]
                file_type = file_type.lower()
                if file_type not in IMAGE_FILE_TYPES:
                    context = {
                        'item': item,
                        'form': form,
                        'error_message': 'Image file must be PNG, JPG, or JPEG',
                    }
                
                    return render(request, 'app/item_edit.html', context)
                item.published_date = timezone.now()
                item.save()
                return redirect('item_detail', pk=item.pk)
        else:
            form = ItemForm(instance=item)
        return render(request, 'app/item_edit.html', {'form': form})

@login_required
def item_draft_list(request):
    items = Item.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'app/item_draft_list.html', {'items': items})

@login_required
def item_publish(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.publish()
    return redirect('item_detail', pk=pk)

@login_required
def item_remove(request, pk):
    
    item = get_object_or_404(Item, pk=pk)
    if item.user == request.user :
        item.delete()
        return redirect('item_list')        

    else:
        messages.success(request, "Post owned by another user, You are having read permission only")
        return render(request,"app/denied.html",{}) 
@login_required
def add_likes_to_post(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = LikesForm(request.POST)
        if form.is_valid():
            likes = form.save(commit=False)
            likes.user = request.user
            likes.item = item
            likes.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = LikesForm()
    return render(request, 'app/add_likes_to_post.html', {'form': form})
@login_required
def unlike_post(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = UnlikeForm(request.POST)
        if form.is_valid():
            unlike = form.save(commit=False)
            unlike.user = request.user
            unlike.item = item
            unlike.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = UnlikeForm()
    return render(request, 'app/unlike_post.html', {'form': form})
