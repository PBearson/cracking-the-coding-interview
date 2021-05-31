# This implementation of Trie uses a (hashed) collection of Trie Nodes, each of which is the root of a Trie graph.
# One of the quirks here is that when we try to find a string, if we find it, then we mark the last node as terminal
# by default.
# An alternative approach is to return true only if we explicitly inserted the string beforehand, i.e., if the node
# was already marked as a terminal node. All well.

class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.terminal = False

class Trie:
    def __init__(self, value):
        self.tries = {}
        self.tries[value] = TrieNode(value)

    def insert(self, string):
        string = string.upper()
        curr = None
        if string[0] in self.tries.keys():
            curr = self.tries[string[0]]
        else:
            self.tries[string[0]] = TrieNode(string[0])
            curr = self.tries[string[0]]

        for s in string[1:]:
            if s in curr.children.keys():
                curr = curr.children[s]
            else:
                curr.children[s] = TrieNode(s)
                curr = curr.children[s]

        curr.terminal = True

    def find(self, string):
        if string[0] not in self.tries.keys():
            return False
        
        curr = self.tries[string[0]]

        for s in string[1:]:
            if s in curr.children.keys():
                curr = curr.children[s]
            else:
                return False
        
        curr.terminal = True
        return True

    def enumerateHelper(self, root, prefix):
        prefix += root.value
        
        if root.terminal == True:
            print(prefix)
        for c in root.children:
            self.enumerateHelper(root.children[c], prefix)


    def enumerate(self):
        for t in self.tries:
            root = self.tries[t]
            self.enumerateHelper(root, "")
            

def test():
    t = Trie("A")
    t.insert("APPLE")
    t.insert("BCD")
    t.insert("OHIO")
    t.insert("PASSIVE")
    t.insert("GOAT")

    assert t.find("APPLE") == True
    assert t.find("APP") == True
    assert t.find("APPLES") == False

    t.insert("CAT")

    assert t.find("A") == t.find("CA") == t.find("CAT") == True

    t.enumerate()

if __name__ == "__main__":
    test()