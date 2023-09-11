import logging
from typing import Optional


class Logger:
    def __init__(
        self,
        name: str,
        log_filename: Optional[str] = "master.log",
        level: int = logging.DEBUG,
        formatter: str = "[%(asctime)s\t %(levelname)s\t %(name)s] %(message)s",
    ) -> None:
        self.logger = logging.getLogger(
            name=name,
        )
        self.logger.setLevel(
            level=level,
        )

        self.formatter = formatter
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(
            fmt=logging.Formatter(
                formatter,
            ),
        )

        self.stream_handler.setLevel(
            level=level,
        )

        self.logger.addHandler(
            hdlr=self.stream_handler,
        )

        if log_filename:
            self.file_handler = logging.FileHandler(
                log_filename,
            )

            self.file_handler.setFormatter(
                fmt=logging.Formatter(
                    formatter,
                ),
            )

            self.file_handler.setLevel(
                level=level,
            )

            self.logger.addHandler(
                self.file_handler,
            )

    def critical(
        self,
        msg: str,
    ) -> None:
        self.logger.critical(
            msg=msg,
        )

    def debug(
        self,
        msg: str,
    ) -> None:
        self.logger.debug(
            msg=msg,
        )

    def error(
        self,
        msg: str,
    ) -> None:
        self.logger.error(
            msg=msg,
        )

    def info(
        self,
        msg: str,
    ) -> None:
        self.logger.info(
            msg=msg,
        )

    def warn(
        self,
        msg: str,
    ) -> None:
        self.logger.warning(
            msg=msg,
        )
