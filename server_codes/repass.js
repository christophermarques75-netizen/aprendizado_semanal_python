document.getElementById('enviar').addEventListener('click', async () => {
    const meuObjeto = { nome: "Maria", idade: 30 };

    const resposta = await fetch('http://localhost:5000/receber-dados', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(meuObjeto)
    });

    const resultado = await resposta.json();
    console.log(resultado);
});