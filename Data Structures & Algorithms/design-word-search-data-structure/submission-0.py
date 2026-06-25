class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(root,word):
            curr = root
            for index,char in enumerate(word):
                if char == ".":
                    for child in curr.children.values():
                        if dfs(child,word[index+1:]):
                            return True
                    return False
                elif char in curr.children:
                    curr = curr.children[char]
                else: return False
            return curr.isEndOfWord
            
        return dfs(self.root,word)
                


