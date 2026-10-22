"""
Reference algorithmic functions for AI Test Case Generator evaluation.
Demonstrates boundary conditions, invalid input handling, and non-trivial logic.
"""

from typing import List, Optional

def binary_search(arr: List[int], target: int) -> int:
    """
    Search for target in sorted array. Returns index if found, else -1.
    Raises TypeError if array contains non-integers.
    """
    if not isinstance(arr, list):
        raise TypeError("Input array must be a list")
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if not isinstance(arr[mid], int):
            raise TypeError("Array elements must be integers")
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def clamp(val: float, min_val: float, max_val: float) -> float:
    """
    Clamps a value within [min_val, max_val] range.
    Raises ValueError if min_val > max_val.
    """
    if min_val > max_val:
        raise ValueError(f"min_val ({min_val}) cannot exceed max_val ({max_val})")
    return max(min_val, min(val, max_val))

def format_byte_size(num_bytes: int) -> str:
    """
    Converts raw bytes to human-readable format.
    Raises ValueError on negative bytes.
    """
    if num_bytes < 0:
        raise ValueError("Byte count cannot be negative")
    
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if num_bytes < 1024.0:
            return f"{num_bytes:3.1f} {unit}".strip()
        num_bytes /= 1024.0
    return f"{num_bytes:.1f} PB".strip()
