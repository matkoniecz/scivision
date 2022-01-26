from scivision.catalog import add_dataset, add_model
import json


DATA_CATALOG = 'scivision/catalog/data/datasources.json'


def test_add_dataset():
    """Test that a new dataset can be added to the scivision dataset catalog."""
    test_entry = 'tests/catalog_data_entry.json'
    add_dataset(test_entry, DATA_CATALOG)
    with open(test_entry) as file:
        entry = json.load(file)
    entry_name = list(entry.keys())[0]
    with open('scivision/catalog/data/datasources.json') as file:
        datasources = json.load(file)
    assert entry_name in datasources
    assert "task" in datasources[entry_name]
    assert "domain" in datasources[entry_name]
    assert "datasource" in datasources[entry_name]
    assert "format" in datasources[entry_name]
    assert "labels" in datasources[entry_name]
    assert "institution" in datasources[entry_name]
    assert "tags" in datasources[entry_name]
    
    
def test_add_dataset_multiple():
    """Test that multiple datasets can be added to the scivision dataset catalog when provided."""
    test_entry = 'tests/catalog_data_multiple_entries.json'
    add_dataset(test_entry, DATA_CATALOG)
    with open(test_entry) as file:
        entry = json.load(file)
    entries = list(entry.keys())
    with open('scivision/catalog/data/datasources.json') as file:
        datasources = json.load(file)
    for entry_name in entries:
        assert entry_name in datasources
        assert "task" in datasources[entry_name]
        assert "domain" in datasources[entry_name]
        assert "datasource" in datasources[entry_name]
        assert "format" in datasources[entry_name]
        assert "labels" in datasources[entry_name]
        assert "institution" in datasources[entry_name]
        assert "tags" in datasources[entry_name]
        
        
# def test_add_dataset_entry_exists():
#     """Test that a new dataset is not added to the scivision dataset catalog if an entry with the same name exists."""
    # TODO: instead, have it so that the datasets are named however people like for now
    