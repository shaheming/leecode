class Solution:
    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        for word in strs:
            length = len(word)
            c_f = {}
            for ch in word:
                if ch not in c_f:
                    c_f[ch] = 1
                else:
                    c_f[ch] += 1

            if length not in group:
                group[length] = [[c_f, [word]]]
            else:
                for g in group[length]:
                    is_in = True
                    for k, v in g[0].items():
                        if k not in c_f or c_f[k] != v:
                            is_in = False
                            break
                    if is_in:
                        g[1].append(word)
                        break

                if not is_in:
                    group[length].append([c_f, [word]])

        r = []
        for k, v in group.items():
            for g in v:
                r.append(g[1])
        return r

    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            key = "".join(sorted(w))
            d[key] = d.get(key, []) + [w]
        return list(d.values())
#Z注意 p3 要使用 list(d.values()) 和 for k,v in dic.items() 来进行遍历
