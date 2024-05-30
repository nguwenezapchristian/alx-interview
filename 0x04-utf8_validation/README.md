# UTF-8 Validation

## Overview

This project is designed to validate whether a given dataset represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding used for electronic communication, where each character can be encoded using 1 to 4 bytes.

## Project Requirements

- **Language**: Python 3.4.3
- **OS**: Ubuntu 20.04 LTS
- **Coding Style**: PEP 8 (version 1.7.x)
- **File Requirements**:
  - All Python files must start with the shebang `#!/usr/bin/python3`
  - All files should end with a new line
  - Files should be executable

## Usage

The main function provided is `validUTF8(data)`, which determines if the given dataset is a valid UTF-8 encoding.

### Function Prototype

```python
def validUTF8(data):
```

### Parameters

- `data` (List[int]): A list of integers representing bytes of the dataset. Each integer should only contain the 8 least significant bits of a byte.

### Returns

- `bool`: Returns `True` if the data is a valid UTF-8 encoding, otherwise returns `False`.

## Example

Below is an example of how to use the `validUTF8` function:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False
```

## Implementation Details

The `validUTF8` function performs the following steps:

1. **Initialization**: It initializes `num_bytes` to keep track of the number of remaining bytes in the current UTF-8 character.
2. **First Byte Check**: For each byte, if `num_bytes` is 0, it determines the number of bytes in the current character by counting the leading 1s in the byte.
3. **Continuation Byte Check**: For continuation bytes (when `num_bytes > 0`), it checks if they match the 10xxxxxx pattern.
4. **Final Validation**: After processing all bytes, it ensures that `num_bytes` is 0, indicating that all characters were valid.

### Bitwise Operations

The function uses bitwise operations to efficiently check the patterns required by the UTF-8 encoding scheme:

- `mask1 = 1 << 7` (10000000) to check the most significant bit.
- `mask2 = 1 << 6` (01000000) to check the second most significant bit.

### Error Handling

- The function returns `False` if:
  - The number of leading 1s in the first byte is not between 1 and 4.
  - Any continuation byte does not match the 10xxxxxx pattern.

## Running the Script

Make sure to set the executable permissions for your Python files:

```bash
chmod +x 0-validate_utf8.py
chmod +x 0-main.py
```

Then, you can run the script:

```bash
./0-main.py
```
