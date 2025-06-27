# AccoQuestion1
Django Signals: Synchronous Execution - Detailed Analysis
By default, Django signals are executed synchronously. When a signal is sent, all connected receivers are called immediately in the same thread, and the sender waits for all receivers to finish processing before continuing execution.
