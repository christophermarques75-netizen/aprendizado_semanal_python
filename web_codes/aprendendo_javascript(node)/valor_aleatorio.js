const opcoes = ["pedra", "papel", "tesoura"];

function escolhaComputador() {
  const indiceAleatorio = Math.floor(Math.random() * opcoes.length);
  return opcoes[indiceAleatorio];
}

console.log(escolhaComputador());
