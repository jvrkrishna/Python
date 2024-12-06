# a=10 ----- 1010
# b=7  ----- 0111
# a&b  ----- 0010 ---- 2
# a|b  ----- 1111 ---- 15
# a^b  ----- 1101 ---- 13 (If both are same then 0 other wise 1)

# a=13  ------------- 0|1101 ---- 0010(Actual answer 2 but no)
#                         +1 ( Here 1+1 is 10 give 0 and 1 carries)
#                   =========
#                     1|1110 (Here 1 is negative index and 0 is positive index)
#          Output is: -14
# print(~a)


# x=10 --------------- 0|1010 ------- 0101(Actual output 5)
#                          +1
#                     ==========
#                      1|1011
#               result is -11
# print(~x)
