<?php
if (isset($_GET['estado'])) {
    $estado = $_GET['estado'];
    file_put_contents("estado.txt", $estado);
    echo "Estado actualizado a: $estado";
} else {
    echo "Falta parámetro estado (usa ?estado=on o ?estado=off)";
}
?>
