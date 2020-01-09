k = 0
for x1 in [True]:
    for x2 in [True, False]:
        for x3 in [True, False]:
            for x4 in [True, False]:
                for x5 in [True, False]:
                    for x6 in [True, False]:
                        for x7 in [True, False]:
                            for x8 in [True, False]:
                                if (x1 == x2 or x3 or x4 or not(x5))and(x2 == x3 or x4 or x5 or not(x6))and(x3 == x4 or x5 or x6 or not(x7))and(x4 == x5 or x6 or x7 or not(x8)):
                                    k += 1
print(k)
