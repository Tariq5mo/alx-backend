# 0x00. Pagination

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Setup](#setup)
- [Project Tasks](#project-tasks)
  - [0. Simple Helper Function](#0-simple-helper-function)
  - [1. Simple Pagination](#1-simple-pagination)
  - [2. Hypermedia Pagination](#2-hypermedia-pagination)
  - [3. Deletion-Resilient Pagination](#3-deletion-resilient-pagination)
- [Usage](#usage)
- [Author](#author)

---

## Overview

This project is part of the ALX Software Engineering curriculum focused on **Back-End Development**. It introduces the concept of pagination, a crucial feature in designing REST APIs for handling large datasets. The project builds upon a dataset of popular baby names and explores different pagination strategies.

---

## Learning Objectives

By completing this project, you will be able to:

1. Paginate datasets using simple `page` and `page_size` parameters.
2. Implement hypermedia-driven pagination with metadata.
3. Design deletion-resilient pagination for dynamic datasets.

---

## Requirements

- **Environment**: Ubuntu 18.04 LTS
- **Python Version**: Python 3.7
- **Code Style**: `pycodestyle` (v2.5.*)
- All files must:
  - Start with `#!/usr/bin/env python3`.
  - Include proper documentation.
  - End with a new line.
- Functions and coroutines must be type-annotated.

---

## Setup

### Dataset

The dataset used is `Popular_Baby_Names.csv`. It contains information about baby names categorized by year, gender, ethnicity, count, and rank.

To retrieve and prepare the dataset:

```bash
wget https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv -O Popular_Baby_Names.csv
```

---

## Project Tasks

### 0. Simple Helper Function

Implement a function `index_range(page, page_size)` to calculate start and end indices for a page of data.

### 1. Simple Pagination

Develop the `Server` class with:

- A `dataset()` method to cache and return the dataset.
- A `get_page(page, page_size)` method to retrieve a specific page from the dataset.

### 2. Hypermedia Pagination

Extend the `Server` class to include:

- A `get_hyper(page, page_size)` method that returns a dictionary with:
  - `page_size`, `page`, `data`, `next_page`, `prev_page`, and `total_pages`.

### 3. Deletion-Resilient Pagination

Implement deletion-resilient pagination in the `get_hyper_index(index, page_size)` method, ensuring no items are skipped even when rows are removed.

---

## Usage

To run the examples, execute the provided main files. For instance:

```bash
./0-main.py
./1-main.py
./2-main.py
./3-main.py
```

### Example Output

For **Simple Pagination**:

```bash
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ...]
```

For **Hypermedia Pagination**:

```json
{
  "page_size": 10,
  "page": 1,
  "data": [...],
  "next_page": 2,
  "prev_page": null,
  "total_pages": 1000
}
```

---

## Author

### Tariq Omer

- GitHub: [Tariq5mo](https://github.com/Tariq5mo)
- ALX Software Engineering Student specializing in Back-End Development.
