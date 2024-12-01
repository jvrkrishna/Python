def fun(num):
    print('*'*num)
    if num==5:
        return
    fun(num+1)

fun(1)
