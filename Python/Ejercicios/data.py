clientes = [
  {"dni_cliente": "12345678", 
   "nombre_cliente": "Juan Perez", 
   "direccion_cliente": "Av. Siempre Viva 123", 
   "distrito": "Lima"},
  {"dni_cliente": "87654321", 
   "nombre_cliente": "María López", 
   "direccion_cliente": "Calle Falsa 456", 
   "distrito": "Miraflores"},
  {"dni_cliente": "23456789", 
   "nombre_cliente": "Carlos García", 
   "direccion_cliente": "Jr. Los Olivos 789", 
   "distrito": "Surco"},
  {"dni_cliente": "98765432", 
   "nombre_cliente": "Ana Torres", 
   "direccion_cliente": "Av. Las Palmeras 101", 
   "distrito": "San Isidro"}
]

cuentas = [
  {"numero_cuenta": "001-123456", 
   "tipo_cuenta": "Ahorros", 
   "moneda": "Soles", 
   "saldo_actual": 5500.00, 
   "dni_cliente": "12345678"},
  {"numero_cuenta": "002-876543", 
   "tipo_cuenta": "Corriente", 
   "moneda": "Dólares", 
   "saldo_actual": 2350.50, 
   "dni_cliente": "87654321"},
  {"numero_cuenta": "003-234567",
   "tipo_cuenta": "Ahorros", 
   "moneda": "Soles", 
   "saldo_actual": 250.75, 
   "dni_cliente": "23456789"},
  {"numero_cuenta": "004-987654", 
   "tipo_cuenta": "Corriente", 
   "moneda": "Soles", 
   "saldo_actual": 17000.00, 
   "dni_cliente": "98765432"}
]

movimientos = [
  {"numero_cuenta": "001-123456", 
   "fecha_operacion": "2024-11-05", 
   "descripción": "Depósito en efectivo", 
   "numero_operacion": "0001", 
   "tipo_operacion": "Depósito", 
   "importe": 500.00, 
   "saldo_contable": 500.00},
  {"numero_cuenta": "001-123456", 
   "fecha_operacion": "2024-11-06", 
   "descripción": "Retiro en cajero", 
   "numero_operacion": "0002", 
   "tipo_operacion": "Retiro", 
   "importe": 300.00, 
   "saldo_contable": 200.00},
  {"numero_cuenta": "001-123456", 
   "fecha_operacion": "2024-11-07", 
   "descripción": "Transferencia recibida", 
   "numero_operacion": "0003", 
   "tipo_operacion": "Depósito", 
   "importe": 800.00, 
   "saldo_contable": 1000.00},
  
  {"numero_cuenta": "002-876543", 
   "fecha_operacion": "2024-11-08", 
   "descripción": "Retiro en cajero", 
   "numero_operacion": "0004", 
   "tipo_operacion": "Retiro", 
   "importe": 200.00, 
   "saldo_contable": 2300.50},
  {"numero_cuenta": "002-876543", 
   "fecha_operacion": "2024-11-09", 
   "descripción": "Depósito en efectivo", 
   "numero_operacion": "0005", 
   "tipo_operacion": "Depósito", 
   "importe": 100.00, 
   "saldo_contable": 2400.50},
  {"numero_cuenta": "002-876543", 
   "fecha_operacion": "2024-11-10", 
   "descripción": "Pago de servicio", 
   "numero_operacion": "0006", 
   "tipo_operacion": "Retiro", 
   "importe": 50.00, 
   "saldo_contable": 2350.50},

  {"numero_cuenta": "003-234567", 
   "fecha_operacion": "2024-11-11", 
   "descripción": "Depósito por venta", 
   "numero_operacion": "0007", 
   "tipo_operacion": "Depósito", 
   "importe": 100.00, 
   "saldo_contable": 200.75},
  {"numero_cuenta": "003-234567", 
   "fecha_operacion": "2024-11-12", 
   "descripción": "Retiro por cajero", 
   "numero_operacion": "0008", 
   "tipo_operacion": "Retiro", 
   "importe": 50.00, 
   "saldo_contable": 150.75},
  {"numero_cuenta": "003-234567", 
   "fecha_operacion": "2024-11-13", 
   "descripción": "Depósito en efectivo", 
   "numero_operacion": "0009", 
   "tipo_operacion": "Depósito", 
   "importe": 100.00, 
   "saldo_contable": 250.75},

  {"numero_cuenta": "004-987654", 
   "fecha_operacion": "2024-11-09", 
   "descripción": "Depósito de nómina", 
   "numero_operacion": "0010", 
   "tipo_operacion": "Depósito", 
   "importe": 5000.00, 
   "saldo_contable": 20000.00},
  {"numero_cuenta": "004-987654", 
   "fecha_operacion": "2024-11-11", 
   "descripción": "Pago de tarjeta", 
   "numero_operacion": "0011", 
   "tipo_operacion": "Retiro", 
   "importe": 1000.00, 
   "saldo_contable": 19000.00},
  {"numero_cuenta": "004-987654", 
   "fecha_operacion": "2024-11-13", 
   "descripción": "Compra en supermercado", 
   "numero_operacion": "0012", 
   "tipo_operacion": "Retiro", 
   "importe": 2000.00, 
   "saldo_contable": 17000.00}
]
