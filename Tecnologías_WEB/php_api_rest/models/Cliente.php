<?php

require_once __DIR__ . '/../connection/Connection.php';

class Cliente {
  private $pdo;

  public function __construct() {
    $baseDatos = new Connection();
    $this->pdo = $baseDatos->getConnection();
  }

  public function getAll() {
    try {
      $sql = "SELECT * FROM clientes";
      $stmt = $this->pdo->query($sql);
      return $stmt->fetchAll();
    } catch (PDOException $e) {
      echo "Error: " . $e->getMessage();
    }
  }

  public function getWhere($id) {
    try {
      $sql = "SELECT * FROM clientes WHERE id = :id";
      $stmt = $this->pdo->prepare($sql);
      $stmt -> bindParam(':id', $id, PDO::PARAM_INT);
      $stmt -> execute();
      return $stmt->fetch();
    } catch (PDOException $e) {
      echo "Error: " . $e->getMessage();
    }
  }

  public function registrar($nombre, $apellidoPaterno, $apellidoMaterno, $fechaNacimiento, $genero) {
    $fechaNacimiento = (new DateTime($fechaNacimiento))->format('Y-m-d');
  
    try {
      $sql = "INSERT INTO clientes (nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, genero) 
              VALUES (:nombre, :apellidoPaterno, :apellidoMaterno, :fechaNacimiento, :genero)";
      $stmt = $this->pdo->prepare($sql);
      $stmt->bindParam(':nombre', $nombre, PDO::PARAM_STR);
      $stmt->bindParam(':apellidoPaterno', $apellidoPaterno, PDO::PARAM_STR);
      $stmt->bindParam(':apellidoMaterno', $apellidoMaterno, PDO::PARAM_STR);
      $stmt->bindParam(':fechaNacimiento', $fechaNacimiento, PDO::PARAM_STR);
      $stmt->bindParam(':genero', $genero, PDO::PARAM_STR);
      $stmt->execute();
      return $this->pdo->lastInsertId();
    } catch (PDOException $e) {
      error_log($e->getMessage(), 0);
      echo "Error: " . $e->getMessage();
      return false;
    }
  }
  
}
?>
