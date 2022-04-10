def search(pat, txt):
    """
    Given a text txt[0..n-1] and a pattern pat[0..m-1], 
    write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[].
    You may assume that n > m.
    """
    N = len(txt)
    M = len(pat)

    for i in range(N-M+1):
        j = 0
        while (j < M):
            if(txt[i+j] != pat[j]):
                break
            j += 1
        if (j == M):
            print("pattern found at index: ", i)



if __name__ == "__main__":
    pat = "AAAB"
    txt = "AAAAAAAAAAAAAAAAAB"
    search(pat, txt) 
