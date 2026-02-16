# 🛒 Guia de Compras Hackintosh (2026)

Este guia foca em componentes com o melhor custo-benefício, priorizando o mercado de usados (OLX/Marketplace) e a importação estratégica via AliExpress.

---

## ⚡ 1. O Combo "Custo-Benefício" (AliExpress)

Se o orçamento está apertado, a 10ª Geração Intel é o "ponto doce" para Hackintosh, pois permite usar o sistema sem placa de vídeo dedicada inicialmente.

| Componente | Recomendação | Por que escolher? |
| :--- | :--- | :--- |
| **CPU** | **i5-10400** ou **i7-10700** | Suporte 100% nativo à iGPU (UHD 630). |
| **Placa-Mãe** | **B460M** ou **H410M** | Marcas como ASUS, MSI ou Gigabyte facilitam patches ACPI. |
| **RAM** | **16GB DDR4 3200MHz** | Marcas: Juhor, Asgard ou Netac (estáveis e baratas). |

!!! info "Sobre Placas-Mãe Chinesas (Huananzhi, Machinst, etc)"
    Embora baratas, elas costumam ter BIOS limitadas e tabelas ACPI bagunçadas, o que exige muito mais trabalho de correção manual na sua EFI.

---

## 🎮 2. Placa de Vídeo (GPU)

Para rodar sistemas modernos como o **macOS Sequoia** com aceleração de hardware total, você precisará de uma GPU AMD.

### 💰 Opções no Mercado de Usados (OLX/Marketplace)

* **Ultra-Budget: AMD Radeon RX 560 (4GB)**
    * **Preço médio:** R$ 300 - R$ 450
    * **Status:** Nativa, ideal para produtividade e edição leve.
* **Equilibrada: AMD Radeon RX 6600**
    * **Preço médio:** R$ 1.100 - R$ 1.300
    * **Status:** Performance excelente, arquitetura moderna e suporte total.

!!! danger "Cuidado com a RX 580 '2048SP'"
    Muito comum no AliExpress, este modelo é na verdade uma RX 570 "disfarçada" e **não funciona nativamente**. Exige troca de BIOS (VBIOS Flash), o que pode inutilizar a placa se feito incorretamente.

---

## 💾 3. Armazenamento (NVMe e SATA)

Um SSD incompatível é a causa principal de *Kernel Panics* aleatórios e lentidão no boot.

| Componente | Recomendação | Onde comprar |
| :--- | :--- | :--- |
| **NVMe (Alta Performance)** | WD Black SN770 / SN850 | Amazon / Kabum / Pichau |
| **NVMe (Custo-Benefício)** | Kingston NV2 | Mercado Livre |
| **SATA (Upgrade Antigo)** | Crucial BX500 | Lojas Nacionais |
| **🚫 EVITAR** | **Samsung PM981 / 970 EVO Plus*** | AliExpress / Usados |

*\*A 970 EVO Plus só é recomendada se estiver com o firmware mais recente atualizado via Windows.*

---

## 🌐 4. Wi-Fi e Bluetooth

No macOS Sonoma e Sequoia, o suporte a Wi-Fi mudou. Fique atento:

* **Melhor escolha (Nativa):** **Fenvi T919** (PCIe) ou **Fenvi BCM94360NG** (M.2).
    * *Vantagem:* AirDrop, Handoff e Sidecar funcionam como num Mac real.
* **Escolha Econômica (Kext):** Adaptadores **Intel AX200/AX210**.
    * *Vantagem:* Baratos e fáceis de achar.
    * *Desvantagem:* Requerem a kext `AirportItlwm` e o AirDrop é instável ou inexistente.

---

!!! note "Lembrete sobre Impostos"
    Considere o programa **Remessa Conforme**. Para itens acima de $50, o imposto de importação pode dobrar o valor do produto. Às vezes, comprar a Placa-mãe no Brasil com garantia é mais vantajoso que importar.