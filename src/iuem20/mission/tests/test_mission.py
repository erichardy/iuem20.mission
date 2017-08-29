# -*- coding: utf-8 -*-
from iuem20.mission.interfaces import Imission
from iuem20.mission.testing import IUEM20_MISSION_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class missionIntegrationTest(unittest.TestCase):

    layer = IUEM20_MISSION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='mission')
        schema = fti.lookupSchema()
        self.assertEqual(Imission, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='mission')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='mission')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(Imission.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='mission',
            id='mission',
        )
        self.assertTrue(Imission.providedBy(obj))
