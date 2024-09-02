let total = 0;
function adicionarCarrinho() {
    let preco = 0;
    let valor = 0;
    let fruta = document.getElementById("fruta").value.trim();
    let qtd = document.getElementById("quantidade").value;
    switch (fruta) {
        case ("Banana"):
            preco = 2;
            valor = (qtd * preco);
            total = total + valor;
            break;
        case ("Laranja"):
            preco = 1.5;
            valor = (qtd * preco);
            total = total + valor;
            break;
        case ("Maçã"):
            preco = 3;
            valor = (qtd * preco);
            total = total + valor;
            break;
        default:
            preco = 5;
            valor = (qtd * preco);
            total = total + valor;
            break;
    }
    if (qtd < 1) {
        alert("insira a quantidade do produto (dever ser maior q 1!)");
        document.getElementById("quantidade").value = null;
    } else {
        let produtos = document.createElement("div", id = "produtos");
        produtos.style = 'word-break: break-all;';
        produtos.innerHTML = qtd + 'x' + ' ' + fruta + ' - R$ ' + valor.toFixed(2);
        document.getElementById("carrinho").appendChild(produtos);
        let resultado = document.getElementById("total");
        resultado.innerHTML = "TOTAL:<b> R$ " + total.toFixed(2) + "</b>";
    }
}