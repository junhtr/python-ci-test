#!/usr/bin/env python3
"""Python script to test GitHub actions"""
import sys
from typing import Optional


def main() -> int:
    """main"""
    result = 1 + 1
    sys.stdout.write(f"Test {result}\n")
    return result


def main2() -> Optional[int]:
    """main2"""
    result = 3
    return result


if __name__ == "__main__":
    main()
