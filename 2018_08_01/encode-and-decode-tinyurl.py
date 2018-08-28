class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.baseUrl = "http://tinyurl/"
        import hashlib, random
        self.store = {}
        m = hashlib.sha256(longUrl.encode('utf-8'))
        key = m[:5]
        import collections
        path = collections.defaultdict(0)

        while key in self.store:
            tmp = longUrl + str(random.random())
            m = hashlib.sha256(tmp.encode('utf-8'))
            key = m[:5]

        self.store[key] = longUrl
        return self.baseUrl + key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl.replace(self.baseUrl, '')
        return self.store[key]


s = Codec()
s.encode("https://leetcode.com/problems/design-tinyurl")
