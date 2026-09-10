const entrada1 = document.getElementById("capturaIdade");

const result = document.getElementById("resultadoidade");

const botao = document.getElementById("verificaridade");

botao.addEventListener("click", function(){

    const idade = Number(entrada1.value);

    if (idade <= 18) {
        result.innerText = "deu errado mano volta quando for maior de idade";
        result.style.color = "red";
    } else {
        result.innerText = "deu certo meu carreto pode ir";
        result.style.color = "black";
    }
});