<?php
class Rectangulo {
  public $base, $altura;

  public function getArea($base, $altura) {
    $this -> base = $base;
    $this -> altura = $altura;

    $res = $base * $altura;
    return $res;
  }
  public function getPerimetro($base, $altura) {
    $this -> base = $base;
    $this -> altura = $altura;

    $res = ($base * 2) + ($altura * 2);
    return $res;
  }
}
?>