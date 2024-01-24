import logging
import os
import re

from gherkin.parser import Parser
from gherkin.token_scanner import TokenScanner
from gherkin.parser import Parser
from gherkin.errors import CompositeParserException

_logger = logging.getLogger(__name__)

def get_scenarios_from_feature(feature_content):
    scanner = TokenScanner(feature_content)
    parser = Parser()
    try:
        feature = parser.parse(scanner)
    except CompositeParserException as e:
        # Handle parsing errors if necessary
        _logger.error(f"Parsing error: {e}")
        raise e

    scenarios = []
    for scenario in feature['children']:
        if scenario['type'] == 'Scenario' or scenario['type'] == 'ScenarioOutline':
            scenarios.append(scenario['name'])

    return scenarios


def walk_get_path(path):
    feature_files = []
    feature_file_pattern = re.compile(r'.*\.feature$', re.IGNORECASE)
    
    def Walk(dir):
        for root, dirs, file_names in os.walk(dir):
            for file in file_names:
                if re.match(feature_file_pattern, file):
                    feature_files.append(os.path.join(root, file))
            for d in dirs:
                Walk(os.path.join(root, d))
    
    _logger.info("getting all feature files")
    Walk(path)
    _logger.info("load files done")

    return feature_files

def load_all_scenarios():
    with open
    
    scenarios = get_scenarios_from_feature()