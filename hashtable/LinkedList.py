class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        curStr = ""
        curr = self.head
        while curr is not None:
            curStr += f'{str(curr.value)} ->'
            curr = curr.next
        return curStr

    # runtime: O(1)
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    
    # Runtime: O(n) * O(1) = O(n)
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.get(node.value)
        if existingNode is not None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)

    # Runetime: O(n) n = num of nodes
    # Space: O(1) constant because space doesn't change based on input
    def delete(self, value):
        curr = self.head

        if curr.value == value:
            self.head = curr.next
            return curr
        
        prev = curr
        curr = curr.next

        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                cur = curr.next

        return None

    # runtime 0(n) n = number of nodes
    def get(self, value):
        curr = self.head

        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None
    
a = Node(1)
b = Node(2)
c = Node(3)
ll = LinkedList()
ll.insert_at_head(a)
ll.insert_at_head(b)
ll.insert_at_head(c)
ll.insert_at_head_or_overwrite(a)
ll.delete(2)
ll.delete(3)
ll.delete(1)
print(ll)