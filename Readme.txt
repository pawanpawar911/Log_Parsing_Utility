# Log Parser Utility CLI Application

# Overview
This Python script is a flexible log parsing utility that enables users to filter and highlight specific types of information from log files, such as timestamps, IPv4 addresses, and IPv6 addresses. It also supports saving the filtered output to a file.

# Features
- Extract specific lines containing:
  - Timestamps (e.g., `12:34:56`)
  - IPv4 addresses (e.g., `192.168.0.1`)
  - IPv6 addresses (e.g., `fe80::1`)
- Highlight matching patterns in the terminal output.
- Extract the first or last `N` lines of the log file.
- Save the filtered results to a specified output file.

# Usage
Run the script using the following command:
with this command data will save into default result.log file
```
python util.py [options] <file>
```
or 
to store the data into the desired output file.
```
python util.py [options] <output_file> <input_file>
```

### Options
| Option                  | Description                                        |
|-------------------------|----------------------------------------------------|
| `-h, help`              | Help
| `-f, --first NUM`       | Print the first `NUM` lines of the log file.       |
| `-l, --last NUM`        | Print the last `NUM` lines of the log file.        |
| `-t, --timestamps`      | Filter lines containing timestamps.                |
| `-i, --ipv4`            | Filter lines containing IPv4 addresses.            |
| `-I, --ipv6`            | Filter lines containing IPv6 addresses.            |
| `-o, --output FILE`     | Save the output to the specified file. Default: `./result.log`. |


## Examples

### 1. Extract the first 10 lines from a log file:
```
python util.py -f 10 test_1.log
```

### 2. Extract lines containing timestamps:
```
python util.py -t test_1.log
```

### 3. Extract lines with IPv4 addresses and save the result:
```
python util.py -i -o ipv4_results.log test_2.log
```

### 4. Extract lines with both IPv4 and IPv6 addresses:
```
python util.py -i -I -o ipv4_ipv6_results.log test_2.log
```

### 5. Extract the last 20 lines from a log file:
```
python util.py -l 20 example.log
```

### 6. Parse a log from standard input:
```
cat example.log | python util.py -t
```

## Output
The script highlights matched patterns (e.g., timestamps, IPv4, or IPv6 addresses) in the terminal output using yellow text. The results are also saved to the specified output file without any color formatting.

## Implementation Details
- **Regex Patterns:**
  - Timestamps: `\b\d{2}:\d{2}:\d{2}\b`
  - IPv4: `\b(?:\d{1,3}\.){3}\d{1,3}\b`
  - IPv6: `\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b`
- **Dependencies:** The `colorama` library is used to add ANSI color codes for highlighting matches in the terminal output.
- **Output Handling:** The results are saved to the output file with ANSI color codes removed for compatibility with plain text readers.
