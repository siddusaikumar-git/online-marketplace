from django.shortcuts import render, get_object_or_404

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)