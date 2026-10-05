class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st=[]
        n=len(asteroids)
        for i in range(0,n):
            if st and st[-1]>0 and asteroids[i] < 0:
                top=st[-1]
                upcoming=True
                while st and upcoming:
                    if asteroids[i]<0 and top<0:
                        break
                    elif abs(top)==abs(asteroids[i]):
                        st.pop()
                        upcoming=False
                    elif abs(top)<abs(asteroids[i]):
                        st.pop()
                        if st:
                            top=st[-1]
                    else:
                        upcoming=False
                        break
                if upcoming:
                    st.append(asteroids[i])
            else:
                st.append(asteroids[i])
                
        return st
