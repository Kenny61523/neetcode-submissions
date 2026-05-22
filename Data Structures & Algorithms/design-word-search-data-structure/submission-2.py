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
    
        def dfs(i, cur):
            for j in range(i, len(word)):
                
                #case . -> go thorugh children and skip the iteration 
                if word[j] == '.':
                    # go through all chidren values
                    for child in cur.children.values():
                        if dfs(j + 1, child):
                            return True
                    
                    return False

                else:
                    if word[j] not in cur.children:
                        return False
                    # cur = cur.childre[word[j]]
                    return dfs(j + 1, cur.children[word[j]])

            return cur.endOfWord

        return dfs(0, self.root)        





