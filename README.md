# Aplikacja-sklepu-Python-
Aplikacja sklepu odpowiedzialna za edytowanie bazy danych przez administratora oraz za wykonywanie prowizorycznej sumy zakupów, poprzez podawanie kodu oraz wagi produktu.
Aplikacja działa w połączeniu pracy GUI wraz z konsolą, w przyszłości będzie opierać się tylko na wykorzystaniu GUI oraz zostanie rozwinięta o nowe funkcje dla użytkownika jak i admina.

Objaśnienie za co odpowiadają dane kody:

"Main.py":
- Egzekwowanie wcześniej zadeklarowanych klas menu oraz przechodzenie między nimi
- Sprawdzanie statusu logowania Admina

"menu_classes.py":
- klasy odpowiedzialne za tworzenie GUI kolejnych menu sklepu
- metody egzekwujące funkcje z pliku "exectute_fun.py"

"execute_fun.py":
- funkcje odpowiedzialna za dodawanie nowego produktu  do bazy danych "dane.txt" oraz usuwanie istniejącego
- funkcja odpowiedzialna za obliczanie wyniku zakupów dodawwanych przez użytkownika

"making_object.py":
- tworzenie obiektu na podstawie rekordów z pliku "dane.txt", posiadające swój kod, nazwę i cenę
- tworzenie listy wyżej wspomnianych obiektów

"dane.txt":
- plik tekstowy przedstawiający poszczególne produkty
