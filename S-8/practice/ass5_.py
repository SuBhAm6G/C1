# Write code that attempts to import a non-existent module and gracefully handles the import error by printing an error message.
try:
    import not_an_module
except:
    print("Error: Module not found.")