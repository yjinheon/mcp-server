import logging
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.logging import RichHandler

from app.config.settings import settings


def _project_logs_dir() -> Path:
    # logger_config.py → config → app → <project_root>/logs
    project_root = Path(__file__).resolve().parents[2]
    return project_root / "logs"


def get_rich_logger() -> logging.Logger:
    app_name = settings.app_name
    logs_dir = Path(settings.logs_dir or _project_logs_dir())
    logs_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d")
    log_path = logs_dir / f"{app_name}_{ts}.log"

    logger = logging.getLogger(app_name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False

    # fich format file handler

    fp = open(log_path, "w", encoding="utf-8")
    file_console = Console(file=fp, width=120, force_terminal=True)
    file_handler = RichHandler(
        console=file_console,
        show_path=True,
        show_time=True,
        rich_tracebacks=True,
        markup=True,
    )
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    # fich format console handler
    console_handler = RichHandler(
        console=Console(stderr=True, width=120, force_terminal=True),
        show_path=True,
        show_time=True,
        rich_tracebacks=True,
        markup=True,
    )
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    logger.info(f"[init] logging -> {log_path}")
    return logger
