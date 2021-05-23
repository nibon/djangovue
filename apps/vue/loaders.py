from webpack_loader.exceptions import WebpackLoaderTimeoutError, WebpackBundleLookupError, WebpackError, \
    WebpackLoaderBadStatsError
from webpack_loader.loader import WebpackLoader
import json
import time
import os
from io import open

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage


class CustomWebpackLoader(WebpackLoader):
    pass
    # def get_bundle(self, bundle_name):
    #     assets = self.get_assets()
    #
    #     # poll when debugging and block request until bundle is compiled
    #     # or the build times out
    #     if settings.DEBUG:
    #         timeout = self.config['TIMEOUT'] or 0
    #         timed_out = False
    #         start = time.time()
    #         while assets['status'] == 'compile' and not timed_out:
    #             time.sleep(self.config['POLL_INTERVAL'])
    #             if timeout and (time.time() - timeout > start):
    #                 timed_out = True
    #             assets = self.get_assets()
    #
    #         if timed_out:
    #             raise WebpackLoaderTimeoutError(
    #                 "Timed Out. Bundle `{0}` took more than {1} seconds "
    #                 "to compile.".format(bundle_name, timeout)
    #             )
    #
    #     if assets.get('status') == 'done':
    #         chunks = assets['chunks'].get(bundle_name, None)
    #         if chunks is None:
    #             raise WebpackBundleLookupError('Cannot resolve bundle {0}.'.format(bundle_name))
    #
    #         for chunk in chunks:
    #             asset = assets['assets'][chunk]
    #             if asset is None:
    #                 raise WebpackBundleLookupError('Cannot resolve asset {0}.'.format(chunk))
    #
    #         return self.filter_chunks(chunks)
    #
    #     elif assets.get('status') == 'error':
    #         if 'file' not in assets:
    #             assets['file'] = ''
    #         if 'error' not in assets:
    #             assets['error'] = 'Unknown Error'
    #         if 'message' not in assets:
    #             assets['message'] = ''
    #         error = u"""
    #         {error} in {file}
    #         {message}
    #         """.format(**assets)
    #         raise WebpackError(error)
    #
    #     raise WebpackLoaderBadStatsError(
    #         "The stats file does not contain valid data. Make sure "
    #         "webpack-bundle-tracker plugin is enabled and try to run "
    #         "webpack again.")
