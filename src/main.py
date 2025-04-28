from bertho_toolkit import TerminalLogger, EnvManager, FileManager

def run_my_task():
    logger = TerminalLogger(internal_log=True)
    logger.LogInformation("Iniciando a tarefa principal...")
    # ... seu código ...
    logger.LogSuccess("Tarefa principal concluída!")

if __name__ == "__main__":
    run_my_task()
