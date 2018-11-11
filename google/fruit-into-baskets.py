class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(tree) == 0:
            return 0

        p = 0
        maxFruit = 0
        while p < len(tree):
            baskets = set([])
            fruit1 = tree[p]
            fruit2 = -1
            baskets.add(fruit1)
            count = 0
            while p < len(tree):
                if tree[p] in baskets:
                    count += 1
                elif len(baskets) < 2:
                    baskets.add(tree[p])
                    count += 1
                    fruit2 = tree[p]
                else:
                    p -= 1
                    while tree[p-1] == tree[p]:
                        p -= 1
                    break

                p += 1

            maxFruit = max(count, maxFruit)

        return maxFruit
