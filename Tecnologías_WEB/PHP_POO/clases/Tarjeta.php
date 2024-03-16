<?php
class Tarjeta {
  public $tipo, $descuento;

  public function getDescuento($tipo) {
    $this -> tipo = $tipo;

    switch ($tipo) {
      case 'clasico':
        $this -> descuento = 0.01;
        break;
      case 'platino':
        $this -> descuento = 0.035;
        break;
      case 'dorado':
        $this -> descuento = 0.06;
        break;
      default:
        $this -> descuento = 0;
        break;
    }

    return $this -> descuento;
  }
}
?>
