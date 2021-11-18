# Hack the school
Scripts help Ivan hack his class school journal. Scripts only work from Django shell.

## Using
1. Open your Django shell by
    ```
    python manage.py shell
    ```
2. Copy full scripts' texts and paste them in the Django shell.
3. Use all 3 available functions.

## fix_marks
Fix bad marks to A grade of one schoolkid.

Input: 
* schoolkid - Schoolkid object.

Return: None
## remove_chastisements
Remove bad words about ont schoolkid

Input: 
* schoolkid - Schoolkid object.

Return: None
## create_commendation
Get child name, find it in DB. 

If there is not person with this name show message about it and stop the script. 
If there are many of them, say about it and stop the script.

Choose a random lesson of the class. Choose a random commendation. Create new commendation and save it in DB.

Input:
* child_name - str, part of the search name
* subject_name - str, exact name of the subject

Return: None