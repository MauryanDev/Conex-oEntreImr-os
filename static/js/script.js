function alternarSecao(secao) {
    const secoes = ["painel", "entrada", "baixa"];

    secoes.forEach((item) => {
        document.getElementById(`secao-${item}`).classList.toggle("active-section", item === secao);
        document.getElementById(`nav-${item}`).classList.toggle("active", item === secao);
    });
}

const categoriaEntrada = document.getElementById("categoria");
const localEntrada = document.getElementById("local");
const camposAlimentos = document.getElementById("campos-alimentos");
const camposRoupas = document.getElementById("campos-roupas");
const tamanhoRoupa = document.getElementById("tamanho-roupa");
const pecaRoupa = document.getElementById("peca-roupa");

function atualizarCamposDoacao() {
    if (!categoriaEntrada) {
        return;
    }

    const categoria = categoriaEntrada.value;
    const usaDespensa = ["alimentos", "higiene", "limpeza"].includes(categoria);
    const usaBazar = categoria === "roupas";

    camposAlimentos?.classList.toggle("is-visible", categoria === "alimentos");
    camposRoupas?.classList.toggle("is-visible", usaBazar);

    if (tamanhoRoupa && pecaRoupa) {
        tamanhoRoupa.required = usaBazar;
        pecaRoupa.required = usaBazar;

        if (!usaBazar) {
            tamanhoRoupa.value = "";
            pecaRoupa.value = "";
        }
    }

    if (localEntrada && usaDespensa) {
        localEntrada.value = "instituto";
    } else if (localEntrada && usaBazar) {
        localEntrada.value = "bazar";
    }
}

categoriaEntrada?.addEventListener("change", atualizarCamposDoacao);
atualizarCamposDoacao();

// Converte input type="month" (YYYY-MM) para MM/YYYY que o backend espera
const inputMes = document.getElementById("mes");
if (inputMes) {
    inputMes.addEventListener("change", function () {
        const [ano, mes] = this.value.split("-");
        if (ano && mes) {
            const hidden = document.createElement("input");
            hidden.type = "hidden";
            hidden.name = "mes";
            hidden.value = `/`;
            this.name = "_mes_raw";
            this.closest("form").appendChild(hidden);
        }
    });
}
