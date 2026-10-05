class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        maxlen=0
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                if len(st)>1 and s[st[-1]]=='(':
                    st.pop()
                    length=i-st[-1]
                    maxlen=max(maxlen,length)
                else:
                    st.append(i)
        return maxlen
            