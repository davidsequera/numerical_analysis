# def interpolation(x, y, xi):
#     """
#     Interpolates the value of xi using the given x and y values.
#     """
#     n = len(x)
#     if n != len(y):
#         raise ValueError("x and y must have the same length.")
#     if n < 2:
#         raise ValueError("At least two points are required.")
#     if xi < x[0] or xi > x[n-1]:
#         raise ValueError("xi must be within the range of x.")
#     i = 0
#     j = n-1
#     while j - i > 1:
#         k = (xi - x[i]) / (x[j] - x[i])
#         if k < 0 or k > 1:
#             raise ValueError("Something went wrong.")
#         m = i + int((j - i) * k)
#         if xi < x[m]:
#             j = m
#         else:
#             i = m
#     return y[i] + (y[j] - y[i]) * (xi - x[i]) / (x[j] - x[i])


# #  Example
# x = [0, 1, 2, 3, 4]
# y = [0, 1, 8, 27, 64]
# xi = 2.5
# interpolation(x, y, xi)