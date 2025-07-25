<?php
// Simple PHP server for e-commerce API

header('Content-Type: application/json');

$method = $_SERVER['REQUEST_METHOD'];
$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

$productsFile = __DIR__ . '/data/products.json';
$products = json_decode(file_get_contents($productsFile), true);

function jsonResponse($data, $status = 200) {
    http_response_code($status);
    echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    exit;
}

if ($path === '/health') {
    jsonResponse(['status' => 'healthy']);
}

if (strpos($path, '/api/products') === 0) {
    $parts = explode('/', trim($path, '/'));
    if ($method === 'GET' && count($parts) === 2) {
        // GET /api/products
        jsonResponse($products);
    } elseif ($method === 'GET' && count($parts) === 3) {
        // GET /api/products/{id}
        $id = $parts[2];
        foreach ($products as $p) {
            if ($p['id'] === $id) {
                jsonResponse($p);
            }
        }
        jsonResponse(['error' => 'Product not found'], 404);
    } elseif ($method === 'POST' && count($parts) === 2) {
        // POST /api/products (admin token check)
        $auth = $_SERVER['HTTP_AUTHORIZATION'] ?? '';
        if ($auth !== 'Bearer admin') {
            jsonResponse(['error' => 'Admin token required'], 403);
        }
        $input = json_decode(file_get_contents('php://input'), true) ?? [];
        $input['id'] = (string)(count($products) + 1);
        $products[] = $input;
        file_put_contents($productsFile, json_encode($products, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));
        jsonResponse($input, 201);
    } else {
        jsonResponse(['error' => 'Not implemented'], 400);
    }
}

if ($path === '/api/categories' && $method === 'GET') {
    $categories = array_values(array_unique(array_column($products, 'category')));
    jsonResponse(['categories' => $categories]);
}

jsonResponse(['error' => 'Not found'], 404);
