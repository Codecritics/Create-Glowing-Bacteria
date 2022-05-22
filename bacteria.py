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

    with open(input()) as file:
        first_line, second_line = file.readlines()
        original_plasmid_strand, original_plasmid_strand_sticky, complementary_plasmid_strand, complementary_plasmid_strand_sticky = first_line.split()
        original_gfp_strand_sticky, complementary_gfp_strand_sticky = second_line.split()

    print(original_plasmid_strand, original_gfp_strand_sticky, original_plasmid_strand_sticky, sep="")
    print(complementary_plasmid_strand, complementary_gfp_strand_sticky, complementary_plasmid_strand_sticky, sep="")