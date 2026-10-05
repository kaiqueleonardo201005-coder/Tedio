const senhaInput = document.getElementById("senha");
const mascara = document.getElementById("mascara");
const status = document.getElementById("status");
const mensagem = document.getElementById("mensagem");

async function verificarServidor() {
    try {
        const resposta = await fetch("/status");

        if (resposta.ok) {
            status.textContent = "ONLINE";
        } else {
            status.textContent = "ERRO";
        }
    } catch {
        status.textContent = "OFFLINE";
    }
}

senhaInput.addEventListener("input", () => {
    if (senhaInput.value.length === 0) {
        mascara.textContent = "******";
    } else {
        mascara.textContent = "*".repeat(senhaInput.value.length);
    }
});

async function salvarSenha() {
    const senha = senhaInput.value;

    if (senha.length === 0) {
        mensagem.textContent = "ERRO: digite uma senha.";
        return;
    }

    try {
        const resposta = await fetch("/salvar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                senha: senha
            })
        });

        const dados = await resposta.json();

        if (dados.ok) {
            mensagem.textContent = "SENHA DE TESTE SALVA.";
            senhaInput.value = "";
            mascara.textContent = "******";
        } else {
            mensagem.textContent = "ERRO AO SALVAR.";
        }

    } catch {
        mensagem.textContent = "ERRO: servidor offline.";
    }
}

verificarServidor();