import os
import sys
import logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

class TextureConverter(object):
    def __init__(self, maketx_path):
        self.converted = {}
        self.maketx_path = maketx_path

    def convert(self, path):
        if path in self.converted:
            return self.converted[path]
        path_converted = self._convert_with_maketx(path)
        self.converted[path] = path_converted
        return path_converted

    def _convert_with_maketx(self, path):
        base_path, _ = os.path.splitext(path)
        tx_path = f"{base_path}.tx"

        if os.path.exists(tx_path):
            logging.warning(f'{tx_path} already exists.')
            return None

        status = os.system(f'{self.maketx_path} -o "{tx_path}" "{path}"')

        if status != 0:
            logging.error(f'maketx failed with error code {status}.')
            return None

        return tx_path
