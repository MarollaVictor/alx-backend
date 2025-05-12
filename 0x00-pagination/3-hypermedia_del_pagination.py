#!/usr/bin/env python3
server = Server()
print(server.get_hyper(3000, 100))
# Output: {'page_size': 0, 'page': 3000, 'data': [], ... 'total_pages': 195}