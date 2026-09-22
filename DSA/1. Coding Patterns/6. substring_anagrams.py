def substring_anagrams(s: str, t: str ) -> int:
    # calculate the length of target and given string
    len_s, len_t = len(s), len(t)
    # if length of target string is greater than given string, 
    # then no substring anagrams possible for given string
    if len_t > len_s:
        return 0
    # initialize the count of the total anagram substring to 0
    count = 0
    # creating varaible for storing the character frequency for 
    # target string and substring(window on given string) of length off target
    expected_freqs, window_freq = [0] * 26, [0] * 26

    # iterarte through the target string for calculating frequency of each character
    for c in t:
        expected_freqs[ord(c)-ord('a')] += 1

    # initialize the left and right pointer to position 0
    left = right = 0

    # iterate over the given string
    while right < len_s:
        # add the character at the right pointer to window freqs 
        # before sliding the window
        window_freq[ord(s[right]) - ord('a')] += 1
        # if the window has reached the expected fixed length, 
        # advance the lefft pointer as well as the right pointer
        # to slide the window
        if right - left + 1 == len_t:
            if window_freq == expected_freqs:
                count += 1
            # remove the character at the left pointer from
            # window_freqs before advancing the left pointer
            window_freq[ord(s[left])- ord('a')] -= 1
            left += 1
        right += 1
    return count


    