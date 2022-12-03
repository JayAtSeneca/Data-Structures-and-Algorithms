def get_idx(ch):
    return ord(ch.lower()) - ord('a')
    
class Trie:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.is_word_complete = False
            
    def __init__(self):
        self.root = Trie.TrieNode()


    def insert(self, word):
        # Adds word to the Trie
        curr_node = self.root
        for ch in word:
            ch = ch.lower()
            index = get_idx(ch)
            if not curr_node.children[index]:
                curr_node.children[index] = self.TrieNode()
            curr_node = curr_node.children[index]
        curr_node.is_word_complete = True

    def search(self, word):
        curr = self.root
        for ch in word:
            ch = ch.lower()
            index = get_idx(ch)
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.is_word_complete


    def get_all(self):
        words = []
        self.traverse_trie(self.root, "", words)
        return words

    def begins_with(self, prefix):
        curr_node = self.root
        for ch in prefix:
            ch = ch.lower()
            index = get_idx(ch)
            if not curr_node.children[index]:
                return []
            curr_node = curr_node.children[index]

        words = []
        self.traverse_trie(curr_node, prefix, words)
        return words

    def traverse_trie(self, node, prefix, words):
        if node.is_word_complete:
            words.append(prefix)

        for i in range(26):
            if node.children[i]:
                ch = chr(i + ord('a'))
                self.traverse_trie(node.children[i], prefix + ch, words)

# words = ["yellow", "yell", "yeti", "yes","red","redraw","ran","y"]
# the_trie = Trie()
# for i in range(8):
#     the_trie.insert(words[i])
#     i+=1
# for i in range(8):
#     print(the_trie.search(words[i]), True)
# print(the_trie.search("yel"), False)
# print(the_trie.search("yello"), False)
# print(the_trie.search("yetis"), False)
# print(the_trie.search("ranger"), False)
# print(the_trie.search("redr"), False)
# print(the_trie.search("redra"), False)


# words = ["yellow", "yell", "yeti", "yes","red","redraw","ran"]
# the_trie = Trie()
# for i in range(7):
#     the_trie.insert(words[i])
#     i+=1
# all_words =the_trie.get_all()
# words.sort()
# print(len(all_words), len(words))
# print(all_words,words)

