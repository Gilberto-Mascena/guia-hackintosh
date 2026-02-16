# 💻 Guia de Hardware Hackintosh (Brasil) 🇧🇷

Este repositório centraliza informações sobre a compatibilidade de componentes para a instalação do macOS. Diferente dos guias globais, focamos no hardware encontrado no mercado brasileiro.

!!! info "Dica de Navegação"
    Se você está planejando comprar peças novas, confira nosso [🛒 Guia de Compras](compras.md). Se tiver dúvidas rápidas, veja o [❓ FAQ](faq.md).

---

## 🚀 Por onde começar?

O sucesso do seu Hackintosh depende do suporte nativo da Apple aos componentes. 

### 🛠️ Processadores (CPU)

| Família | Status | Observação |
| :--- | :--- | :--- |
| **Intel 10ª Gen e anteriores** | ✅ Nativo | Melhor compatibilidade (iGPU funciona). |
| **Intel 11ª a 14ª Gen** | ⚠️ Parcial | iGPU **NÃO** funciona. Requer GPU dedicada AMD. |
| **AMD Ryzen** | ⚠️ Parcial | Requer patches de Kernel. Bugs em apps Adobe. |

---

## 🎮 Placas de Vídeo (GPU)

!!! tip "Regra de Ouro"
    NVIDIA apenas até a arquitetura Pascal (GTX 10xx) e apenas até o macOS High Sierra. Para sistemas modernos (Sonoma/Sequoia), **AMD é o único caminho.**

### 🟢 Recomendadas (Plug & Play)
* **Série RX 400/500:** RX 460, 470, 480, 560, 570, 580, 590.
* **Série RX 5000:** RX 5500, 5600, 5700 (XT).
* **Série RX 6000:** RX 6600, 6800, 6900 XT (Atenção: 6700 XT **NÃO** é compatível).

### 🔴 Incompatíveis
* **AMD Séries "Lexa":** Algumas RX 550 de entrada.
* **NVIDIA RTX/GTX 16xx:** Sem suporte em nenhuma versão recente.

---

## 🚫 Hardware "Cilada" no Brasil

!!! danger "Cuidado com estes componentes"
    1. **SSDs NVMe Samsung PM981 / Micron:** Causam lentidão extrema e Kernel Panics.
    2. **Laptops 144Hz+ sem Switch MUX:** A bateria terá duração curtíssima.
    3. **GPUs XFX Antigas:** Podem precisar de reflash de BIOS.

---

## 🧪 Teste de Compatibilidade

Rode nosso script de análise rápida para validar seu hardware atual:

1. Tenha o **Python** instalado.
2. No terminal, execute:
    ```bash
    python scripts/check_compatibilidade.py
    ```

---

## 📦 Tax Remessa Conforme

!!! note "Economia Inteligente"
    Com as taxas atuais, vale a pena importar **CPU e RAM** (AliExpress). Placas-mãe e Gabinetes costumam ser mais vantajosos em lojas nacionais (Kabum, Terabyte, Pichau).

---

## 🤝 Como contribuir
Encontrou um hardware que funciona? Ajude a comunidade!

1. Faça um **Fork** do projeto.
2. Crie uma **Issue** relatando o hardware.
3. Envie um **Pull Request**.

---

## 📄 [Licença](licenca.md)
Este guia é distribuído sob a licença MIT.