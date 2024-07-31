<?php

require_once __DIR__ . '/models/Cliente.php';

$cliente = new Cliente();
$clientes = $cliente->getAll();

foreach ($clientes as $c) {
  echo $c->nombre . "<br>";
}

$resultado = $cliente->getWhere(2);

if ($resultado) {
  echo "<br>" . $resultado->apellidoMaterno . "<br>";
} else {
  echo "No se encontró el cliente.";
}
?>

