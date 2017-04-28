def test_loops(max_col, max_row):
    for i in range(col -1, col + 2):
        for j in range(row - 1, row + 2):
            if max_col >= i >= 0 and max_row >= j >= 0:
                print("col:", i, "row:", j)

print("### corner values ###")
col = 244
row = 400
test_loops(244, 400)
print("")
col = 0
row = 0
test_loops(244, 400)
print("")
col = 0
row = 400
test_loops(244, 400)
print("")
col = 244
row = 0
test_loops(244, 400)

print("\n### wall ###")
print("")
col = 244
row = 17
test_loops(244, 400)

print("")
col = 23
row = 400
test_loops(244, 400)

print("\n###center###")
col = 23
row = 56
test_loops(244, 400)
