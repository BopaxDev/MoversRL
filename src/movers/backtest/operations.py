import json
from pathlib import Path
from typing import Any

from movers.utils.settings import get_settings


class TradingLoader(type):
    source_loaded: bool = False
    positions: dict | None = None
    orders: dict | None = None

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if not self.source_loaded:
            if isinstance(get_settings().PositionSource, str):
                if Path(get_settings().PositionSource).exists():
                    with open(get_settings().PositionSource) as file:
                        try:
                            self.positions = json.loads(file)
                            self.source_loaded = True
                        except json.JSONDecodeError:
                            self.positions = {}

                        file.close()
                else:
                    self.positions = {}
            else:
                self.positions = {}

            if isinstance(get_settings().OrderSource, str):
                if Path(get_settings().OrderSource).exists():
                    with open(get_settings().OrderSource) as file:
                        try:
                            self.orders = json.loads(file)
                            self.source_loaded = True
                        except json.JSONDecodeError:
                            self.orders = {}

                        file.close()
                else:
                    self.orders = {}
            else:
                self.orders = {}

        return super().__call__(*args, **kwds)


class TradingSession(metaclass=TradingLoader):
    def __init__(
        self,
    ) -> None:
        ...

    def place_order(
        self,
    ) -> None:
        ...

    def fill_order(
        self,
    ) -> None:
        ...

    def edit_order(
        self,
    ) -> None:
        ...

    def delete_order(
        self,
    ) -> None:
        ...

    def open_position(
        self,
    ) -> None:
        ...

    def edit_position(
        self,
    ) -> None:
        ...

    def delete_position(
        self,
    ) -> None:
        ...

    def report(
        self,
    ) -> None:
        ...

    def save(
        self,
    ) -> None:
        ...
