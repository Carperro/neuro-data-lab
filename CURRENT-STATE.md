# CURRENT STATE — neuro-data-lab

## Date

2026-09-01

## Current Level

LEVEL 1 — Python Fundamentals

## Current Focus

Dictionaries → Functions → Integration

---

## Learning Progress

### Python fundamentals completed/practiced

* Variables
* Data types
* Input
* Arithmetic operators
* Comparison operators
* Logical operators
* Conditionals
* Loops
* Lists
* Indexing
* Negative indexing
* Slicing
* Strings
* String methods
* `lower()`
* `strip()`
* `replace()`
* `split()`
* `enumerate()`
* `continue`
* `in`
* `==`
* Counters
* Sets
* Dictionaries
* Dictionary keys
* Dictionary values
* Dictionary indexing
* Dictionary mutation
* Basic data cleaning

---

## Concepts Currently Being Consolidated

### Dictionaries

Understand that a dictionary stores relationships between:

```text
key → value
```

Example:

```python
neuron_counts = {
    "excitatory": 0,
    "inhibitory": 0,
    "sensory": 0
}
```

Important concepts understood:

```python
neuron_counts["inhibitory"]
```

accesses a value.

```python
neuron_counts["inhibitory"] += 1
```

modifies the stored value.

A dictionary can therefore act as multiple counters without requiring a separate counter variable for every category.

Dynamic key access:

```python
neuron = "inhibitory"

neuron_counts[neuron] += 1
```

---

## Last Exercise

### Exercise 2.5 — Dictionary Basics

Created a dictionary containing neuron types with initial values of `0`.

Practiced:

1. Creating a dictionary.
2. Accessing a value through its key.
3. Understanding that accessing a value does not modify it.
4. Modifying a dictionary value with `+=`.
5. Understanding the difference between evaluating/printing an expression and mutating stored data.

---

## Next Exercise

### Exercise 23 — Unique Neuron Types Counter

Input:

```python
neural_data = " EXCITATORY, inhibitory, sensory, motor, inhibitory, sensory, excitatory, motor, inhibitory "
```

Goal:

Create a dictionary counting the occurrences of each neuron type.

Expected conceptual result:

```python
{
    "excitatory": 2,
    "inhibitory": 3,
    "sensory": 2,
    "motor": 2
}
```

Important concepts to reason through:

* `split()`
* `strip()`
* `lower()`
* `for`
* dictionary membership with `in`
* dictionary indexing
* incrementing dictionary values
* using a dictionary as a collection of counters

Do NOT jump immediately to the solution. Reason through the algorithm first.

---

## Previous Important Learning

### Strings

Learned:

* Strings use zero-based indexing.
* Negative indexes access characters from the end.
* Slicing follows `start:end`, with `start` included and `end` excluded.
* `len(string) - 1` gives the last valid index.
* Strings are immutable.
* String methods generally return new strings.
* Method chaining passes the result of one method into the next method.
* `.strip()` removes surrounding whitespace, not internal whitespace.
* `.replace()` replaces occurrences throughout the string.
* `.split()` converts a string into a list.
* `enumerate()` provides index + element.
* `continue` skips the current iteration.
* `in` checks membership/containment.
* `==` checks equality.

### Sets

Learned:

* Sets automatically remove duplicate values.
* `set(clean_neurons)` creates a new set.
* Creating a set does not modify the original list unless the result is assigned or otherwise used.

### Data Cleaning Pipeline

Established the conceptual pipeline:

```text
raw data
    ↓
split
    ↓
list
    ↓
loop
    ↓
clean each element
    ↓
clean list
    ↓
set / dictionary / analysis
```

---

## Current Project Structure

```text
neuro-data-lab/
├── README.md
│
├── 01_foundations/
│   └── python/
│       ├── 01_variables.py
│       ├── 02_conditionals.py
│       ├── 03_variables_and_conditionals_exercises.py
│       ├── 04_loops.py
│       ├── 05_lists.py
│       ├── 06_exercises_01.py
│       ├── 07_strings.py
│       └── 08_data_structures.py
│
└── CURRENT_STATE.md
```

---

## Learning Methodology

Core process:

```text
UNDERSTAND
    ↓
REASON
    ↓
WRITE
    ↓
TEST
    ↓
DEBUG
    ↓
APPLY
    ↓
INTEGRATE
```

Priority:

```text
Understanding > Speed
Reasoning > Memorization
Practice > Passive consumption
Integration > Isolated topics
Building > Copying
```

The tutor should avoid immediately providing complete solutions.

When possible:

1. Ask what I think should happen.
2. Identify the concepts involved.
3. Let me propose the code.
4. Review the reasoning.
5. Let me correct mistakes.
6. Provide the full solution only when appropriate.

---

## Integrated Study Roadmap

```text
Python
   ↓
Mathematics
   ↓
Statistics
   ↓
Data Science
   ↓
Scientific Python
   ↓
Neuroscience
   ↓
Neurodata
```

### Python

Fundamentals
→ Functions
→ Integration
→ Files
→ Modules
→ Data
→ Intermediate Python
→ Advanced Python

### Mathematics

Algebra
→ Functions
→ Graphs
→ Limits
→ Derivatives
→ Integrals
→ Linear Algebra

### Statistics

Probability
→ Random Variables
→ Distributions
→ Descriptive Statistics
→ Correlation
→ Sampling
→ Inferential Statistics

### Data Science

NumPy
→ Pandas
→ Matplotlib
→ Jupyter
→ Data Cleaning
→ Exploratory Data Analysis
→ Machine Learning

### Neuroscience

Use neuroscience progressively as the application domain for programming, mathematics, statistics and data analysis.

---

## Technical English

Continue progressively using English for:

* variables
* filenames
* function names
* comments
* technical terminology

Main explanations remain in Spanish.

---

## Git Status

The project is maintained with Git/GitHub.

Preferred commit style:

```text
Add Python variables fundamentals
Add Python conditionals fundamentals
Add variables and conditionals exercises
Add loop and conditional integration exercises
Add string manipulation and data cleaning exercises
```

### Before sleeping

Commit and push the current work, including this `CURRENT_STATE.md`.

---

## Next Session

Start by reviewing the last dictionary exercise briefly and continue with:

```text
Dictionary Basics
        ↓
Dictionary Counter Exercise
        ↓
Functions
        ↓
Function + previous concepts integration
```

Do not restart Python fundamentals.

Continue from the current level.

---

## Learning Momentum

The student is progressing quickly through Python fundamentals and is increasingly reasoning about code before writing it.

A particularly important recent transition is understanding dictionaries not merely as containers of data, but as structures that can represent relationships and maintain multiple dynamic counters.

Next objective: consolidate this mental model before moving into functions.
