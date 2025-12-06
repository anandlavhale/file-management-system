import sys
print("Python version:", sys.version)

try:
    import xlsxwriter
    print("✓ xlsxwriter imported successfully")
    print("  Version:", xlsxwriter.__version__)
except ImportError as e:
    print("✗ xlsxwriter import failed:", e)

try:
    import django
    print("✓ Django imported successfully")
    print("  Version:", django.__version__)
except ImportError as e:
    print("✗ Django import failed:", e)

try:
    from records.views import export_to_excel
    print("✓ export_to_excel function imported successfully")
except Exception as e:
    print("✗ export_to_excel import failed:", e)

print("\nAll dependencies are properly installed!")
