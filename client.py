import random

class LoadBalancer:
    def __init__(self):
        self.servers = {}

    def add_server(self, name):
        # Add a new server with 0 connections
        self.servers[name] = 0

    def pick_server(self):
        # Pick the server with the fewest connections
        least_connections = float('inf')
        chosen_server = None

        for server, connections in self.servers.items():
            if connections < least_connections:
                least_connections = connections
                chosen_server = server

        # Increase the connection count for the chosen server
        if chosen_server:
            self.servers[chosen_server] += 1

        return chosen_server


# Create a load balancer
lb = LoadBalancer()

# Add servers
lb.add_server("Server1")
lb.add_server("Server2")
lb.add_server("Server3")

# Add some random starting connections
for i in range(3):
    server = random.choice(["Server1", "Server2", "Server3"])
    lb.servers[server] += random.randint(1, 5)

# Simulate requests
for i in range(10):
    server = lb.pick_server()
    print(f"Request {i + 1}: Sent to {server}")
    print(f"Current Connections: {lb.servers}")
