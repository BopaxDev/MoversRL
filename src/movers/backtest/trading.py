from typing import Any

import pandas as pd

from movers.backtest.operations import TradingSession
from movers.backtest.schemas import Performances
from movers.dataset.loader import TimeSeriesDatasets


class ModelsLoaderMetaclass(type):
    models_initialised: dict = {}

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        Override the call method to initialize risk management models if available.

        Parameters:
            *args (Any): Variable arguments.
            **kwds (Any): Keyword arguments.

        Returns:
            Any: Result of calling the superclass's call method.
        """

        if get_risk_management_models() is None:
            logger.warn("No Risk Management models have been implemented")
        else:
            for model in get_risk_management_models():
                model_initialisation = self.models_initialised.get(model, 0)
                if model_initialisation == 0:
                    self.initialise_model(model_path=model)

        return super().__call__(*args, **kwds)

    def initialise_model(
        self,
        model_path: str,
    ) -> bool:
        """
        Initialize a risk management model from the specified path.

        Parameters:
            model_path (str): Path to the risk management model.

        Returns:
            bool: True if the model is successfully initialized, False otherwise.
        """

        logger.info(f"Trying to load the following model: {model_path}")

        try:
            model = torch.jit.load(model_path)
            model.eval()
        except Exception as error:
            logger.error(
                f"Unable to load the model in the following path: {model_path}. Error"
                f" occurred: {error}"
            )
            return False
        else:
            self.models_initialised[model_path] = model
            return True


class Environment:
    def __init__(self) -> None:
        self.session = TradingSession()
        self.time_series = TimeSeriesDatasets()

    def load_trading_models(self) -> None:
        ...

    def load_risk_management(self) -> None:
        ...

    def load_data_source(self) -> None:
        ...

    def backtest(self) -> Performances:
        for 
