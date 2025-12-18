# Recamán Sequence — First 100 Terms & Visualization

## 📌 Overview

This repository contains a simple implementation of the **Recamán sequence**, along with a plot of its **first 100 terms**.

The Recamán sequence is a well-known integer sequence defined by a simple rule that produces surprisingly complex and chaotic behavior.

---

## 📖 Definition (Recamán’s sequence)

The sequence ( a(n) ) is defined as:

```
a(0) = 0

For n ≥ 1:

If a(n−1) − n > 0 and has not appeared before:
    a(n) = a(n−1) − n
Else:
    a(n) = a(n−1) + n
```


Each step attempts a **backward move** first.
If that move is invalid (negative or already used), the sequence moves **forward** instead.

---

## 🔢 First 100 Terms

The program generates the first **100 terms** of the sequence starting from 0.
These values are stored in a Python list and printed to the console.

Example (initial terms):

```
0, 1, 3, 6, 2, 7, 13, 20, 12, 21, ...
```

---

## 📈 Visualization

The sequence is visualized using **matplotlib**.

* **x-axis**: step number ( n )
* **y-axis**: value of the sequence ( a(n) )

This produces the characteristic **zig-zag / sawtooth pattern**, reflecting the alternation between backward and forward moves.

---

## 🛠️ Requirements

* Python 3.x
* NumPy
* Matplotlib

Install dependencies using:

```bash
pip install numpy matplotlib
```

---

## ▶️ How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/bit10-codes/recaman_sequence.git
   ```
2. Navigate to the project folder:

   ```bash
   cd recaman_sequence
   ```
3. Run the script:

   ```bash
   recaman_sequence.py
   ```

This will:

* Print the first 100 terms
* Display the plot of the sequence

---

## 📚 References

* Wikipedia: [https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence](https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence)

---

## ✨ Possible Extensions

* Animate the sequence
* Plot jumps on the number line
* Generate higher terms and study growth behavior

## 😉 Fun Fact

Neil Sloane has conjectured that every number eventually appears, but this has not been proven. As of 2018, 10^230 terms have been calculated, and 852,655 is the smallest natural number to not appear on the list.
