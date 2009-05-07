import unittest

class SDistTests(unittest.TestCase):

    def _getTargetClass(self):
        from pkginfo.bdist import BDist
        return BDist

    def _makeOne(self, filename=None):
        return self._getTargetClass()(filename)

    def _checkSample(self, sdist, filename):
        self.assertEqual(sdist.filename, filename)
        self.assertEqual(sdist.metadata_version, '1.0')
        self.assertEqual(sdist.name, 'mypackage')
        self.assertEqual(sdist.version, '0.1')
        self.assertEqual(sdist.keywords, None)
        self.assertEqual(list(sdist.classifiers),
                         ['Development Status :: 4 - Beta',
                          'Environment :: Console (Text Based)',
                         ])
        self.assertEqual(list(sdist.supported_platforms), [])

    def test_ctor_w_egg(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1-py2.6.egg' % d
        sdist = self._makeOne(filename)
        self._checkSample(sdist, filename)