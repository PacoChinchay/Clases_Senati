<?php

class Calculadora {
  public $num1, $num2;

  public function getSuma($num1, $num2) {
    $this -> num1 = $num1;
    $this -> num2 = $num2;

    $res = $num1 + $num2;
    return $res;
  }

  public function getResta($num1, $num2) {
    $this -> num1 = $num1;
    $this -> num2 = $num2;
    
    $res = $num1 - $num2;
    return $res;
  }

  public function getMultiplicacion($num1, $num2) {
    $this -> num1 = $num1;
    $this -> num2 = $num2;
    
    $res = $num1 * $num2;
    return $res;
  }  
  
  public function getDivision($num1, $num2) {
    $this -> num1 = $num1;
    $this -> num2 = $num2;
    
    $res = $num1 / $num2;
    return $res;
  }
}

?>