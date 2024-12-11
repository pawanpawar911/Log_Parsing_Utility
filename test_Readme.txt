## Log Parser Utility Test Suite

This test suite is designed to validate the functionality of utility methods for parsing and processing log data. The utilities being tested include filtering log lines based on timestamp, IPv4 and IPv6 address patterns, and highlighting matched patterns. The suite leverages pytest for streamlined testing.

## Features

# Timestamp Filtering:

Tests the ability to filter log lines containing valid timestamps.

# IPv4 Address Filtering:

Validates filtering of lines containing valid IPv4 addresses.

Verifies proper handling of mismatches in IPv4 addresses.

# IPv6 Address Filtering:

Validates filtering of lines containing valid IPv6 addresses.

Verifies proper handling of mismatches in IPv6 addresses.

# ANSI Escape Sequence Removal:

Strips ANSI escape sequences from the processed output to ensure test results are comparable.

## Test Cases

1. Timestamp Filtering

test_timestamps:

Confirms that log lines containing timestamps are correctly filtered.

test_without_timestamps:

Verifies that log lines without timestamps are not erroneously matched.

2. IPv4 Address Filtering

test_ipv4_address:

Tests successful filtering and highlighting of valid IPv4 addresses in log lines.

test_ipv4_address_mismatch:

Ensures lines with mismatched IPv4 addresses are not incorrectly highlighted.

3. IPv6 Address Filtering

test_ipv6_address:

Tests successful filtering and highlighting of valid IPv6 addresses in log lines.

test_ipv6_address_mismatch:

Ensures lines with mismatched IPv6 addresses are not incorrectly highlighted.

## Utility Functions

filtered_lines:
Filters log lines based on a provided regular expression pattern.

highlight_match:
Highlights matched patterns in log lines for improved visibility.

remove_ansi_escape_sequences:
Removes ANSI escape sequences from strings, ensuring test output consistency.

Regular Expression Patterns

ts_pattern: Matches valid timestamps in log lines.

ipv4_pattern: Matches valid IPv4 addresses in log lines.

ipv6_pattern: Matches valid IPv6 addresses in log lines.