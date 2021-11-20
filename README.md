# Hack the school
Scripts help Ivan hack his class school journal. Scripts only work from Django shell.

## Using
1. Copy `scripts.py` file to main directory of your [Django project](https://github.com/devmanorg/e-diary/tree/master)
2. Open your Django shell
    ```
    python manage.py shell
    ```
3. Import scripts in console
   ```
   imprt scripts
   ```
4. Use functions
## fix_marks
Fix bad marks to A grade of one schoolkid.

Input: 
* schoolkid - Schoolkid object.

Return: None

### Using
1. Select a child by using a Django ORM
   ```
   child = Schoolkid.objects.filter(full_name="FULL NAME").first()
   ```
   Replace `FULL NAME` with your choice
2. Use child as `schoolkid` for function
   ```
   scripts.fix_marks(child)
   ```
3. If you did everything right, it shows you a message
   ```
   Success! You are an excellent student!
   ```
## remove_chastisements
Remove bad words about ont schoolkid

Input: 
* schoolkid - Schoolkid object.

Return: None
### Using
1. Select a child by using a Django ORM
   ```
   child = Schoolkid.objects.filter(full_name="FULL NAME").first()
   ```
   Replace `FULL NAME` with your choice
2. Use child as `schoolkid` for function
   ```
   scripts.remove_chastisements(child)
   ```
3. If you did everything right, it shows you a message
   ```
   Success! You are a student w/o problems!
   ```
## create_commendation
Get child name, find it in DB. 

If there is no person with this name show message about it and stop the script. 
If there are many of them, say about it and stop the script.

Choose a random lesson of the class. Choose a random commendation. Create new commendation and save it in DB.

Input:
* child_name - str, part of the search name
* subject_name - str, exact name of the subject

Return: None
### Using
1. Easy peasy! Just use this command
   ```
   scripts.create_commendation("FULL NAME", "SUBJECT NAME")
   ```
   Replace `FULL NAME` with the full name of the student and `SUBJECT NAME` with the name of the subject.

   Example:
   ```
   scripts.create_commendation("Фролов Иван", "Математика")
   ```
2. The answer will be smth like this:
   ```
   "Фролов Иван Григорьевич 6А" received an commendation "Я поражен!" for the subject Математика 6 класса on 2019-04-01
   ```