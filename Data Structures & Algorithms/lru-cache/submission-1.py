class Node:
    def __init__(self, key, val):
        self.key = key  # Key to identify the node (used for hashmap lookup)
        self.val = val  # Value stored in the node
        self.prev = None  # Pointer to the previous node in the doubly linked list
        self.next = None  # Pointer to the next node in the doubly linked list

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity  # Maximum capacity of the cache
        self.cache = {}  # Hashmap to map keys to their corresponding nodes

        # Initialize dummy nodes to mark the boundaries of the doubly linked list
        # left.next = LRU (least recently used), right.prev = MRU (most recently used)
        self.left = Node(0, 0)  # Dummy head (leftmost node)
        self.right = Node(0, 0)  # Dummy tail (rightmost node)
        
        # Connect the dummy nodes initially (empty list: left <-> right)
        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the doubly linked list
    def remove(self, node):
        # Get the previous and next nodes of the target node
        prev_node = node.prev
        next_node = node.next
        
        # Bypass the target node by linking prev_node and next_node directly
        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert a node at the MRU (rightmost) position of the list
    def insert(self, node):
        # The node to be inserted will be placed just before the dummy tail (self.right)
        prev_node = self.right.prev  # Current MRU node
        next_node = self.right  # Dummy tail
        
        # Update pointers to insert the new node
        prev_node.next = node
        next_node.prev = node
        node.prev = prev_node
        node.next = next_node

    # Retrieve a value from the cache
    def get(self, key: int) -> int:
        if key in self.cache:
            # If the key exists, move its node to MRU (since it was recently accessed)
            self.remove(self.cache[key])  # Remove from current position
            self.insert(self.cache[key])  # Re-insert at MRU
            return self.cache[key].val  # Return the value
        return -1  # Key not found

    # Insert or update a key-value pair in the cache
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If key exists, remove its node (to update its position later)
            self.remove(self.cache[key])
        
        # Create a new node and add it to the cache (and MRU position)
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If capacity is exceeded, evict the LRU node (left.next)
        if len(self.cache) > self.cap:
            lru_node = self.left.next  # The LRU node (leftmost real node)
            self.remove(lru_node)  # Remove from the list
            del self.cache[lru_node.key]  # Remove from the hashmap