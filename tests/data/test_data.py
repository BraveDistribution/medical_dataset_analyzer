import os


from pathlib import Path

from preprocess.data.data import Dataset, DatasetAnalyzer, Modality, VolumeType


def test_end_to_end_data():
    """Test end to end data."""
    path_to_test_data = str(Path(__file__).parent.parent.resolve()) + "/test_data"
    dataset = Dataset(path_to_test_data, Modality.CT, VolumeType.NIFTY)
    dataset_analyzer = DatasetAnalyzer(dataset)
    result = dataset_analyzer.collect_volume_properties()
    assert len(result) == 2
    print(result)