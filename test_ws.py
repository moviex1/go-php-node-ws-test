import asyncio
import websockets
import time
import statistics
from concurrent.futures import ThreadPoolExecutor

class WebSocketPerformanceTester:
    def __init__(self, uri, num_connections=150, messages_per_connection=100, message_size=100):
        self.uri = uri
        self.num_connections = num_connections
        self.messages_per_connection = messages_per_connection
        self.message_size = message_size
        self.message = 'a' * message_size

    async def connection_test(self):
        start_time = time.time()
        async with websockets.connect(self.uri) as websocket:
            pass
        return time.time() - start_time

    async def latency_test(self):
        async with websockets.connect(self.uri) as websocket:
            start_time = time.time()
            await websocket.send(self.message)
            await websocket.recv()
            return time.time() - start_time

    async def throughput_test(self):
        async with websockets.connect(self.uri) as websocket:
            start_time = time.time()
            for _ in range(self.messages_per_connection):
                await websocket.send(self.message)
                await websocket.recv()
            return self.messages_per_connection / (time.time() - start_time)

    async def run_tests(self):
        print(f"Testing WebSocket server at {self.uri}")
        print(f"Number of connections: {self.num_connections}")
        print(f"Messages per connection: {self.messages_per_connection}")
        print(f"Message size: {self.message_size} bytes")
        print("\nRunning tests...\n")

        # Connection time test
        connection_times = await asyncio.gather(*[self.connection_test() for _ in range(self.num_connections)])
        avg_connection_time = statistics.mean(connection_times)
        print(f"Average connection time: {avg_connection_time:.6f} seconds")

        # Latency test
        latencies = await asyncio.gather(*[self.latency_test() for _ in range(self.num_connections)])
        avg_latency = statistics.mean(latencies)
        print(f"Average latency: {avg_latency:.6f} seconds")

        # Throughput test
        throughputs = await asyncio.gather(*[self.throughput_test() for _ in range(self.num_connections)])
        avg_throughput = statistics.mean(throughputs)
        total_throughput = sum(throughputs)
        print(f"Average throughput per connection: {avg_throughput:.2f} messages/second")
        print(f"Total throughput: {total_throughput:.2f} messages/second")

async def main():
    servers = [
        "ws://localhost:8082/",  # Go WebSocket server
        "ws://localhost:8081/",  # Go WebSocket server
        "ws://localhost:8080/"      # PHP WebSocket server
    ]

    for server in servers:
        tester = WebSocketPerformanceTester(server)
        await tester.run_tests()
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    asyncio.run(main())
