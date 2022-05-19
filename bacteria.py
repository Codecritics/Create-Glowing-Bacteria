def get_complementary_strand(origin: str) -> str:
    complementary_strand = ""
    complementary_principle = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    for vitamin in origin:
        complementary_strand = "".join([complementary_strand, complementary_principle[vitamin]])
    return complementary_strand


if __name__ == '__main__':
    origin_strand = input()
    print(origin_strand, get_complementary_strand(origin_strand), sep="\n")
