class SimpleBalancer:
    def __init__(self, server_list):
        self.server_list = server_list
        self.index = 0

    def next_server(self):
        server = self.server_list[self.index]
        self.index = (self.index + 1) % len(self.server_list)
        return server


# List of servers
servers = ["Server1", "Server2", "Server3"]

# Create the balancer
balancer = SimpleBalancer(servers)

# Handle some requests
for i in range(10):
    server = balancer.next_server()
    print(f"Request {i + 1}: Sent to {server}")