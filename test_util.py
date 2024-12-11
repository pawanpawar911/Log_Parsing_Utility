import pytest
import re

from util import filtered_lines, highlight_match, ipv4_pattern, ipv6_pattern , ts_pattern

def remove_ansi_escape_sequences(text):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)

class TestLogParserUtility():

    def test_timestamps(self):
        lines = ["13:01:03 INFO Application started"]
        result = filtered_lines(lines, ts_pattern)
        
        expected = ["13:01:03 INFO Application started"]
        
        assert result == expected
        
    def test_without_timestamps(self):
        lines = ["INFO Application started"]
        result = filtered_lines(lines, ts_pattern)
        
        expected = ["INFO Application started"]
        print("Test is without Timestamp")
        
        assert result != expected
        
    def test_ipv4_address(self):
        lines = ["04:36:58 ERROR Connection failed to 192.168.0.1"]
        
        filter_line = filtered_lines(lines, ipv4_pattern)
        result = highlight_match(filter_line, ipv4_pattern)
        
        #expected = ["04:36:58 ERROR Connection failed to \033[32m192.168.0.1\033[0m"]
        expected = ["04:36:58 ERROR Connection failed to 192.168.0.1"]
        
        result_stripped = [remove_ansi_escape_sequences(line) for line in result]
        expected_stripped = [remove_ansi_escape_sequences(line) for line in expected]
        
        assert result_stripped == expected_stripped
        
    def test_ipv4_address_mismatch(self):
        lines = ["04:36:58 ERROR Connection failed to 192.168.0.2"]
        
        filter_line = filtered_lines(lines, ipv4_pattern)
        result = highlight_match(filter_line, ipv4_pattern)
        
        #expected = ["04:36:58 ERROR Connection failed to \033[32m192.168.0.1\033[0m"]
        expected = ["04:36:58 ERROR Connection failed to 192.168.0.1"]
        
        result_stripped = [remove_ansi_escape_sequences(line) for line in result]
        expected_stripped = [remove_ansi_escape_sequences(line) for line in expected]
        
        assert result_stripped != expected_stripped
        
    def test_ipv6_address(self):
        lines = ["23:27:37 INFO Network request to be5c:5799:416:4b92:25b7:e6df:dc9:d50d completed"]
        
        filter_line = filtered_lines(lines, ipv6_pattern)
        result = highlight_match(filter_line, ipv6_pattern)
        
        expected = ["23:27:37 INFO Network request to be5c:5799:416:4b92:25b7:e6df:dc9:d50d completed"]
        
        result_stripped = [remove_ansi_escape_sequences(line) for line in result]
        expected_stripped = [remove_ansi_escape_sequences(line) for line in expected]
        
        assert result_stripped == expected_stripped
        
    def test_ipv6_address_mismatch(self):
        lines = ["23:27:37 INFO Network request to be5c:5799:416:4b92:25b7:e6df:dc9: completed"]
        
        filter_line = filtered_lines(lines, ipv6_pattern)
        result = highlight_match(filter_line, ipv6_pattern)
        
        expected = ["23:27:37 INFO Network request to be5c:5799:416:4b92:25b7:e6df:dc9:d50d completed"]
        
        result_stripped = [remove_ansi_escape_sequences(line) for line in result]
        expected_stripped = [remove_ansi_escape_sequences(line) for line in expected]
        
        assert result_stripped != expected_stripped
            
if __name__ == "__main__":
    pytest.main()