# ❓ Perguntas Frequentes (FAQ)

Este FAQ aborda as dúvidas mais comuns da comunidade brasileira. Se sua dúvida não estiver aqui, abra uma [Issue](https://github.com/Gilberto-Mascena/guia-hackintosh/issues).

---

## 🧐 Dúvidas Gerais

???+ question "1. Dá para fazer Hackintosh em qualquer notebook ou PC?"
    **Não.** A Apple parou de dar suporte a CPUs muito antigas e nunca suportou certas tecnologias (como Wi-Fi MediaTek ou GPUs NVIDIA RTX). O primeiro passo é conferir o nosso [Guia de Hardware](index.md).

???+ question "2. Meu PC tem processador AMD Ryzen, vale a pena?"
    Sim, mas com ressalvas importantes:
    * **Adobe Suite:** Apps como Premiere e After Effects precisam de patches extras e podem ser instáveis.
    * **Virtualização:** Docker e Máquinas Virtuais (VMware) são bem mais complexos de configurar em AMD.
    * **Áudio:** O microfone interno de muitos laptops Ryzen não funciona.

???+ question "3. Dá para usar o iMessage, FaceTime e iCloud?"
    **Sim.** Desde que você gere uma **SMBIOS** (números de série) válida e única. Serviços como AirDrop e Handoff exigem placas Wi-Fi específicas (veja o [Guia de Compras](compras.md)).

???+ question "4. O macOS vai rodar mais rápido que o Windows?"
    Em fluidez de sistema e uso de RAM, **sim**. Porém, para **jogos e renderização pesada**, o Windows ainda leva vantagem pelos drivers oficiais das fabricantes.

???+ question "5. Posso atualizar o sistema direto pelo Painel de Controle?"
    Apenas se sua **EFI (OpenCore e Kexts)** estiver atualizada primeiro. Atualizações entre versões (ex: Sonoma para Sequoia) exigem cautela e backup.

---

## 📘 Dicionário para Iniciantes

Se você é novo no mundo Hackintosh, esses termos vão aparecer o tempo todo:

| Termo | O que significa? |
| :--- | :--- |
| **Kext** | É o equivalente aos "Drivers" no macOS. |
| **Kernel Panic** | A famosa "Tela Azul" do Mac. Geralmente causada por kext errada. |
| **Verbose (-v)** | Modo de inicialização com texto na tela (essencial para diagnóstico). |
| **NVRAM** | Memória que guarda configs de boot (como o disco padrão de inicialização). |
| **SMBIOS** | Definição de qual modelo de Mac real o seu PC está "fingindo" ser. |

---

!!! tip "Dica de Ouro"
    Nunca faça uma atualização do macOS sem ter um pendrive de boot de reserva com uma EFI funcional. Se algo der errado, você não fica na mão!