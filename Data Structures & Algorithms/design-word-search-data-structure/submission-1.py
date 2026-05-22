class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        # forgot this
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(j, cur):
            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    # look for all children valeus 
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            # check if any of the children nodes match
                            return True
                    return False

                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return  cur.endOfWord

        return dfs(0, cur)            


