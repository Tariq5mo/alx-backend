# Caching

This project focuses on implementing various caching algorithms using Python. It is part of the ALX Software Engineering program, designed to deepen understanding of caching systems and their role in optimizing data storage and retrieval.

## Table of Contents

- [Introduction](#introduction)
- [Concepts and Skills](#concepts-and-skills)
- [Requirements](#requirements)
- [Project Tasks](#project-tasks)
- [Usage](#usage)
- [Resources](#resources)
- [Author](#author)

---

## Introduction

Caching is a technique used to improve data access speed by storing frequently accessed data temporarily. This project explores different caching strategies through practical implementations.

### Algorithms Covered

- **Basic Cache**: Unlimited storage, no eviction.
- **FIFO**: First In, First Out.
- **LIFO**: Last In, First Out.
- **LRU**: Least Recently Used.
- **MRU**: Most Recently Used.

**Objective**:
Design Python classes for each caching strategy while adhering to specific rules, including eviction policies when the cache exceeds its maximum size.

---

## Concepts and Skills

### Key Topics Covered

1. **Caching Systems**:
   - Understanding caching purpose and limitations.
   - Exploring real-world applications.

2. **Algorithm Development**:
   - Implementing caching policies with Python.
   - Managing evictions based on specified criteria.

3. **Object-Oriented Programming (OOP)**:
   - Designing classes and methods for specific behaviors.
   - Using inheritance to extend functionality.

4. **Python Programming**:
   - Writing clean, efficient, and modular code.
   - Adhering to the **PEP 8 style guide**.

---

## Requirements

### General

- **Allowed editors**: `vi`, `vim`, `emacs`.
- Code will be interpreted/compiled on **Ubuntu 20.04 LTS** using Python 3.7.
- Adhere to the **PEP 8 style guide** (version 2.5).
- No external module imports allowed.
- All files should:
  - End with a new line.
  - Be executable.
  - Include proper documentation for modules, classes, and functions.

### Repository Structure

- **GitHub repository**: [alx-backend](https://github.com/Tariq5mo/alx-backend)
- **Directory**: `0x01-caching`
- **Files**:
  - `base_caching.py`: Base class for all caching systems.
  - `0-basic_cache.py`: Basic caching with no eviction policy.
  - `1-fifo_cache.py`: FIFO caching.
  - `2-lifo_cache.py`: LIFO caching.
  - `3-lru_cache.py`: LRU caching.
  - `4-mru_cache.py`: MRU caching.

---

## Project Tasks

### **0. Basic Cache**

Create a class `BasicCache` that inherits from `BaseCaching`.
This caching system has no size limit and does not implement an eviction policy.

#### Methods

- `put(self, key, item)`:
  - Adds an item to the cache.
  - Does nothing if `key` or `item` is `None`.
- `get(self, key)`:
  - Retrieves an item by key or `None` if the key does not exist.

---

### **1. FIFO Caching**

Create a class `FIFOCache` that inherits from `BaseCaching`.
Implements the **FIFO (First In, First Out)** eviction policy when the cache exceeds its size limit.

#### Rules

- When the number of items exceeds `MAX_ITEMS`, discard the oldest entry.
- Print `DISCARD: <key>` for the discarded key.

---

### **2. LIFO Caching**

Create a class `LIFOCache` that inherits from `BaseCaching`.
Implements the **LIFO (Last In, First Out)** eviction policy when the cache exceeds its size limit.

#### Rules

- When the number of items exceeds `MAX_ITEMS`, discard the most recently added entry.
- Print `DISCARD: <key>` for the discarded key.

---

### **3. LRU Caching**

Create a class `LRUCache` that inherits from `BaseCaching`.
Implements the **LRU (Least Recently Used)** eviction policy.

#### Rules

- When the number of items exceeds `MAX_ITEMS`, discard the least recently used entry.
- Print `DISCARD: <key>` for the discarded key.

---

### **4. MRU Caching**

Create a class `MRUCache` that inherits from `BaseCaching`.
Implements the **MRU (Most Recently Used)** eviction policy.

#### Rules

- When the number of items exceeds `MAX_ITEMS`, discard the most recently used entry.
- Print `DISCARD: <key>` for the discarded key.

---

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Tariq5mo/alx-backend.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x01-caching
   ```

3. Run the example script for each caching system. For instance, to test FIFO:

   ```bash
   ./1-main.py
   ```

---

## Resources

- **[Caching Strategies](https://en.wikipedia.org/wiki/Cache_replacement_policies)**:
  - Overview of FIFO, LRU, LFU, and MRU.
- **Python Documentation**:
  - Working with dictionaries and object-oriented programming.
- **GeeksforGeeks**:
  - Tutorials on caching and algorithms.

---

## Author

This project was completed by **Tariq Omer**, a student of the ALX Software Engineering program specializing in back-end development. Connect with me on [GitHub](https://github.com/Tariq5mo).

---

**Copyright © 2024 ALX. All rights reserved.**
