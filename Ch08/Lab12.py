def find_genes(genes: str):
    start = "ATG"
    ends = ("TAG", "TAA", "TGA")
    init_length = len(genes)

    while genes.find(start) != -1:

        genes = genes[genes.find(start) + 3:]

        for i in range(len(genes)):

            if genes[i] == "T" and (genes[i:i + 3] in ends):
                end = genes[0:i]

                if len(end) >= 3:
                    print(end, end=" ")

                genes = genes[i + 2:]
                break

    if len(genes) == init_length:
        print("no gene is found")

    print()


if __name__ == '__main__':
    print("TTATGTTTTAAGGATGGGGCGTTAGTT = ", end="")
    find_genes("TTATGTTTTAAGGATGGGGCGTTAGTT")

    print("TGTGTGTATAT = ", end="")
    find_genes("TGTGTGTATAT")
