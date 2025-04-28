# src/main.py
from bertho_toolkit import terminal_logger # Import relativo funciona pois estamos dentro de 'src'
# Ou, se executar de fora de src, o import seria: from src.bertho_toolkit import terminal_logger

def run_my_task():
    logger = terminal_logger.TerminalLogger(internal_log=True) # Supondo que a classe exista assim
    logger.LogInformation("Iniciando a tarefa principal...")
    # --- Coloque aqui o código que usa seu toolkit ---
    # Exemplo: Use o file_manager, env_manager, etc.
    logger.LogSuccess("Tarefa principal concluída!")

if __name__ == "__main__":
    run_my_task()