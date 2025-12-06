# Bug Fix: Upload Form Not Working

## Problem
When submitting the upload form (description + file), the data was not being saved to the database and no new rows appeared in the table.

## Root Cause
The upload form on the main page was posting to `/` (the list page), but the `list_records` view **did not handle POST requests**. It only handled GET requests for searching/filtering.

The form submission was being silently ignored because:
1. The `list_records` view only processed GET parameters (search, filters, pagination)
2. It never checked for `request.method == 'POST'`
3. The upload logic was in a separate `upload_record` view at `/upload/`, but the form wasn't posting to that URL

## Solution Applied

### 1. Modified `records/views.py` - `list_records()` function
**Before:** Only handled GET requests
**After:** Now handles both GET and POST requests
- Added `if request.method == 'POST':` block at the beginning
- When POST: Binds form with `request.POST` and `request.FILES`
- Validates with `form.is_valid()`
- Saves with `form.save()`
- Displays errors or redirects on success

### 2. Updated `records/templates/records/list.html`
**Fixed label 'for' attributes:**
- Changed `for="description"` to `for="id_description"` 
- Changed `for="file"` to `for="id_file"`

Django auto-generates IDs with the `id_` prefix, so labels must match.

## How It Works Now

### Upload Flow:
1. User fills in description and selects a file
2. Clicks "Upload File" button
3. Form submits POST to `/` (list_records view)
4. `list_records` view receives POST request
5. Creates `FileRecordForm(request.POST, request.FILES)`
6. If valid: calls `form.save()` → saves to database
7. Shows success message
8. Redirects back to list page
9. New record immediately appears in the table

### Error Handling:
- If description is empty: Shows error message
- If no file selected: Shows error message  
- If file > 10MB: Shows error message
- Errors persist form and show in red text

## Files Modified
- `records/views.py` - Added POST handling to `list_records()`
- `records/templates/records/list.html` - Fixed label `for` attributes

## Testing the Fix

1. Restart the Django server
2. Go to http://localhost:8000/
3. Fill in the upload form:
   - Description: "Test Document"
   - File: Select any file (PDF, image, etc.)
4. Click "Upload File"
5. You should see a success message
6. A new row should immediately appear in the table

## Why the Previous Code Didn't Work

The `upload_record` view in urls.py was unused because:
- The form's action attribute wasn't set to `/upload/`
- It defaulted to posting to the current page `/`
- But that view didn't handle POST requests

The fix simplifies this by having the main list page handle uploads directly, which is also better UX since users stay on the same page.

## Related Files (unchanged but relevant)
- `records/forms.py` - FileRecordForm (already correct)
- `records/models.py` - FileRecord model (already correct)
- `records/urls.py` - URL configuration (already correct)
