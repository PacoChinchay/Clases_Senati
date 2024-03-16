<?php
require_once("./clases/Calculadora.php");
require_once("./clases/Rectangulo.php");
require_once("./clases/Pension.php");
require_once("./clases/Tarjeta.php");

$numero1 = $numero2 = $resultado = '';
$operacion = 'sumar'; 

if(isset($_POST["btn"])) {
  $numero1 = $_POST["numero1"];
  $numero2 = $_POST["numero2"];
  $operacion = $_POST["operacion"];

  if(is_numeric($numero1) && is_numeric($numero2)) {
    $calculadora = new Calculadora;
    switch ($operacion) {
      case 'sumar':
        $resultado = $calculadora -> getSuma($numero1, $numero2);
        break;
      case 'restar':
        $resultado = $calculadora -> getResta($numero1, $numero2);
        break;
      case 'multiplicar':
        $resultado = $calculadora -> getMultiplicacion($numero1, $numero2);
        break;
      case 'dividir':
        if ($numero2 != 0) {
          $resultado = $calculadora -> getDivision($numero1, $numero2);
        } else {
          $resultado = 'Error: División por cero.';
        }
        break;
    }
  } else {
    $resultado = 'Por favor, ingresa números válidos.';
  }
}

if(isset($_POST["btn2"])) {
  $base = $_POST["base"];
  $altura = $_POST["altura"];
  $operacion = $_POST["operacion2"];

  if(is_numeric($base) && is_numeric($altura)) {
    $rectangulo = new Rectangulo;
    switch ($operacion) {
      case 'area':
        $resultado = $rectangulo -> getArea($base, $altura);
        break;
      case 'perimetro':
        $resultado = $rectangulo -> getPerimetro($base, $altura);
        break;
    }
  } else {
    $resultado = "Por favor, ingresa números válidos.";
  }
}

if(isset($_POST["btn3"])) {
  $seguro = $_POST["seguro"];
  $sueldo = $_POST["sueldo"];

  if(isset($_POST["seguro"]) && is_numeric($sueldo)) {
    $pension = new Pension;
    $resultado = $pension -> getPension($sueldo, $seguro);
  }
}

if(isset($_POST["btn4"])) {
  $precio = $_POST["pelicula"];
  $tipo = $_POST["operacion3"];
  $entradas = $_POST["entradas"];
  $nombre = $_POST["nombre"];

  if(is_numeric($precio) && is_numeric($entradas)) {
    $tarjeta = new Tarjeta;
    $descuento = $tarjeta -> getDescuento($tipo);
    $precioTotal = $precio * $entradas;
    $descuentoTotal = $precioTotal * $descuento;
    $precioFinal = $precioTotal - $descuentoTotal;
  } else {
    $precioFinal = 'Por favor, ingresa un precio válido y la cantidad de entradas.';
  }
}


?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>POO</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Entregable 2</h1>

  <form action="" method="POST" class="form">
    <h2>Operador Aritmético</h2>
    <fieldset>
      <legend>Elija sus números</legend>
      <label>
        Número 1: <input type="number" name="numero1" value="<?= isset($_POST["btn"])? $_POST["numero1"]: '' ?>">
      </label>
      <label>
        Número 2: <input type="number" name="numero2" value="<?= isset($_POST["btn"])? $_POST["numero2"]: '' ?>">
      </label>
      <label>
        Operación a Realizar:
        <select name="operacion">
          <option value="sumar" <?= $operacion == 'sumar' ? 'selected' : '' ?>>Sumar</option>
          <option value="restar" <?= $operacion == 'restar' ? 'selected' : '' ?>>Restar</option>
          <option value="multiplicar" <?= $operacion == 'multiplicar' ? 'selected' : '' ?>>Multiplicar</option>
          <option value="dividir" <?= $operacion == 'dividir' ? 'selected' : '' ?>>Dividir</option>
        </select>
      </label>
    </fieldset>
    <div>
      <h3>Resultado:</h3>
      <?= isset($_POST["btn"])? $resultado : 'aún no envías una operación';?>
    </div>
    <button name="btn">Enviar</button>
  </form>

  <form action="" method="POST" class="form">
    <h2>Área y Perímetro</h2>
    <fieldset>
      <legend>Dimensiones</legend>
      <label>
        Base: <input type="number" name="base" value="<?= isset($_POST["btn2"])? $_POST["base"]: '' ?>">
      </label>
      <label>
        Altura: <input type="number" name="altura" value="<?= isset($_POST["btn2"])? $_POST["altura"]: '' ?>">
      </label>
      <label>
        Operación a Realizar:
        <select name="operacion2">
          <option value="area" <?= $operacion == 'area' ? 'selected' : '' ?>>Área</option>
          <option value="perimetro" <?= $operacion == 'perimetro' ? 'selected' : '' ?>>Perímetro</option>
        </select>
      </label>
    </fieldset>
    <div>
      <h3>Resultado de su figura:</h3>
      <?= isset($_POST["btn2"])? $resultado : 'ingrese las dimensiones';?>
    </div>
    <button name="btn2">Enviar</button>
  </form>

  <form action="" method="POST" class="form">
    <h2>Pensiones de Seguro</h2>
    <fieldset class="seguros">
    <legend>Plan de Seguro</legend>
    <div>
      <label>
        <input type="radio" name="seguro" value="0.025" <?= isset($_POST["seguro"]) && $_POST["seguro"] == "0.025" ? 'checked' : '' ?>> AFP PRIMA 2.5%
      </label>
      <br>
      <label>
        <input type="radio" name="seguro" value="0.03" <?= isset($_POST["seguro"]) && $_POST["seguro"] == "0.03" ? 'checked' : '' ?>> AFP HABITAT 3%
      </label>
      <br>
      <label>
        <input type="radio" name="seguro" value="0.05" <?= isset($_POST["seguro"]) && $_POST["seguro"] == "0.05" ? 'checked' : '' ?>> ONP 5%
      </label>
    </div>
    <label>
      Sueldo: <input type="number" name="sueldo" value="<?= isset($_POST["sueldo"]) ? $_POST["sueldo"] : '' ?>">
    </label>
    </fieldset>
    <div>
      <h3>Resultado:</h3>
      <?= isset($_POST["btn3"]) ? "Fecha: " . $resultado["Fecha"] . "<br>Hora: " . $resultado["Hora"] . "<br>Seguro: " . $resultado["Seguro"] . "<br>Pensión: " . $resultado["Pension"] : 'Aún no ingresa sus datos'?>
    </div>
    <button name="btn3">Enviar</button>    
  </form>

  <form action="" method="POST" class="form">
    <h2>CinePlanet</h2>
    <fieldset class="seguros">
      <legend>
        Películas
      </legend>
      <div>
        <label>
          <input type="radio" name="pelicula" value="12" <?= isset($_POST["pelicula"]) && $_POST["pelicula"] == "12" ? 'checked' : '' ?>> Rapidos y Furiosos X
        </label>
        <br>
        <label>
          <input type="radio" name="pelicula" value="10" <?= isset($_POST["pelicula"]) && $_POST["pelicula"] == "10" ? 'checked' : '' ?>> Destino Final 5 
        </label>
        <br>
        <label>
          <input type="radio" name="pelicula" value="11" <?= isset($_POST["pelicula"]) && $_POST["pelicula"] == "11" ? 'checked' : '' ?>> Ironman 3
        </label>
        <br>
        <label>
          <input type="radio" name="pelicula" value="13" <?= isset($_POST["pelicula"]) && $_POST["pelicula"] == "13" ? 'checked' : '' ?>> Thor 2
        </label>
      </div>
      <label>
        Tarjeta:
        <select name="operacion3" class="tarjetas">
          <option value="clasico" <?= $tipo == 'classico' ? 'selected' : '' ?>>Clasico</option>
          <option value="platino" <?= $tipo == 'platino' ? 'selected' : '' ?>>Platino</option>
          <option value="dorado" <?= $tipo == 'dorado' ? 'selected' : '' ?>>Dorado</option>
        </select>
      </label>
    </fieldset>
    <fieldset>
      <legend>Datos personales</legend>
      <label>
        Nombre: <input type="text" placeholder="Paco Chinchay" name="nombre">
      </label>
      <label>
        Entradas: <input type="number" name="entradas" value="<?= isset($_POST["entradas"]) ? $_POST["entradas"] : '' ?>">
      </label>
    </fieldset>
    <div>
      <h3>Resumen de la Compra:</h3>
      <?= isset($_POST["btn4"]) ? "Nombre: " . $_POST["nombre"] . "<br>Precio Total: " . $precioFinal . "<br>Descuento: " . $descuentoTotal : 'Aún no ingresa sus datos'?>
    </div>
    <button name="btn4">Enviar</button>
  </form>
</body>
</html>