function calcular(){
    let x = document.getElementById("numero").value;
    let numero = parseInt(x);
    let resposta = document.getElementById("resposta");

    if (document.getElementById("tempCelsiusFahrenheit").checked){
        resposta.innerHTML=CelsiusParaFahrenheit(numero);
    }else if(document.getElementById("tempFahrenheitCelsius").checked){
        resposta.innerHTML=FahrenheitParaCalsius(numero);
    }
}

function CelsiusParaFahrenheit(num){
    let x = (1.8*num+32);
    return x;
}

function FahrenheitParaCalsius(num){
    let x = ((num-32)*5/9);
    return x;
}

function limparCampos(){
    document.getElementById("numero").value = "";
    let resposta = document.getElementById("resposta");
    resposta.innerHTML="";
    console.log("Limpar Campos")    
    }