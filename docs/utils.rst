Utilities
=====

This is a collection of utility classes and functions that I've found useful in my projects. They are all written in C# and are designed to be used in the Scoutify projects.

Error Logging
------------

The `ErrorLogger` class is a simple class that logs errors to a file. It is designed to be used in a try-catch block to log any exceptions that are thrown. The class is static and has a single method, `LogError`, which takes an exception and a message as parameters. The exception is written to the log file along with the message and the current date and time.


File Utilities
------------

The `FileUtilities` class is a collection of static methods that perform various file operations. The class has methods for reading and writing text files, reading and writing binary files, and copying files. The class also has a method for creating a new directory if it does not already exist.