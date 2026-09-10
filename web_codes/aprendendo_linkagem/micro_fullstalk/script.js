const entrada1 = document.getElementById("capturaIdade");
const result = document.getElementById("resultadoidade");
const botao = document.getElementById("verificaridade");

const escolhas = ["pedra", "papel", "tesoura"];

function escolhaComputador() {
    const escolhasistema = Math.floor(Math.random() * escolhas.length);
    return escolhas[escolhasistema]; 
}

botao.addEventListener("click", function(){

    const escolha = entrada1.value.toLowerCase().trim();
    const pc = escolhaComputador();

    
    if (!escolhas.includes(escolha)) {
        result.innerText = "escolha invalida negao"
        result.style.color = "black"
    } 
    else if (escolha === pc){
        result.innerText = "empate"
        result.style.color = "blue"
    }
    else if (escolha === "papel" && pc === "pedra" ||
             escolha === "tesoura" && pc === "papel" ||
             escolha === "pedra" && pc === "tesoura")
    {
    result.innerText = `vitoria meu amigooo o computador escolheu ${pc} bora que bora`
    result.style.color = "red"
    }
    else {
        result.innerText = `voce perdeu amigo a jogada foi ${pc}`
        result.style.color = "black"
    }
})