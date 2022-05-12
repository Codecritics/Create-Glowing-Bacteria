origin_strand = input()
complementary_strand = ""
complementary_principle = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}
for vitamin in origin_strand:
    complementary_strand = "".join([complementary_strand, complementary_principle[vitamin]])

print(complementary_strand)