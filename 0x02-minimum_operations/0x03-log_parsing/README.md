# Log Parsing

## Overview

This project involves creating a Python script to read log data from standard input, parse it, and compute some metrics. The script reads lines of log data, parses them to extract useful information, and prints statistics after every 10 lines or upon receiving a keyboard interruption (Ctrl + C).

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS

## Project Structure

- `0-stats.py`: The main script to read from stdin, parse log data, and compute metrics.
- `README.md`: This file, providing an overview of the project.

## Input Format

The script reads from standard input (stdin) with each line in the format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

## Output Format

After every 10 lines and/or a keyboard interruption (Ctrl + C), the script prints the following statistics from the beginning:

- **Total file size**: The sum of all previous `<file size>`.
- **Number of lines by status code**:
  - Possible status codes: 200, 301, 400, 401, 403, 404, 405, 500
  - Status codes should be printed in ascending order if they appear.

## Example

Example output after processing lines:

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```

## Usage

To run the script, use:

```bash
./0-stats.py
```

Ensure the script has execute permissions:

```bash
chmod +x 0-stats.py
```

You can generate log data using the provided generator script:

```bash
./0-generator.py | ./0-stats.py
```

## Author

[Nguweneza P Christian]