import argparse
import re
import sys
from colorama import Fore, Style

ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ipv6_pattern = r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b'
ts_pattern = r'\b\d{2}:\d{2}:\d{2}\b'

def parse_args():
    parser = argparse.ArgumentParser(description= "Log Parser Utility")
    parser.add_argument("-f", "--first", type=int, help="Print first NUM lines")
    parser.add_argument("-l", "--last", type=int, help="Print last NUM lines")
    parser.add_argument("-t", "--timestamps", action="store_true", help="Print lines containing timestamps")
    parser.add_argument("-i", "--ipv4", action="store_true", help="Print lines containing ipv4 addresses")
    parser.add_argument("-I", "--ipv6", action="store_true", help="Print lines containing ipv6 addresses")
    parser.add_argument("-o", "--output", type=str, default="./result.log", help="Output file to save results")
    parser.add_argument("file", nargs="?", type=argparse.FileType('r'), default=sys.stdin, help="Log file to parse the data")
    return parser.parse_args()
    
def filtered_lines(lines, pattern):
    return [line for line in lines if re.findall(pattern, line)]

def highlight_match(lines, pattern):
    return [re.sub(pattern, f"{Fore.YELLOW}\\g<0>{Style.RESET_ALL}", line) for line in lines]

def remove_ansi_escape_sequences(text):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)
    
def main():
    
    ipv4_lines = []
    ipv6_lines = []
    result_lines = []
    
    args = parse_args()
    lines = args.file.readlines()
    
    if args.first:
        lines = lines[:args.first]
        
    if args.last:
        lines = lines[-args.last:]
        
    if args.timestamps:
        lines = filtered_lines(lines, ts_pattern)
    
    if args.ipv4:
        ipv4_lines = highlight_match(filtered_lines(lines, ipv4_pattern), ipv4_pattern)
    
    if args.ipv6:
        ipv6_lines = highlight_match(filtered_lines(lines, ipv6_pattern), ipv6_pattern)

    if args.ipv4:
        result_lines.extend(ipv4_lines)
        
    if args.ipv6:
        result_lines.extend(ipv6_lines)

    if not args.ipv4 and not args.ipv6:
        result_lines = lines

    for line in result_lines:
        print(line, end="")
        
    with open(args.output, 'w') as file: 
            
        for item in result_lines:
            file.write(remove_ansi_escape_sequences(item) + '\n')
        
if __name__ == "__main__":
    main()