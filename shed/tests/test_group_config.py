import json
from pathlib import Path
from config import HCCLinksConfig

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
        print(config_obj.source_bundle_id)
        assert config_obj.source_bundle_id == 'insights', "OO source bundle ID should be 'insights'"
        assert len(config_obj.collections) == 2, "OO config should contain 2 collections"
        assert config_obj.collections[0].items[0].method == 'HEAD', "First item in first collection should be HEAD"

    def test_read_bad_config_iface(self):
        config_obj = HCCLinksConfig('./tests/bad_config.json')
        assert True