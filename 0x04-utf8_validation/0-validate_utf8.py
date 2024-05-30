#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Validate if a given list of integers represents a valid UTF-8 encoding.

    Args:
    data (List[int]): List of integers representing the bytes of the data set.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    """ Masks for the significant bits of the bytes """
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        if num_bytes == 0:
            """
            Determine the number of bytes in
            the current UTF-8 character
            """
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                """Single-byte character (0xxxxxxx)"""
                continue

            if num_bytes == 1 or num_bytes > 4:
                """Invalid scenarios: continuation byte or more than 4 bytes"""
                return False

        else:
            """ Check that the byte is of the form 10xxxxxx """
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
