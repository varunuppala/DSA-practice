"""
huffman trial
"""
import os
from pprint import pprint

class Node:
	"""
	Creating a class for the nodes
	prob : is the probablity of it appearing
	char : is the character we are storing
	left : intially None
	right : intially None
	code : encoded code
	"""
	def __init__(self, prob, char, left=None, right=None):
		# probability of character
	    self.prob = prob

	    # character 
	    self.char = char

	    # left node
	    self.left = left

	    # right node
	    self.right = right

	    # Code of each
	    self.code = ''

def huffmancode(data1):
	"""
	Calculating the huffman code
	1. Calculating the probablities
	2. Creating a node for each character with its probabilty 
	3. Iterating over the nodes,sorting them,combining and adding the new one.
	4. After the new is added remove the previous two
	5. repeat till one char is left
	6. Finding the encoded code for each character
	7. Finding the bit size of the data
	"""
	
	data = calculateProbability(data1)	
	nodes = []


	for char,prob in data.items():
		nodes.append(Node(prob,char))

	while len(nodes)>1:

		# Sorting the nodes first
		nodes = sorted(nodes, key=lambda x: x.prob)

		# Picking two least two nodes
		right = nodes[0]
		left = nodes [1]


		# intiating the codes for the least characters to be 0 and 1
		left.code,right.code = 0,1

		# Creating a new node by combining the two least ones
		newchar = Node(left.prob+right.prob,left.char+right.char,left,right)

		nodes.remove(left)
		nodes.remove(right)
		nodes.append(newchar)



	huffmancodestring = calculateCodes(nodes[0])
	encodedsize(data1,huffmancodestring)


def encodedsize(data,huffman):
	"""
	Find the len of original data
	Finding the size of the encoded string
	"""
	original = len(data)*8
	compressed = 0
	for char in huffman:
		count = data.count(char)
		compressed += count*len(huffman[char])

	print("Before encoding :",original,"bits")
	print("After encoding :",compressed,"bits")

# To store the codes
codes = {}
def calculateCodes(node, val=''):
	"""
	assigning codes to each of the character in the tree
	"""
    
    newchar = value + str(node.code)

    if(node.left):
        Calculate_Codes(node.left, newchar)
    if(node.right):
        Calculate_Codes(node.right, newchar)

    if(not node.left and not node.right):
        codes[node.char] = newchar
         
    return codes        


def calculateProbability(data):
	"""
	returns counts
	"""
	prob = {}
	for i in data:
		if i in prob:
			prob[i] += 1
		else:
			prob[i] = 1

	return prob


def main():
	"""
	Opening tht file given
	"""
    with open('huffinput.txt', 'r') as file:
        data = file.read().replace('\n', '')

    huffmancode(data)
	



if __name__ == "__main__":
	main()



