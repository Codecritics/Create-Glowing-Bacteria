origin_strand, complementary_strand = input().split()

origin_start = origin_strand.rindex("CTGCAG")
origin_restriction_site = origin_strand[origin_start:origin_start + 6]
complementary_restriction_site = ""
complementary_principle = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}
for nucleotide in origin_restriction_site:
    complementary_restriction_site = "".join([complementary_restriction_site, complementary_principle[nucleotide]])

print(origin_strand[:origin_start + 1], origin_strand[origin_start + 1:])
complementary_start = complementary_strand.rindex(complementary_restriction_site)
print(complementary_strand[:complementary_start + 5], complementary_strand[complementary_start + 5:])