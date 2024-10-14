# Python File Operations

This README demonstrates various file operations in Python, including opening, reading, writing, and appending to files.

## Basic File Operations

### Opening a File

There are two common ways to open a file in Python:

1. Using the `open()` function:
   ```python
   file = open("my_file.txt")
   ```

2. Using the `with` statement (recommended):
   ```python
   with open("my_file.txt") as file:
       contents = file.read()  # Read the file
       print(contents)  # This should print "Hello, I'm Dawei."
   ```

The `with` statement automatically closes the file when you're done, so you don't need to call `file.close()`.

## File Modes

When opening a file, you can specify the mode:

- `"r"`: Read (default)
- `"w"`: Write (overwrites existing content)
- `"a"`: Append (adds to existing content)

### Appending to a File

To add new content without overwriting existing data:

```python
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")
```

### Creating a New File

To create a new file and write to it:

```python
with open("new_testing_file.txt", mode="w") as file:
    file.write("Hello world.")
```

This creates a new file named `new_testing_file.txt` in the current directory. If the file already exists, it will be overwritten.

Note: The `"w"` mode will create a new file only if it doesn't already exist. If the file exists, it will be overwritten.

## Best Practices

1. Always use the `with` statement when working with files. It ensures that the file is properly closed after you're done with it.
2. Choose the appropriate mode (`"r"`, `"w"`, or `"a"`) based on your needs.
3. Be cautious when using `"w"` mode, as it will overwrite existing files.
4. Use `"a"` mode when you want to add content to an existing file without erasing its current contents.