from django.http import HttpResponse
import threading
from .models import Book

def create_book(request):
    current_thread = threading.current_thread()
    print(f"\n[VIEW] Running in thread: {current_thread.name} (ID: {current_thread.ident})")
    
    print("[VIEW] Creating book...")
    book = Book.objects.create(title="Django Signals", author="Python Dev")
    
    print("[VIEW] Book created, continuing execution")
    return HttpResponse("Check your console for thread information")