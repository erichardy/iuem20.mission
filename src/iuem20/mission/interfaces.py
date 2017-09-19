# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective import dexteritytextindexer
from iuem20.mission import _
from plone.app.textfield import RichText
from plone.app.vocabularies.catalog import CatalogSource as CS
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope.interface import alsoProvides
from zope.interface import Invalid
from zope.interface import invariant
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema import Date
from zope.schema import TextLine


class IIuem20MissionLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class StartBeforeEnd(Invalid):
    __doc__ = _(u'The start or end date is invalid')


class IMission(model.Schema):
    """
    Schema du type de contenu ``iuem20.mission``
    """
    model.fieldset('descriptions',
                   label=_(u'descriptions'),
                   fields=['title',
                           'description',
                           'presentation',
                           'start_date',
                           'end_date',
                           'label_to_project',
                           ])

    dexteritytextindexer.searchable('title')
    title = TextLine(title=_(u'mission label'),
                     required=True,
                     )
    dexteritytextindexer.searchable('description')
    description = TextLine(title=_(u'very short mission description'),
                           required=True,
                           )
    dexteritytextindexer.searchable('presentation')
    presentation = RichText(title=_(u'main presentation'),
                            description=_(u'Mission presentation'),
                            required=False
                            )

    dexteritytextindexer.searchable('start_date')
    start_date = Date(title=_(u'start date for the mission'),
                      description=_(u''),
                      required=False,
                      )
    dexteritytextindexer.searchable('end_date')
    end_date = Date(title=_(u'end date for the mission'),
                    description=_(u''),
                    required=False,
                    )
    label_to_project = TextLine(
        title=_(u'label for project link'),
        default=u'part of',
        required=True,
        )
    model.fieldset('images_and_doc',
                   label=_(u'images and doc'),
                   fields=[
                           'image',
                           'img_author',
                           'thumbnail',
                           'doc',
                           ])

    image = NamedBlobImage(title=_(u'main photo'),
                           required=True,
                           )
    img_author = TextLine(title=_(u'picture author'),
                          required=False,
                          )
    thumbnail = NamedBlobImage(title=_(u'small photo'),
                               required=True,
                               )
    doc = NamedBlobFile(title=_(u'other document'),
                        description=_(u'downloaded by visitors'),
                        required=False
                        )

    model.fieldset('participants',
                   label=_(u'participants'),
                   fields=[
                       'chiefs_title',
                       'chiefs',
                       'other_title',
                       'other',
                           ])
    chiefs_title = TextLine(
        title=_(u'title for chiefs section'),
        default=u'Chefs de mission / chiefs scientist',
        required=True,
        )
    chiefs = RelationList(title=_(u'chiefs scientist'),
                          value_type=RelationChoice(
                             title=_(u'Target'),
                             source=CS(portal_type='iuem20.portrait')),
                          required=True,
                          )
    other_title = TextLine(
        title=_(u'title for other participants section'),
        default=u'Other participants',
        required=True,
        )

    other = RelationList(title=_(u'other participants'),
                         value_type=RelationChoice(
                             title=_(u'Target'),
                             source=CS(portal_type='iuem20.portrait')),
                         required=False,
                         )

    @invariant
    def validateStartEnd(data):
        """
        :param data: les données du formulaire
        :type data: objet ayant pour attrituts les champs du formulaire
        :return: lève une erreur si la date de début est après la date de fin
        """
        if data.start_date is not None and data.end_date is not None:
            if data.start_date > data.end_date:
                msg = _(u'The start date must be before the end date.')
                raise StartBeforeEnd(_(msg))


alsoProvides(IMission, IFormFieldProvider)
