from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time
from .models import Book

@receiver(post_save, sender=Book)
def log_book_creation(sender, instance, created, **kwargs):
    if created:
        current_thread = threading.current_thread()
        print(f"\n[SIGNAL] Running in thread: {current_thread.name} (ID: {current_thread.ident})")
        print(f"[SIGNAL] Processing new book: {instance}")
        time.sleep(3)  # Simulate heavy processing
        print("[SIGNAL] Finished processing\n")