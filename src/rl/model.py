from collections import OrderedDict, namedtuple
from typing import Any, Optional, Union

import numpy as np
import numpy.typing as npt
import torch.nn as nn
import yaml
from lightning import LightningModule
from lightning.pytorch.utilities.types import STEP_OUTPUT
from omegaconf import DictConfig

from log.Logger import Logger
from utils.parameters import Parameters


class NN(
    LightningModule,
):
    def __init__(
        self,
        name: str,
        cfg: Optional[DictConfig] = None,
    ) -> None:
        super(
            NN,
            self,
        ).__init__()

        self.model_name = name
        self.configuration = cfg
        if not self.configuration:
            self.log = Logger(
                f"MODEL_{self.model_name}",
            )
            self.log.warn(
                "No configuration file has been file",
            )


class Encoder(
    LightningModule,
):
    def __init__(
        self,
        parameters_config: Optional[str] = None,
        dim_time_series: Optional[int] = None,
    ) -> None:
        super(
            Encoder,
            self,
        ).__init__()

        if parameters_config:
            with open(parameters_config) as file:
                yaml_file = yaml.safe_load(file)
                file.close()

            if not dim_time_series:
                parameters = Parameters(**yaml_file)
                dim_time_series = parameters.model.timeseries_input_dim

        self.time_series_first_encoding_block = nn.Sequential(
            OrderedDict(
                [
                    (
                        "conv1",
                        nn.Conv1d(
                            dim_time_series,
                            64,
                            3,
                        ),
                    ),
                    (
                        "gelu",
                        nn.GELU(),
                    ),
                ],
            ),
        )

        self.time_series_second_encoding_block = nn.Sequential(
            OrderedDict(
                [
                    (
                        "conv1",
                        nn.Conv1d(
                            dim_time_series,
                            64,
                            3,
                        ),
                    ),
                    (
                        "gelu",
                        nn.GELU(),
                    ),
                ],
            ),
        )

        self.time_series_third_encoding_block = nn.Sequential(
            OrderedDict(
                [
                    (
                        "conv1",
                        nn.Conv1d(
                            dim_time_series,
                            64,
                            3,
                        ),
                    ),
                    (
                        "gelu",
                        nn.GELU(),
                    ),
                ],
            ),
        )

        self.context_variables_first_encoding_block = nn.Sequential(
            OrderedDict(
                [
                    (
                        "linear",
                        nn.Linear(3, 4),
                    ),
                ],
            ),
        )

        self.context_variables_second_encoding_block = nn.Sequential(
            OrderedDict(
                [
                    (
                        "linear",
                        nn.Linear(3, 4),
                    ),
                ],
            ),
        )

        self.first_block = nn.Sequential(
            OrderedDict(
                [
                    (
                        "Conv1D",
                        nn.Conv1d(1, 2, 2),
                    ),
                ],
            ),
        )
        self.second_block = nn.Sequential(
            OrderedDict(
                [
                    (
                        "Conv1D",
                        nn.Conv1d(1, 2, 2),
                    ),
                ],
            ),
        )
        self.third_block = nn.Sequential(
            OrderedDict(
                [
                    (
                        "Conv1D",
                        nn.Conv1d(
                            1,
                            2,
                            2,
                        ),
                    ),
                ],
            ),
        )

    def embedding(
        self,
        encoded_time_series: Union[
            npt.ArrayLike,
            list,
        ],
        context_variables: Union[
            OrderedDict,
            namedtuple,
            dict,
        ],
    ):
        return np.concatenate(
            (
                encoded_time_series,
                context_variables,
            ),
        ).reshape(
            1,
            -1,
        )

    def forward(
        self,
        time_series: Union[
            npt.ArrayLike,
            list,
        ],
        context_variables: Union[
            OrderedDict,
            namedtuple,
            dict,
        ],
    ):
        time_series = self.time_series_third_encoding_block(
            self.time_series_second_encoding_block(
                self.time_series_first_encoding_block(
                    time_series,
                ),
            ),
        )

        context_variables = self.context_variables_first_encoding_block(
            self.context_variables_second_encoding_block(
                context_variables,
            ),
        )

        embedding = self.embedding(
            time_series,
            context_variables,
        )

        return self.third_block(
            self.second_block(
                self.first_block(
                    embedding,
                ),
            ),
        )

    def on_train_batch_end(
        self,
        outputs: STEP_OUTPUT,
        batch: Any,
        batch_idx: int,
    ) -> None:
        self.log.info(
            f"Just completed the Batch N° {batch_idx}",
        )

        return super().on_train_batch_end(
            outputs,
            batch,
            batch_idx,
        )

    def train(
        self,
    ):
        pass


class DQN(
    nn.Module,
):
    def __init__(
        self,
        n_observations,
        n_actions,
    ) -> None:
        self(
            DQN,
            self,
        ).__init__()
        self.first_block = (
            nn.Sequential(
                OrderedDict(
                    (
                        "linear_1",
                        nn.Linear(
                            n_observations,
                            128,
                        ),
                    ),
                    (
                        "relu_1",
                        nn.ReLU(),
                    ),
                ),
            ),
        )

        self.second_block = (
            nn.Linear(
                128,
                128,
            ),
        )
        self.third_block = (
            nn.Linear(
                128,
                n_actions,
            ),
        )

    def __str__(
        self,
    ) -> str:
        return super().__str__()

    def forward(
        self,
        encoded_state: Union[
            npt.ArrayLike,
            list,
        ],
    ):
        return (
            self.first_block(
                self.second_block(
                    self.first_block(
                        encoded_state,
                    ),
                ),
            ),
        )
