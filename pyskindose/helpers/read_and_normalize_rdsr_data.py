import logging
import os
from pathlib import Path

import pandas as pd
import pydicom

from pyskindose.rdsr_normalizer import rdsr_normalizer, RDM_normalizer
from pyskindose.rdsr_parser import rdsr_parser, RDM_parser
from pyskindose.settings import PyskindoseSettings

logger = logging.getLogger(__name__)


def read_and_normalise_rdsr_data(rdsr_filepath: str, settings: PyskindoseSettings):

    rdsr_filepath = (
        Path(rdsr_filepath)
        if rdsr_filepath
        else Path(__file__).parent.parent / "example_data/RDSR" / settings.rdsr_filename
    )

    logger.debug(str(rdsr_filepath.absolute()))

    # If provided, load preparsed rdsr data in .json format
    if ".json" == rdsr_filepath.suffix.lower():
        return pd.read_json(rdsr_filepath)
    
    if ".xlsx" == rdsr_filepath.suffix.lower():
        data_raw = pd.read_excel(rdsr_filepath, skiprows=[i for i in range(43)])

        data_parsed = RDM_parser(data_raw)

        normalized_data = RDM_normalizer(data_parsed, settings=settings)

    else:
        # else load RDSR data with pydicom
        data_raw = pydicom.dcmread(rdsr_filepath)

        # parse RDSR data from raw .dicom file
        data_parsed = rdsr_parser(data_raw)

        # normalized rdsr for compliance with PySkinDose
        normalized_data = rdsr_normalizer(data_parsed, settings=settings)

    return normalized_data
