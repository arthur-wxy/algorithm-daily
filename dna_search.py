from enum import IntEnum
from typing import Tuple, List


Nucleotide = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str = "ACGTGGCTAAAGCAGTACCCCCGATCGAAAGCATGTTCCAATGCA"

# 把str转换为Gene
def string_to_gene(s):
    gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene


my_gene = string_to_gene(gene_str)
# print(my_gene)
# print(type(my_gene))

# 二分搜索
def binary_contains(gene, key_codon):
    low = 0
    high = len(gene) - 1
    while low <= high:
        mid = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False

my_sorted_gene = sorted(my_gene)
print(my_sorted_gene)
print(binary_contains(my_sorted_gene, ACG))
print(binary_contains(my_sorted_gene, gat))
