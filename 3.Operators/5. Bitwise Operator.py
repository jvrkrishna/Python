# Bitwise Operators in Python

# a = 10  ----- 1010
# b = 7   ----- 0111

# a & b   ----- 0010 ---- 2
# AND Operator:
# Both bits must be 1 to get 1.

# a | b   ----- 1111 ---- 15
# OR Operator:
# At least one bit should be 1 to get 1.

# a ^ b   ----- 1101 ---- 13
# XOR Operator:
# If both bits are same -> 0
# If bits are different -> 1


# =====================================
# Bitwise NOT (~)
# Formula: ~(n) = -(n + 1)
# =====================================

# a = 13 ------------- 0|1101
#                      0010   (1's complement)
#                     +0001
#                   =========
#                     0011

# Formula:
# ~(13) = -(13 + 1)
#       = -14

# Output: -14
# print(~a)


# x = 10 ------------- 0|1010
#                      0101   (1's complement)
#                     +0001
#                   =========
#                      0110

# Formula:
# ~(10) = -(10 + 1)
#       = -11

# Output: -11
# print(~x)


# =====================================
# Left Shift (<<)
# Formula:
# n << k = n * (2^k)
# Shifts bits to the left by k positions.
# Zeros are added on the right.
# =====================================

# x = 10 ------------- 1010

# x << 1 ------------ 10100 ---- 20
# (10 * 2^1 = 20)

# x << 2 ----------- 101000 ---- 40
# (10 * 2^2 = 40)

# print(x << 1)  # 20
# print(x << 2)  # 40


# =====================================
# Right Shift (>>)
# Formula:
# n >> k = n // (2^k)
# Shifts bits to the right by k positions.
# Bits on the right are discarded.
# =====================================

# x = 10 ------------- 1010

# x >> 1 ------------- 0101 ---- 5
# (10 // 2^1 = 5)

# x >> 2 ------------- 0010 ---- 2
# (10 // 2^2 = 2)

# print(x >> 1)  # 5
# print(x >> 2)  # 2


# =====================================
# Summary
# =====================================

# &  -> AND        (Both 1 => 1)
# |  -> OR         (Any 1 => 1)
# ^  -> XOR        (Different => 1)
# ~  -> NOT        (-(n+1))
# << -> Left Shift (Multiply by 2^k)
# >> -> Right Shift(Divide by 2^k)

# Example:
# 10 << 2 = 40
# 10 >> 2 = 2