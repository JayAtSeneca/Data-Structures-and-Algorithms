def get_idx(ch):
    return ord(ch.lower()) - ord('a')
    
class Trie:
    # Define the TrieNode class
    class TrieNode:
        def __init__(self):
            # Initialize the children list with the capacity to store all 26 elements(one for each letter of the alphabet)
            self.children = [None] * 26

            # Initialize a boolean value to indicate whether the current node marks the end of a word
            self.is_word_complete = False
    #This is the constructor of class Trie. It creates the root node of Trie and initializes the root node with the empty TrieNode.
    def __init__(self):
        # Create a new TrieNode instance and assign it to the root of the Trie.
        self.root = Trie.TrieNode()

    #This function adds word to the Trie
    def insert(self, word):
        curr_node = self.root
        for ch in word:
            ch = ch.lower()
            index = get_idx(ch)
            if not curr_node.children[index]:
                curr_node.children[index] = Trie.TrieNode()
            curr_node = curr_node.children[index]
        curr_node.is_word_complete = True

    #This function returns True if word is in the Trie. Otherwise, it will return false
    def search(self, word):
        # Start at the root of the trie
        curr = self.root

        # Iterate through each character in the word
        for ch in word:
            # Convert the character to lowercase
            ch = ch.lower()

            # Get the index of the character in the trie's children array
            index = get_idx(ch)

            # If there is no node at the calculated index, the word is not in the trie
            if not curr.children[index]:
                return False

            # Move to the child node at the calculated index
            curr = curr.children[index]

        # Return whether the current node marks the end of a valid word
        return curr.is_word_complete


    # This function returns a list of all the words in a trie in alphabetical order
    def get_all(self):
        # Initialize an empty list to store the words
        words = []

        # Call the helper function to traverse the trie and add all the words to the list
        self.traverse_trie(self.root, "", words)

        # Return the list of words
        return words

    # This function returns a list of words that begin with prefix in alphabetical order
    def begins_with(self, prefix):
        # Start at the root of the trie
        curr_node = self.root

        # Iterate through each character in the prefix
        for ch in prefix:
            # Convert the character to lowercase
            ch = ch.lower()

            # Get the index of the character in the trie's children array
            index = get_idx(ch)

            # If there is no node at the calculated index, the prefix is not in the trie
            if not curr_node.children[index]:
                return []

            # Move to the child node at the calculated index
            curr_node = curr_node.children[index]

        # Initialize an empty list to store the words that begin with the given prefix
        words = []

        # Call the helper function to traverse the trie starting from the current node and add all the words that begin with the prefix to the list
        self.traverse_trie(curr_node, prefix, words)

        # Return the list of words that begin with the given prefix
        return words


    #This function is a helper function for the get_all and begins_with functions. It traverses a trie data structure and adds all the words to a given list
    def traverse_trie(self, node, prefix, words):
        # If the current node marks the end of a valid word, add the word to the list
        if node.is_word_complete:
            words.append(prefix)

        # Iterate through the children of the current node
        for i in range(26):
            # If there is a child at the current index
            if node.children[i]:
                # Get the character represented by the current index
                ch = chr(i + ord('a'))

                # Recursively call the traverse_trie function with the child node, the prefix appended with the character, and the list of words
                self.traverse_trie(node.children[i], prefix + ch, words)