class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None
        
    def insert(self, route):
        if route not in self.children:
            self.children[route] = RouteTrieNode()

class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, route, handler, current_node = None):
        if not current_node:
            current_node = self.root
        t=route[0]

        if len(route) == 0:
            current_node.handler = handler
        elif len(route) == 1:
            current_node.insert(t)
            current_node.children[t].handler = handler
        else:
            current_node.insert(t)
            self.insert(route[1:], handler, current_node.children[t])
    

    def find(self, route, current_node = None):
        if not current_node:
            current_node = self.root
    
        if len(route) == 0:
            return current_node.handler
        else:
            if route[0] in current_node.children:
                return self.find(route[1:], current_node.children[route[0]])
            else:
                return None

 
class Router:
    def __init__(self, root_handler, not_found_handler):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.route_trie.insert(self.split_path(path), handler)
        

    def lookup(self, path):
        handler =  self.route_trie.find(self.split_path(path))
        
        if handler is None:
            return self.not_found_handler
        else:
            return handler

    def split_path(self, path):
        split_p = path.split('/')[1:]
        if len(split_p) == 0:
            return [] 
        if split_p[-1] == "":
            return split_p[:-1]
        return split_p

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route


# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one