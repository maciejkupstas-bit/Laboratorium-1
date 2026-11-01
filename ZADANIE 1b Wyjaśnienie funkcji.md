## Wyjaśnienie operatorów z Zadania 1A

- `+` dodaje liczby. Gdy oba argumenty są całkowite, wynik ma typ `int`; jeśli któryś jest ułamkowy, wynik ma typ `float`.
- `/` wykonuje zwykłe dzielenie. W Pythonie wynik jest typu `float`, nawet gdy dzielenie wychodzi bez reszty, np. `4 / 2` daje `2.0`.
- `//` wykonuje dzielenie całkowite i zaokrągla iloraz w dół. Dlatego `3 // 2` daje `1`, a `-3 // 2` daje `-2`.
- `%` zwraca resztę z dzielenia. W `11 % 2` reszta wynosi `1`.
- `**` oznacza potęgowanie. Na przykład `2 ** 10` daje `1024`.
- Znak `-` przed liczbą, jak w `-3`, zmienia jej znak na przeciwny.
- Nawiasy w `8 ** (1 / 3)` wskazują, że najpierw obliczamy wykładnik `1 / 3`. Potęgowanie 8 do tej potęgi odpowiada wyciągnięciu pierwiastka sześciennego z 8.

Funkcja `type(x)` nie jest operatorem. Sprawdza typ wartości `x`, np. `int` (liczba całkowita) lub `float` (liczba zmiennoprzecinkowa).

W części 1B sprawdzane są konwersje typów: `int()` zamienia wartość na liczbę całkowitą, `float()` na zmiennoprzecinkową, `str()` na tekst, a `bool()` na wartość logiczną (`True` albo `False`). Na przykład `bool(0)` daje `False`.