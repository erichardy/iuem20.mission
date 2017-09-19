# -*- coding: utf-8 -*-
"""
Nous aurons besoin des references :
http://docs.plone.org/external/plone.app.dexterity/docs/advanced/references.html
pour associer un projet à des missions et des portraits.

tools to get coordinates :

* http://www.birdtheme.org/useful/v3tool.html

* http://www.latlong.net/

* http://codepen.io/jhawes/pen/ujdgK

* http://stackoverflow.com/questions/5072059/polygon-drawing-and-getting-
  coordinates-with-google-map-api-v3

* charger un kml/gps/geojson dans leaflet :
  http://www.d3noob.org/2014/02/load-kml-gpx-or-geojson-traces-into.html

"""

from iuem20.mission import _
from iuem20.mission.interfaces import IMission
# from plone import api
# from plone.dexterity.browser import edit
# from plone.autoform import directives
from plone.dexterity.browser import add
from plone.dexterity.content import Container
from plonetheme.iuem20.utils import getGalleryImages as ggi
# from Products.CMFPlone.utils import safe_unicode
from z3c.form import button
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope.interface import implementer
from zope.publisher.browser import BrowserView

import logging


logger = logging.getLogger('iuem20 MISSIONS')
mois = []
mois.append(u'Janvier')
mois.append(u'Février')
mois.append(u'Mars')
mois.append(u'Avril')
mois.append(u'Mai')
mois.append(u'Juin')
mois.append(u'Juillet')
mois.append(u'Aout')
mois.append(u'Septembre')
mois.append(u'Octobre')
mois.append(u'Novembre')
mois.append(u'Décembre')
months = {}
months['01'] = u'Janvier'
months['02'] = u'Février'
months['03'] = u'Mars'
months['04'] = u'Avril'
months['05'] = u'Mai'
months['06'] = u'Juin'
months['07'] = u'Juillet'
months['08'] = u'Aout'
months['09'] = u'Septembre'
months['10'] = u'Octobre'
months['11'] = u'Novembre'
months['12'] = u'Décembre'


class AddForm(add.DefaultAddForm):
    portal_type = 'iuem20.mission'
    ignoreContext = True
    label = _(u'Add a new mission !')

    def update(self):
        super(add.DefaultAddForm, self).update()
        # logger.info('Mission addForm : in update()')
        # logger.info(self.context)

    def updateWidgets(self):
        super(add.DefaultAddForm, self).updateWidgets()
        # logger.info(self.context)

    @button.buttonAndHandler(_(u'Save this mission'), name='save_this_mission')
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = _('Please correct errors')
            return
        try:
            obj = self.createAndAdd(data)
            # logger.info(obj)
            # logger.info(u'=-=-=-=-=')
            context = self.context
            objId = obj.getId()
            url = context[objId].absolute_url()
            self.request.response.redirect(url)
        except Exception:
            raise

    @button.buttonAndHandler(_(u'Cancel this mission'))
    def handleCancel(self, action):
        data, errors = self.extractData()
        # context is the thesis repo
        contextURL = self.context.absolute_url()
        self.request.response.redirect(contextURL)


class AddView(add.DefaultAddView):
    form = AddForm


"""
class editForm(edit.DefaultEditForm):
    pass
"""


class MissionView(BrowserView):
    """
    Vue des missions

    .. note:: les méthodes de cette vue ne sont généralement pas utilisées.
       on préfère utiliser les méthodes de l'objet lui-même
    """

    def _date_fr(self, date):
        j = date.strftime('%d')
        m = date.strftime('%m')
        y = date.strftime('%Y')
        M = months[m]
        return j + ' ' + M + ' ' + y

    def getDates(self):
        start = self.context.start_date
        end = self.context.end_date
        if (start is None) or (end is None):
            return False
        return self._date_fr(start) + ' - ' + self._date_fr(end)

    def getParentProject(self):
        return self.context.aq_inner.aq_parent

    def getPictAuthor(self):
        if not self.context.pict_author:
            return False
        return self.context.pict_author

    def getChief(self):
        return self.context.chief.to_object

    def getTeam(self):
        others = []
        for other in self.context.other:
            others.append(other.to_object)
        # import pdb;pdb.set_trace()
        return others

    def getAffiliations(self, person):
        aff = u''
        if person.affiliation1:
            aff += person.affiliation1
        if person.affiliation2:
            aff += ' - ' + person.affiliation2
        if person.affiliation3:
            aff += ' - ' + person.affiliation3
        return aff

    def displayEN(self):
        return self.context.display_en

    def getGalleryImages(self):
        return ggi(self.context)


@implementer(IMission)
class mission(Container):

    def _date_fr(self, date):
        """
        :return: une chaine de caractères représentant une date telle
           qu'on la représente habituellement en france : jj Mois YYYY
        """
        j = date.strftime('%d')
        m = date.strftime('%m')
        y = date.strftime('%Y')
        M = months[m]
        return j + ' ' + M + ' ' + y

    def getDates(self):
        """
        :return: les dates de début et de fin de la mission. Si pas de
           date, retourne ``False``
        """
        start = self.start_date
        end = self.end_date
        if (start is None) or (end is None):
            return False
        return self._date_fr(start) + ' - ' + self._date_fr(end)

    def getParentProject(self):
        """
        :return: l'objet parent de la mission. Normalement, ce doit être
           un projet
        """
        return self.aq_inner.aq_parent

    def getImgAuthor(self):
        """
        :return: L'auteur de l'image principale de la mission.
           Ou ``False`` si pas d'auteur
        """
        if not self.img_author:
            return False
        return self.img_author

    def getAffiliations(self, person):
        """
        A une mission, sont associées des personnes dont le portrait
        a été préalablement saisi.

        :param person: l'une des personnes impliquée dans la mission
        :type person: iuem20.portrait
        :return: les affiliations de la personne
        """
        aff = u''
        if person.affiliation1:
            aff += person.affiliation1
        if person.affiliation2:
            aff += ' - ' + person.affiliation2
        if person.affiliation3:
            aff += ' - ' + person.affiliation3
        return aff

    def displayEN(self):
        """
        :return: Booléen qui indique si on affiche la version anglaise
        """
        return self.display_en

    def getGalleryImages(self):
        """
        :return: la liste des images du répertoire ``carousel`` si présent.
           Sinon, ``False``
        """
        return ggi(self)

    def getTeam(self):
        """
        :return: La liste des ``iuem20.portrait`` des participants
           à la mission.
        """
        others = []
        for other in self.other:
            others.append(other.to_object)
        return others

    def getChiefs(self):
        """
        :return: La liste des ``iuem20.portrait`` des chefs
           de la mission.
        """
        chiefs = []
        for chief in self.chiefs:
            chiefs.append(chief.to_object)
        return chiefs

    def getPresentation(self):
        """
        :return: Le texte en français en format ``raw`` s'il existe.
           Sinon ``False``
        """
        try:
            if len(self.presentation.raw) < 6:
                # logger.info('inf a 6')
                return False
            else:
                return self.presentation.raw
        except Exception:
            # logger.info('excepppppp')
            return False
