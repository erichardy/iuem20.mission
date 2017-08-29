# -*- coding: utf-8 -*-

from data import lorem
from data import missions
from os.path import abspath
from os.path import dirname
from os.path import join
from plone import api
from plone.namedfile import NamedBlobImage
from z3c.relationfield.relation import RelationValue
# from plone.i18n.normalizer.interfaces import INormalizer
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.publisher.browser import BrowserView

import logging


PREFIX = abspath(dirname(__file__))
logger = logging.getLogger('iuem20.mission: CREATEDATASET')


def input_image_path(f):
    return join(PREFIX, '../tests/images/', f)


class createDataSet(BrowserView):

    def __call__(self):
        portal = api.portal.get()
        project = portal.get('mon-projet')
        if project:
            self.createMissions(project)
        else:
            logger.info('Dossier projet absent')

        url = portal.absolute_url() + '/folder_contents'
        self.request.response.redirect(url)

    def getMissions(self):
        portal = api.portal.get()
        intids = getUtility(IIntIds)
        founds = api.content.find(context=portal,
                                  portal_type='iuem20.mission',
                                  path='/'.join(portal.getPhysicalPath())
                                  )
        p_ids = []
        for found in founds:
            p_ids.append(intids.getId(found.getObject()))
        return p_ids

    def getPortraits(self):
        portal = api.portal.get()
        intids = getUtility(IIntIds)
        founds = api.content.find(context=portal,
                                  portal_type='iuem20.portrait',
                                  path='/'.join(portal.getPhysicalPath())
                                  )
        p_ids = []
        for found in founds:
            p_ids.append(intids.getId(found.getObject()))
        return p_ids

    def createMissions(self, project):
        for mission in missions:
            obj = api.content.create(
                type='iuem20.mission',
                title=mission['title'],
                description=mission['description'],
                start_date=mission['start_date'],
                end_date=mission['end_date'],
                presentation=mission['presentation'],
                display_one=mission['display_one'],
                presentation_one=mission[
                    'presentation_one'],
                display_two=mission['display_two'],
                presentation_two=mission[
                    'presentation_two'],
                image=NamedBlobImage(),
                img_author=mission['img_author'],
                thumbnail=NamedBlobImage(),
                doc=mission['doc'],
                container=project
                )
            path_main = input_image_path(mission['image'])
            fd = open(path_main, 'r')
            obj.image.data = fd.read()
            fd.close()
            obj.image.filename = mission['image']
            path_main = input_image_path(mission['thumbnail'])
            fd = open(path_main, 'r')
            obj.thumbnail.data = fd.read()
            fd.close()
            obj.thumbnail.filename = mission['thumbnail']
            obj.reindexObject()
            allPortraits = self.getPortraits()
            obj.chiefs = set([RelationValue(allPortraits[0]),
                             RelationValue(allPortraits[4])])
            obj.other = set([RelationValue(allPortraits[1]),
                             RelationValue(allPortraits[2]),
                             RelationValue(allPortraits[3]),
                             ])
            obj.reindexObject()
            self.createCarousel(obj)
            logger.info(obj.title + ' Created')

    def _loadImage(self, objField, image):
        imgPath = image.split('/')
        if len(imgPath) > 1:
            title = imgPath[len(imgPath) - 1]
        else:
            title = image
        path = input_image_path(image)
        fd = open(path, 'r')
        objField.data = fd.read()
        fd.close()
        objField.filename = title

    def _loadImagesInFolder(self, folderish, images):
        for img in images:
            imgPath = img.split('/')
            if len(imgPath) > 1:
                title = imgPath[len(imgPath) - 1]
            else:
                title = img
            image = api.content.create(type='Image',
                                       title=title,
                                       image=NamedBlobImage(),
                                       description=lorem,
                                       container=folderish)
            self._loadImage(image.image, img)
            image.reindexObject()
            api.content.transition(obj=image, transition='publish')
            image.reindexObject()

    def createCarousel(self, loc):
        carousel = api.content.create(type='Folder',
                                      title=u'carousel',
                                      container=loc)
        api.content.transition(obj=carousel, transition='publish')
        imgs = [u'1800-IMGA0536.JPG', u'1800-IMGA0537.JPG',
                u'1800-IMGA0538.JPG', u'1800-IMGA0671.JPG',
                u'1800-IMGA0971.JPG']
        self._loadImagesInFolder(carousel, imgs)
        logger.info(carousel.title + ' Created')
