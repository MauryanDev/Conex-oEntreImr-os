document.addEventListener("DOMContentLoaded", () => {
    const categoriaEntrada = document.getElementById("categoria");
    const localEntrada = document.getElementById("local");
    const camposAlimentos = document.getElementById("campos-alimentos");
    const camposRoupas = document.getElementById("campos-roupas");
    const tamanhoRoupa = document.getElementById("tamanho-roupa");
    const pecaRoupa = document.getElementById("peca-roupa");

    function atualizarCamposDoacao() {
        if (!categoriaEntrada) return;

        const categoria = categoriaEntrada.value;
        const usaDespensa = ["alimentos", "higiene", "limpeza"].includes(categoria);
        const usaBazar = categoria === "roupas";

        if (camposAlimentos) {
            camposAlimentos.classList.toggle("is-visible", categoria === "alimentos");
        }
        
        if (camposRoupas) {
            camposRoupas.classList.toggle("is-visible", usaBazar);
        }

        if (tamanhoRoupa && pecaRoupa) {
            tamanhoRoupa.required = usaBazar;
            pecaRoupa.required = usaBazar;

            if (!usaBazar) {
                tamanhoRoupa.value = "";
                pecaRoupa.value = "";
            }
        }

        if (localEntrada) {
            if (usaDespensa) {
                localEntrada.value = "instituto";
            } else if (usaBazar) {
                localEntrada.value = "bazar";
            }
        }
    }

    if (categoriaEntrada) {
        categoriaEntrada.addEventListener("change", atualizarCamposDoacao);
        atualizarCamposDoacao();
    }
});