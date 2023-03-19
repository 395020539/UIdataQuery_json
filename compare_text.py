
# 筛选字符串中非空格的内容并输出成新字符串
def simp_str(str):
    str_out = ""
    if str:
        for char in str:
            if char != " " and char != "\n":
                str_out = str_out + char
    print(f"str_out = {str_out}")
    return str_out


# if simp_str(str1) == simp_str(str2):
#     print("相同")
# else:
#     print("不同")
