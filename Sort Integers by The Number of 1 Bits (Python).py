from typing import List

def rearrange(arr:List[int])-> List[int]:
    
    frequency_lists = {}
    for num in arr:
        binary_num = "{0:b}".format(num)
        bit_freq = len([bit for bit in binary_num if bit == '1'])
        frequency_lists.setdefault(bit_freq,[]).append(num)
        
    sorted_freqs = list(sorted(frequency_lists.keys()))
    out = []
    for freq in sorted_freqs:
        out = out+sorted(frequency_lists.get(freq))
    return out
