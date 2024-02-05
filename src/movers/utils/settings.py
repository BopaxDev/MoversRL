from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

from omegaconf import OmegaConf


@dataclass
class RiskManagementModel:
    """
    Data class representing backtesting settings.
    These essentially represents the value used as default when no pre-trained risk
    management model has been loaded.

    Attributes:
        TakeProfit (int | float): Value indicating the take profit
        StopLoss (int | float): Value indicating the stop loss
    """

    name: str | None = field(default=None)
    type: str | None = field(default=None)


@dataclass
class TradingModel:
    name: str | None = field(default=None)
    type: str | None = field(default=None)
    source: str | None = field(default=None)


@dataclass
class PortfolioManagementModel:
    type: str | None = field(default="")
    take_profit: float = field(default=0.0)
    stop_loss: float = field(default=0.0)


@dataclass
class Settings:
    """
    Data class representing system settings.

    Attributes:
        PostgreSQL (PostgreSQL): PostgreSQL settings.
        MongoDB (MongoDB): MongoDB settings.
        API (API): API settings.
        Policies (Policies): Policies settings.
        RiskManagement (RiskManagement): Risk management settings.
        TechnicalIndicators (TechnicalIndicators): Technical indicators settings.
        Backtesting (Backtesting): Backtesting settings.
        TradingTickers (list): List of trading tickers.

    Optional Attributes:
        TradingRiskManagement (TradingRiskManagement): Default Risk Management Values
        DefaultAdministrators (dict): Default administrators' information.
        DefaultInvestors (list): Default investors' information.
        DefaultFunds (dict): Default funds' information.
        DefaultStrategies (list): Default strategies' information.
    """

    PositionSource: str | None = field(default=None)
    RiskManagementModels: list[RiskManagementModel] = field(default_factory=list)
    TradingModels: list[TradingModel] = field(default_factory=list)
    PortfolioManagementModel: PortfolioManagementModel = field(
        default_factory=PortfolioManagementModel
    )


@lru_cache
def get_settings() -> Settings:
    """
    Function to fetch application settings using caching.

    Returns:
        Settings: An instance of the Settings class representing the overall
            configuration settings for the application.
    """

    settings_import = OmegaConf.load(
        Path(__file__)
        .absolute()
        .parent.parent.parent.parent.joinpath(
            "config.yaml",
        ),
    )

    return OmegaConf.structured(
        Settings(**settings_import),
    )
