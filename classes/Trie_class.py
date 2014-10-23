class TrieNode:
	"""docstring for TrieNode"""
	def __init__(self):
		self.word = None
		self.children = {} # key: c, value: TrieNode object
	

class Trie(object):
	"""Trie is also known as prefix tree, as it can be searched by prefixes. 

	No node in the tree stores the key associated with that node; 
	instead, its position in the tree defines the key with which it is associated.

	All the children of a node have a common prefix of the string associated 
	with that node, and the root is associated with the empty string. 

	Trie can be relatively slow, but can look for data faster in the worst case.
	And it also require more space in memory.
	(Compare with hash table)
	"""
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		node = self.root
		for c in word:
			if c not in node.children:
				node.children[c] = TrieNode()
			node = node.children[c]
		node.word = word

	def delete(self, word, node = None, i = 0):
		node = self.root if not node else node
		c = word[i]
		if c in node.children:
			child_node = node.children[c]
			if len(word) - 1 == i:
				return node.children.pop(c) 
			else:
				return self.delete(word, child_node, i + 1)
			# if len(child_node.children) == 0:
			# 	node.children.pop(c)
		else:
			return False

	def SearchByExactWord(self, word):
		node = self.root
		for c in word:
			if c not in node.children:
				print 'No such word found!'
				# raise ValueError 'word'
				return (False, None)
			node = node.children[c]
		if node.word != word:
			return (False, None)
		return (True, node.word)

	def SearchByPrefix(self, prefix):
		node = self.root
		self.results = []
		for c in prefix:
			if c not in node.children:
				return (False, None)
			node = node.children[c]
		self.DFS(node)
		return self.results

	def PrintWords(self):
		'''Print all the words'''
		self.results = []
		self.DFS(self.root)
		return self.results

	def DFS(self, node):
		if node.word:
			self.results.append(node.word)
		if node.children == {}:
			return
		for i in xrange(0, len(node.children)):
			self.DFS(node.children[node.children.keys()[i]])

if __name__ == '__main__':
	trie = Trie()
	trie.insert('to')
	trie.insert('A')
	trie.insert('tea')
	trie.insert('ted')
	trie.insert('inn')
	trie.insert('AB')
	trie.insert('i')

	print trie.PrintWords()

	print trie.SearchByExactWord('ted')
	print trie.SearchByExactWord('inn')
	print trie.SearchByExactWord('in')  

	print trie.SearchByPrefix('t')
	print trie.SearchByPrefix('te')
	print trie.SearchByPrefix('ted')

	trie.delete('AB')
	print trie.PrintWords()

	trie.delete('ted')
	print trie.PrintWords()

	trie.delete('inn')
	print trie.PrintWords()











		
		