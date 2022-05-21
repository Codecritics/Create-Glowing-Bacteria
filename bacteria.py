def get_complementary_strand(origin: str) -> str:
    c_strand = ""
    c_principle = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
        " ": " "
    }
    for vitamin in origin:
        c_strand = "".join([c_strand, c_principle[vitamin]])
    return c_strand


if __name__ == '__main__':
    origin_strand, restriction_site = input(), input()
    complementary_restriction_site, complementary_strand = get_complementary_strand(
        restriction_site), get_complementary_strand(origin_strand)
    origin_start, origin_end = origin_strand.index(restriction_site.split()[0]), origin_strand.index(
        restriction_site.split()[1])
    print(origin_strand[origin_start + 1:origin_end + 1])

    complementary_start, complementary_end = complementary_strand.index(
        complementary_restriction_site.split()[0]), complementary_strand.index(
        complementary_restriction_site.split()[1])
    print(complementary_strand[
          complementary_start + len(complementary_restriction_site.split()[0]) - 1:complementary_end + len(
              complementary_restriction_site.split()[1]) - 1])
