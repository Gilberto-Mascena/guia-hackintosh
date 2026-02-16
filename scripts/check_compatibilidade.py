import os

URL_PROJETO = "https://gilberto-mascena.github.io/guia-hackintosh/"

# Códigos de cores para o terminal
class Cores:
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_hardware():
    limpar_tela()
    print(f"{Cores.BOLD}{'='*60}")
    print(f"🔍 DIAGNÓSTICO RÁPIDO HACKINTOSH (BRASIL) - v1.0")
    print(f"{'='*60}{Cores.RESET}")
    print("Responda com o número da opção desejada.\n")

    try:
        # --- PROCESSADOR ---
        print(f"{Cores.BOLD}1. Qual o seu Processador?{Cores.RESET}")
        print("[1] Intel (10ª geração ou anterior)")
        print("[2] Intel (11ª geração ou superior)")
        print("[3] AMD Ryzen")
        cpu = input("R: ")

        # --- GPU ---
        print(f"\n{Cores.BOLD}2. Qual a sua Placa de Vídeo (GPU)?{Cores.RESET}")
        print("[1] Integrada Intel (iGPU)")
        print("[2] AMD Radeon (Séries RX 400, 500, 5000, 6000)")
        print("[3] NVIDIA (Qualquer uma)")
        gpu = input("R: ")

        # --- ARMAZENAMENTO ---
        print(f"\n{Cores.BOLD}3. Qual o modelo do seu SSD NVMe?{Cores.RESET}")
        print("[1] Western Digital / Crucial / Kingston")
        print("[2] Samsung (PM981 / PM991) ou Micron")
        print("[3] Outro / Não sei")
        ssd = input("R: ")

    except KeyboardInterrupt:
        print("\n\nSaindo...")
        return

    print("\n" + "="*60)
    print(f"{Cores.BOLD}📊 RESULTADO DO DIAGNÓSTICO:{Cores.RESET}")
    print("="*60)

    alertas = []
    sucesso = True

    # Validação CPU + GPU
    if cpu == "1":
        print(f"{Cores.VERDE}✅ CPU: Excelente compatibilidade nativa.{Cores.RESET}")
    elif cpu == "2":
        if gpu != "2":
            alertas.append(f"{Cores.VERMELHO}❌ ERRO: CPUs Intel de 11ª+ gen exigem GPU AMD dedicada. A iGPU não funciona.{Cores.RESET}")
            sucesso = False
        else:
            print(f"{Cores.VERDE}✅ CPU/GPU: Setup moderno com GPU AMD é suportado.{Cores.RESET}")
    elif cpu == "3":
        alertas.append(f"{Cores.AMARELO}⚠️ AVISO: AMD Ryzen exige patches de kernel e tem bugs conhecidos em apps Adobe.{Cores.RESET}")

    # Validação GPU NVIDIA ou AMD específica
    if gpu == "3":
        alertas.append(f"{Cores.VERMELHO}❌ ERRO: NVIDIA não tem suporte em versões modernas do macOS.{Cores.RESET}")
        sucesso = False
    elif gpu == "2":
        print(f"{Cores.AMARELO}ℹ️ NOTA: Certifique-se que sua GPU não é uma RX 6700 XT (incompatível).{Cores.RESET}")

    # Validação SSD
    if ssd == "2":
        alertas.append(f"{Cores.VERMELHO}❌ CILADA: SSD Samsung/Micron detectado. Risco alto de instabilidade.{Cores.RESET}")
        sucesso = False

    # Resultado Final
    if not alertas:
        print(f"\n{Cores.VERDE}{Cores.BOLD}🚀 SINAL VERDE! Seu hardware parece ser muito compatível.{Cores.RESET}")
    else:
        for a in alertas:
            print(a)
    
    if sucesso and alertas:
        print(f"\n{Cores.VERDE}👍 Apesar dos avisos, seu sistema é tecnicamente viável.{Cores.RESET}")

    print(f"\n{Cores.BOLD}🔗 Para detalhes, acesse: {URL_PROJETO}{Cores.RESET}")

if __name__ == "__main__":
    check_hardware()