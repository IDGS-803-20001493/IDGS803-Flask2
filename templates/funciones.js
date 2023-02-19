function generarCasillas(){
var casillas = $("#numeroCasillas").val();

var i = 0;
do {
    $("#contenedor").html('{{render_caja("txtNumero","Numero 1",type="number")}}');
    i = i + 1;
} while (i < casillas);
}
