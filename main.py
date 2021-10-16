#!/usr/bin/env python3
"""Python script to test GitHub actions"""
import sys


def main() -> int:
    result = 1 + 1
    sys.stdout.write(f"Test {result}\n")
    return result


if __name__ == "__main__":
    main()
