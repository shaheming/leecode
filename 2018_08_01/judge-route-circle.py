class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        path = {}
        for m in moves:
            if m not in path:
                path[m]=1
            else:
                path[m]+=1
        return path.get("L",0) == path.get("R",0) and path.get("U",0)==path.get("D",0)
