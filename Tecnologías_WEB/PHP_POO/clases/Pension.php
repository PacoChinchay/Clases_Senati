<?php
class Pension {
  public $sueldo, $pension;

  public function getPension($sueldo, $pension) {
    $this -> sueldo = $sueldo;
    $this -> pension = $pension;
    $res = $sueldo * $pension;
    $seguro = '';
  
    if($pension == 0.03) {
      $seguro = 'AFP HABITAT';
    } else if($pension == 0.025) {
      $seguro = 'AFP PRIMA';
    } else if($pension == 0.05) {
      $seguro = 'ONP';
    }
  
    $fecha = date("Y-m-d");
    $hora = date("H:i:s");
  
    return array(
      "Fecha" => $fecha,
      "Hora" => $hora,
      "Seguro" => $seguro,
      "Pension" => $res
    );
  }
  
}
?>