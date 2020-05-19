

# O(n) time, O(1) space
def o_1_space(n):
    total = 0

    for i in range(n):
        total += 1

    return total


def o_2_space_v2(n):
    times_table = []
    for i in range(n):
        times_table.append(i)

        for j in range(n):
            times_table.append(j)

    return times_table


# O(n) time, and O(n) space
def o_n_space(n):
    sums = []

    for i in range(n):
        sums.append(i + i)

    return sums


# O(n^2) time, O(n) space
def o_n2_space(n):
    times_table = []

    for i in range(n):  # O(n) time
        row = []

        for j in range(n):
            row.append(j * i)  # we're adding n elements to the `row` list

        times_table.append(row)  # we have n lists that each hold n elements

    return times_table  # O(n^2)


# space cpomlexity cares about how much _additional_ space is being used
# O(1) o_1_space
# don't count data structures that are passed in as input
def foo(arr):
    for x in arr:
        print(x + x)


# O(n) space
def bar(arr):
    output = []

    for n in arr:
        output.append(n * n)  # O(n) space

    return output


# O(n)
deg baz(arr):
    evens = []

    # we're adding half of the values from the input array
    for n in arr:
        if n % 2 == 0:
            evens.append(n)  #O(n/2) == O(n)

    return evens
