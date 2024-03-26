class DeleteSolution:
    def deleteNode(del_node):
        #code here
        if del_node is None:
            return None
        '''
        Approach:
        1. create nodes pointing to node and next node
        2. copy the data of the next node to the current node
        3. point the current node to next of next node
        '''
            
        currentNode = del_node
        nextNode = del_node.next
        
        if nextNode is None:
            currentNode = None
        else:
            currentNode.data = nextNode.data
            currentNode.next = nextNode.next