# CURRENT STATE — neuro-data-lab
## Date
2026-09-04
## Current Level
LEVEL 1 — Python Fundamentals
## Current Focus
Functions → Integration → Mathematical Reasoning
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
* Nested dictionaries
* Tuples
* Basic data cleaning
* Functions
* Parameters and arguments
* Positional and keyword arguments
* `return`
* Default parameters
* Functions working with lists and dictionaries
* Function composition / separation of responsibilities
* Basic statistical calculations
* Basic mathematical reasoning
* Basic algorithmic reasoning
---

## Concepts Currently Being Consolidated
### Functions
Current function concepts include:
* Defining functions with `def`
* Calling functions
* Parameters vs arguments
* Positional arguments
* Keyword arguments
* Returning values with `return`
* Multiple return paths
* Default parameters
* Returning different data structures
* Functions receiving lists and dictionaries
* Separating data processing from presentation
* Functions working together as a pipeline
Current conceptual architecture:
```text
raw data
    ↓
function
    ↓
processed data
    ↓
function
    ↓
analysis
    ↓
function
    ↓
report
```
The next objective is to become comfortable composing functions and integrating previously learned Python concepts.
---

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

Dynamic key access:

```python
neuron = "inhibitory"

neuron_counts[neuron] += 1
```

A dictionary can therefore represent relationships, structured data, and multiple dynamic counters.

Nested dictionaries are also understood:

```python
neural_population["neuron_1"]["firing_rate"]
```

---

## Recent Integrated Practice

### Neural Population Analysis

Built functions that:

* Clean and normalize neuron data.
* Count neuron types.
* Determine population size.
* Determine the number of unique neuron types.
* Filter neurons according to signal strength.
* Analyze neuron-type frequencies.
* Separate data processing from reporting.
* Return structured results.

Example conceptual pipeline:

```text
raw neural data
       ↓
clean data
       ↓
analyze population
       ↓
classify / filter
       ↓
structured results
       ↓
report
```

---

## Mathematical Practice

Mathematics is being introduced progressively through Python rather than treated as a completely separate subject.

Current topics practiced:

* Positive / negative / zero
* Even / odd numbers
* Remainder and divisibility
* Basic arithmetic
* Total and average
* Highest and lowest values
* Counting according to conditions
* Basic statistics
* Mathematical reasoning through algorithms

Recent exercises included:

* Number classification
* Basic statistics
* Temperature analysis
* Number analysis
* Prime number detection

Important current objective:

```text
intuition
    ↓
reasoning
    ↓
formalization
    ↓
Python implementation
    ↓
interpretation
```

Mathematics should become progressively more automatic while avoiding premature abstraction.

---

# Academic Roadmap

The project is being developed as preparation for the first year of the:

**Tecnicatura Universitaria en Ciencia de Datos — UNCUYO**

The university curriculum is used as a **roadmap**, not as a rigid checklist.

The objective is to arrive at the degree with strong Python fundamentals and enough computational maturity to dedicate more attention to mathematics, statistics, English, software design and data science.

---

## First-Year Academic Map

### 1. Cálculo y Álgebra Lineal Aplicados

Topics to progressively prepare for:

```text
Logic
    ↓
Functions
    ↓
Limits
    ↓
Derivatives
    ↓
Integrals
    ↓
Sequences and series
    ↓
Vectors
    ↓
Matrices
    ↓
Linear systems
    ↓
Vector spaces
    ↓
Linear transformations
    ↓
Eigenvalues / eigenvectors
    ↓
LU / SVD
    ↓
Multivariable calculus
```

Python will later be used as a computational tool for mathematical exploration.

---

### 2. Inglés

Progressively develop the ability to understand:

* Technical vocabulary
* Instructions
* Explanatory texts
* Documentation
* Programming terminology
* Data science terminology

English will continue to be integrated naturally into programming.

---

### 3. Probabilidad y Análisis Estadístico

Progressive roadmap:

```text
Arithmetic
    ↓
Descriptive statistics
    ↓
Probability
    ↓
Random variables
    ↓
Distributions
    ↓
Sampling
    ↓
Correlation
    ↓
Regression
    ↓
Inference
```

Python will eventually be used to simulate, calculate and visualize statistical concepts.

---

### 4. Introducción a la Programación

Current main preparation path:

```text
Variables
    ↓
Conditionals
    ↓
Loops
    ↓
Lists / Tuples / Sets / Dictionaries
    ↓
Functions
    ↓
Files
    ↓
Modules
    ↓
Standard library
    ↓
Object-oriented programming
    ↓
Scientific Python
```

Later topics:

* CSV
* NumPy
* Pandas
* Matplotlib
* Seaborn

---

### 5. Análisis y Diseño de Software

To be introduced progressively after stronger programming fundamentals:

* Problem decomposition
* Requirements
* Modularity
* Cohesion
* Coupling
* Object-oriented analysis
* UML
* Design patterns
* Software architecture

The current separation between analysis functions and reporting functions is an early introduction to modular design.

---

### 6. Inglés Aplicado

Later preparation:

* Verb structures
* Passive voice
* Connectors
* Technical texts
* CV
* Professional profile

---

### 7. Gestión de Proyectos de Software

Git and GitHub will continue throughout the project.

Later topics:

* Branches
* Remote repositories
* Merge conflicts
* Project planning
* Agile methodologies
* CI/CD

Current practice:

```text
learn
  ↓
implement
  ↓
test
  ↓
commit
  ↓
push
```

---

### 8. Bases de Datos

Later roadmap:

```text
Data structures
    ↓
Structured data
    ↓
Files / CSV
    ↓
Relational databases
    ↓
SQL
    ↓
Python + databases
    ↓
NoSQL
```

---

### 9. Introducción a Ciencia de Datos

Later roadmap:

```text
Data
    ↓
Cleaning
    ↓
Exploration
    ↓
Features / Labels
    ↓
Training / Testing
    ↓
Evaluation
    ↓
Machine Learning
```

Tools to introduce progressively:

* NumPy
* Pandas
* Matplotlib
* Jupyter
* Scikit-Learn

TensorFlow and Keras remain later-stage topics.

---

### 10. Taller de Programación

This represents a later stage of the Python roadmap.

Topics include:

* Advanced OOP
* Special methods
* Operator overloading
* Composition and aggregation
* Advanced data structures
* Stacks
* Queues
* Trees
* Graphs
* Exceptions
* Serialization
* Decorators
* Generators
* Functional programming
* `lambda`
* `map`
* `filter`
* `reduce`
* Concurrency
* Parallelism
* Advanced NumPy / Pandas
* Algorithmic efficiency
* Big-O
* Integrative software projects

These topics should **not be studied prematurely**. They will be introduced when the underlying concepts are sufficiently developed.

---

# Integrated Learning Roadmap

The long-term structure of the project is:

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
Machine Learning
   ↓
Neuroscience
   ↓
Neurodata
```

These areas are interconnected rather than strictly sequential.

Python provides the computational foundation.

Mathematics provides formal reasoning.

Statistics provides tools for uncertainty and data analysis.

Data Science integrates programming, mathematics and statistics.

Neuroscience provides the scientific domain in which these tools can eventually be applied.

---

# Learning Methodology

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

Exercises should describe the required behavior without revealing the exact Python constructs needed to solve them.

The objective is to develop independent problem-solving ability.

---

# Technical English

Continue progressively using English for:

* Variables
* Filenames
* Function names
* Comments
* Technical terminology
* Error messages
* Documentation

Main explanations remain in Spanish.

---

# Git Status

The project is maintained with Git/GitHub.

Preferred commit style:

```text
Add Python variables fundamentals

Add Python conditionals fundamentals

Add variables and conditionals exercises

Add loop and conditional integration exercises

Add string manipulation and data cleaning exercises

Add dictionary fundamentals

Add Python functions fundamentals

Add function integration exercises
```

Before ending a study session:

```text
review changes
    ↓
commit
    ↓
push
```

Keep `CURRENT_STATE.md` updated when the learning state changes significantly.

---

# Current Project Structure

```text
neuro-data-lab/

├── README.md
├── CURRENT_STATE.md
│
└── 01_foundations/
    └── python/
        ├── 01_variables.py
        ├── 02_conditionals.py
        ├── 03_variables_and_conditionals_exercises.py
        ├── 04_loops.py
        ├── 05_lists.py
        ├── 06_exercises_01.py
        ├── 07_strings.py
        ├── 08_data_structures.py
        ├── 09_dictionaries.py
        ├── 10_functions.py
        └── 11_exercises_02.py
```
---
# Current Position

Current stage:

```text
Python Fundamentals
        ↓
Functions
        ↓
Integration
        ↓
Mathematical reasoning
```

Current objective:

**Consolidate functions by combining them with the Python concepts already learned, while progressively introducing mathematical reasoning and preparing the foundations required by the first-year Data Science curriculum.**

Do not restart Python fundamentals.

Continue from the current level.
---
# Learning Momentum
The student is progressing from isolated Python concepts toward integrated problem solving.

A particularly important transition has occurred:

```text
learning individual syntax
        ↓
reasoning about data
        ↓
designing functions
        ↓
combining functions
        ↓
solving mathematical problems
        ↓
thinking about algorithms
```
The next stage is to strengthen this transition without rushing into advanced Python.
The university curriculum should guide the direction of the project while the actual learning pace remains determined by conceptual understanding and practical competence.
