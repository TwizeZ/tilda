"""
Felix Larsson
DD1320 Tillämpad datalogi
C-labben
2024-12-10
"""

data_file1 = "data1.json"
data_file2 = "data2.json"
data_file3 = "data3.json"
data_file4 = "data4.json"
data_file5 = "data5.json"

import time
import gzip
import bz2
import os


def compress_gzip(input_data):
    start = time.time()
    compressed_data = gzip.compress(input_data)
    duration = time.time() - start
    return compressed_data, duration


def compress_bz2(input_data):
    start = time.time()
    compressed_data = bz2.compress(input_data)
    duration = time.time() - start
    return compressed_data, duration


def calculate_speed_ratio(time1, time2):
    if time2 == 0:  # Undvik division med noll
        return float('inf')
    return time1 / time2



def main(file_path):
    # Läs in JSON-filen
    with open(file_path, 'rb') as file:
        data = file.read()
    
    original_size = len(data)
    print(f"Original storlek: {original_size} bytes")
    
    # Gzip-komprimering
    gzip_data, gzip_time = compress_gzip(data)
    gzip_size = len(gzip_data)
    print(f"Gzip: {gzip_size} bytes, Komprimeringstid: {gzip_time:.5f} sekunder")

    # BZ2-komprimering
    bz2_data, bz2_time = compress_bz2(data)
    bz2_size = len(bz2_data)
    print(f"BZ2: {bz2_size} bytes, Komprimeringstid: {bz2_time:.5f} sekunder")
    print()
    # Komprimeringsgrad
    gzip_ratio = 100 * (1 - gzip_size / original_size)
    bz2_ratio = 100 * (1 - bz2_size / original_size)
    print(f"Gzip komprimeringsgrad: {gzip_ratio:.2f}%")
    print(f"BZ2 komprimeringsgrad: {bz2_ratio:.2f}%")
    print()
    speed_ratio = calculate_speed_ratio(gzip_time, bz2_time)
    print(f"Speed Ratio (Gzip/BZ2): {speed_ratio:.2f}")
    print()


if __name__ == "__main__":
    print()
    main(data_file1)
    main(data_file2)
    main(data_file3)
    main(data_file4)
    main(data_file5)