class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):

        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:

        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()


            cur = cur.children[w]

        cur.end = True
        

    def search(self, word: str) -> bool:
        

        def dfs(i, node):
            
            if i == len(word):
                return node.end
            
            w = word[i]

            if w == ".":
                for child in node.children.values():

                    if dfs(i+1, child):
                        return True

                return False

            
            if w not in node.children:

                return False

            return dfs(i+1, node.children[w])

        

        return dfs(0, self.root)

                


            

                
                
