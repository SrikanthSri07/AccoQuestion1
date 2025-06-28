from django.dispatch import Signal, receiver
import time

# Create a custom signal
test_signal = Signal()

@receiver(test_signal)
def slow_receiver_1(sender, **kwargs):
    print("Receiver 1 starting - will take 3 seconds")
    time.sleep(3)
    print("Receiver 1 finished")

@receiver(test_signal)
def slow_receiver_2(sender, **kwargs):
    print("Receiver 2 starting - will take 2 seconds")
    time.sleep(2)
    print("Receiver 2 finished")

def send_test_signal():
    print("Sending signal...")
    test_signal.send(sender=None)
    print("Signal sending complete")