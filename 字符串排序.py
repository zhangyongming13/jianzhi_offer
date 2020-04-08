# 字符串排序
# https://www.nowcoder.com/practice/5190a1db6f4f4ddb92fd9c365c944584?tpId=37&tqId=21249&rp=0&ru=/ta/huawei&qru=/ta/huawei/question-ranking
if __name__ == '__main__':
    st = 'nowcoder.com/practice/5190a1db6f4f4ddb92'
    st_list = list(st)
    st_dict = {}
    # 记录费字母的字符所在位置
    for i in range(len(st_list)):
        if st_list[i].isalpha():
            pass
        else:
            st_dict[i] = st_list[i]
    # 去除非字母字符
    cisu = 0
    for key, valu in st_dict.items():
        st_list.pop(int(key) - cisu)
        cisu += 1
    # 剩下的字母进行排序
    st_list = sorted(st_list, key=str.upper)
    # 将非字母字符插回原来的位置
    for key, valu in st_dict.items():
        st_list.insert(int(key), valu)
    print(''.join(st_list))
