Курс Алгоритмы и структуры данных
------
### Введение в алгоритмы

<details><summary> D. Хаотичность погоды  </summary>

**[code_d.py](https://github.com/lazy-stuff/algorithms_course/blob/main/sprint_1/code_d.py)**

Метеорологическая служба вашего города решила исследовать погоду новым способом.
Под температурой воздуха в конкретный день будем понимать максимальную температуру в этот день.
Под хаотичностью погоды за n дней служба понимает количество дней, в которые температура строго больше, чем в день до (если такой существует) и в день после текущего (если такой существует). Например, если за 5 дней максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов, то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот период.
Заметим, что если число показаний n=1, то единственный день будет хаотичным.

**Формат ввода**

В первой строке дано число n –— длина периода измерений в днях, 1 ≤ n≤ 105. Во второй строке даны n целых чисел –— значения температуры в каждый из n дней. Значения температуры не превосходят 273 по модулю.

**Формат вывода**

Выведите единственное число — хаотичность за данный период.

</details>

<details><summary> F. Палиндром </summary>

**[code_f.py](https://github.com/lazy-stuff/algorithms_course/blob/main/sprint_1/code_f.py)**

**Формат ввода**

В единственной строке записана фраза или слово. Буквы могут быть только латинские. Длина текста не превосходит 20000 символов.
Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.

**Формат вывода**

Выведите «True», если фраза является палиндромом, и «False», если не является.
</details>

<details><summary> H. Двоичная система </summary>

**[code_h.py](https://github.com/lazy-stuff/algorithms_course/blob/main/sprint_1/code_h.py)**

Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести их сумму, также в двоичной системе. Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя. Помогите Гоше решить задачу.
Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе.

**Формат ввода**

Два числа в двоичной системе счисления, каждое на отдельной строке. Длина каждого числа не превосходит 10 000 символов.
**Формат вывода**

Одно число в двоичной системе счисления.
</details>
<details><summary> J. Факторизация </summary>

**[code_j.py](https://github.com/lazy-stuff/algorithms_course/blob/main/sprint_1/code_j.py)**

Напишите программу, которая производит факторизацию переданного числа.
**Формат ввода**

В единственной строке дано число n (2 ≤ n ≤ 109), которое нужно факторизовать.
**Формат вывода**

Выведите в порядке неубывания простые множители, на которые раскладывается число n.
</details>
<details><summary> K. Списочная форма </summary>

**[code_k.py](https://github.com/lazy-stuff/algorithms_course/blob/main/sprint_1/code_k.py)**

Число К не превосходят 10000. Длина числа Х не превосходит 1000.
Нужно вернуть списочную форму числа X + K.
**Формат ввода**

В первой строке — длина списочной формы числа X. На следующей строке — сама списочная форма с цифрами записанными через пробел.
В последней строке записано число K, 0 ≤ K ≤ 10000.
**Формат вывода**

Выведите списочную форму числа X+K.
</details>
<details><summary> L. Лишняя буква </summary>

**[code_L.py](https://github.com/lazy-stuff/algorithms_course/blob/main/sprint_1/code_L.py)**

**Формат ввода**

На вход подаются строки s и t, разделённые переносом строки. Длины строк не превосходят 1000 символов. Строки не бывают пустыми.
**Формат вывода**

Выведите лишнюю букву.

Выведите списочную форму числа X+K.
</details>
<details><summary> A. Ближайший ноль </summary>

**[closest_zero.py](https://github.com/lazy-stuff/algorithms_course/blob/main/sprint_1/closest_zero.py)**

**Формат ввода**

В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль. Номера домов (положительные числа) уникальны и не превосходят 109.
**Формат вывода**

Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.
</details>
<details><summary> B. Ловкость рук </summary>

**[dexterity_game.py](https://github.com/lazy-stuff/algorithms_course/blob/main/sprint_1/dexterity_game.py)**

**Формат ввода**

В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой строке. Каждый символ —– либо точка, либо цифра от 1 до 9. Символы одной строки идут подряд и не разделены пробелами.
**Формат вывода**

Выведите единственное число –— максимальное количество баллов, которое смогут набрать Гоша и Тимофей.
</details>