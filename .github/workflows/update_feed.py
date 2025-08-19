import os
import subprocess

# Caminho da pasta onde está o conteúdo do site
SITE_DIR = "."

def main():
    try:
        # Atualiza o repositório local
        subprocess.run(["git", "pull"], check=True)

        # Adiciona todas as alterações
        subprocess.run(["git", "add", "."], check=True)

        # Cria um commit com a mensagem padrão
        subprocess.run(["git", "commit", "-m", "Atualizando feed automático"], check=True)

        # Envia para o GitHub
        subprocess.run(["git", "push"], check=True)

        print("✅ Feed atualizado com sucesso!")

    except subprocess.CalledProcessError as e:
        print("⚠️ Erro ao atualizar o feed:", e)

if __name__ == "__main__":
    main()
