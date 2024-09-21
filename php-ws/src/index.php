<?php

namespace Nikitazubkov\TestWs;

use Ratchet\Server\IoServer;
use Ratchet\Http\HttpServer;
use Ratchet\WebSocket\WsServer;
use Ratchet\MessageComponentInterface;
use Ratchet\ConnectionInterface;

require __DIR__ . '/../vendor/autoload.php';

class EchoServer implements MessageComponentInterface {
    protected $clients;

    public function __construct() 
    {
        $this->clients = new \SplObjectStorage;
    }

    public function onOpen(ConnectionInterface $conn): void 
    {
        $this->clients->attach($conn);
    }

    public function onMessage(ConnectionInterface $from, $msg): void 
    {
        foreach ($this->clients as $client) {
            if ($from === $client) {
                $client->send($msg);
            }
        }
    }

    public function onClose(ConnectionInterface $conn): void 
    {
        $this->clients->detach($conn);
    }

    public function onError(ConnectionInterface $conn, \Exception $e): void 
    {
        $conn->close();
    }
}

$server = IoServer::factory(
    new HttpServer(
        new WsServer(
            new EchoServer()
        )
    ),
    8080
);

echo "PHP WebSocket server running on port 8080\n";
error_reporting(E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED);
$server->run();
