# In-Memory Database with Transaction Support

This repository contains a Python script implementing a simple in-memory database that supports transactions. The InMemoryDB class offers basic functionalities like beginning a transaction, committing changes, rolling back to a previous state, and setting or retrieving key-value pairs.

## Features

- **Begin Transaction**: Start recording database operations that can later be committed or rolled back.
- **Commit**: Apply all changes made during the transaction to the main database state.
- **Rollback**: Discard all changes made during the transaction and revert to the state before the transaction started.
- **Put**: Insert or update a key-value pair in the database within a transaction.
- **Get**: Retrieve the value associated with a key from the database.

## How to Run the Code

To run this script, you will need Python 3 installed on your computer. Steps:

1. Clone this repository or just download the `in_memory_db.py` file.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python by typing `python in_memory_db.py`.

## Provided Example

The script includes an example that shows the functionality of the database class. It shows how to:

- Retrieve a value for a key that does not exist.
- Attempt to modify the database without a transaction and handle the resulting error.
- Start a transaction, modify values, and either commit these changes or roll them back.

## Suggestions for Assignment Improvement

1. Provide a more detailed specification of the expected behaviors for each method. a
2. Give more information on edge cases for each method.
3. Include a set of automated tests that students can run to verify their implementations before submission or at least expected output.
4. Introduce additional features to be implemented that show how these could be used in real-life scenarios.
5. To include more specifics in the grading rubric for the actual code to make sure we are on track.
