# echologyx-py-package

**echologyx_py** - a Python package containing two methods **move_alphabets** and **missing_number**.

## Installation

- Clone the git repository:

  ```bash
  git clone git@github.com:adnan-alam/echologyx-py-package.git
  ```

- Go to the root directory **echologyx-py-package** and install the pacakge:
  ```bash
  pip install .
  ```

## Usage

### move_alphabets

- The method takes two parameters:

  - **word**, a string between 'a-z' (inclusive).
  - **alphabet**, a character between 'a-z' (inclusive).

- It moves all characters in the **word** which matches **alphabet** to end of the **word**
  while maintaining the relative order of the other characters in the **word**.

- Example:
  ```bash
    >>> from echologyx_py.echologyx_py import move_alphabets
    >>> move_alphabets("HelloThere", "e")
    'HlloThreee'
  ```

### missing_number

- The method takes one parameter:

  - **nums**, an array containing **n** distinct numbers in the range [0, n]. **n** is length of the array.

- It returns the only number in the range that is missing from the array.

- Example:
  ```bash
      >>> from echologyx_py.echologyx_py import missing_number
      >>> missing_number([9,6,4,2,3,5,7,0,1])
      8
  ```
