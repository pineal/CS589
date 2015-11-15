from collections import OrderedDict

class MyOrderedDict(OrderedDict):
	def nextKey(self, key):
		print "Finding next key of: "+key
		next=self._OrderedDict__map[key][1]
		if next is self._OrderedDict__root:
			return self.firstKey()
		return next[2]
	def firstKey(self):
		for key in self: return key
		raise ValueError("OrderedDict() is empty")