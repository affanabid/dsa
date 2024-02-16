def pascalTriangle(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    else:
        new_row = [1]
        last_row = pascalTriangle(n-1)
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
    return new_row

print(pascalTriangle(1))
