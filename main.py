import itertools

floors = [1, 2, 3, 4, 5]

for (L, M, N, E, J) in list(itertools.permutations(floors)):

    # Loes woont niet op de bovenste verdieping (5)
    if L == 5:
        continue
    # Marja woont niet op de begane grond (1)
    if M == 1:
        continue
    # Niels woont niet op de begane grond en bovenste verdieping (1, 5)
    if N == 1 or N == 5:
        continue
    # Niels woont niet op op één verdieping hoger of lager dan Marja ( M - 1, M + 1)
    if N == M - 1 or N == M + 1:
        continue
    # Erik woont ten minste 1 verdieping hoger dan Marja (M > E)
    if M > E:
        continue
    # Joep woont niet op één verdieping hoger of lager dan Niels ( N - 1, N + 1)
    if J == N - 1 or J == N + 1:
        continue

    print(f"Loes woont op verdieping {L}")
    print(f"Marja woont op verdieping {M}")
    print(f"Niels woont op verdieping {N}")
    print(f"Erik woont op verdieping {E}")
    print(f"Joep woont op verdieping {J}")