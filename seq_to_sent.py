def seq_to_sent(seq,dic):
    if len(seq)==0:
        return ''
    for i in range(1, len(seq)+1):
        if seq[:i] in dic:
            temp_res = seq_to_sent(seq[i:],dic)
            if temp_res != None:
                return seq[:i]+' '+temp_res
    return None

def main():
    seq = "eatanapple"
    dic = set(["eat","an","a","apple"])
    print (seq_to_sent(seq, dic))

if __name__ == '__main__':
    main()
