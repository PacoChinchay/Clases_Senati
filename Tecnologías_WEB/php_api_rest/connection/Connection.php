<?php
class Connection {
  private $host = "localhost";
  private $usuario = "root";
  private $password = "";
  private $baseDatos = "api_rest";
  private $dsn;
  private $pdo;

  public function __construct() {
    $this->dsn = 'mysql:host=' . $this->host . ';dbname=' . $this->baseDatos;
    try {
      $this->pdo = new PDO($this->dsn, $this->usuario, $this->password);
      $this->pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_OBJ);
      $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOException $e) {
      echo "Error: " . $e->getMessage();
      die();
    }
  }

  public function getConnection() {
    return $this->pdo;
  }
}