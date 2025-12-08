import pytest
import json
from pathlib import Path
from config import HCCLinksConfig, HCCLinksCollection, HCCLinksItem

class TestConfig:

    def test_read_good_config_direct(self):
        cfp = Path('.') / 'tests' / 'good_config.json'
        with cfp.open() as cf:
            cfo = json.load(cf)
            print(json.dumps(cfo))
        assert cfo['sourceBundleId'] == 'insights', "Source bundle ID should be 'insights'"
        assert len(cfo['collections']) == 2, "Config should contain 2 collections"
    
    def test_read_good_config_iface(self):
        config_obj = HCCLinksConfig('./tests/good_config.json')
        assert isinstance(config_obj, HCCLinksConfig), "Config should be HCCLinksConfig object"
        assert config_obj.source_bundle_id == 'insights', "OO source bundle ID should be 'insights'"
        assert isinstance(config_obj.collections[0], HCCLinksCollection), "First config collection should be an HCCLinksCollection object"
        assert len(config_obj.collections) == 2, "OO config should contain 2 collections"
        assert len(config_obj.collections[0].items) == 3, "First collection should contain 3 items"
        assert isinstance(config_obj.collections[0].items[0], HCCLinksItem)
        assert config_obj.collections[0].items[0].method == 'HEAD', "First item in first collection should be HEAD"

    def test_read_bad_config_iface(self):
        with pytest.raises(json.JSONDecodeError):
            config_obj = HCCLinksConfig('./tests/bad_config.json')
            assert True