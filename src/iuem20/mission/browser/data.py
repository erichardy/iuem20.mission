# -*- coding: utf-8 -*-

from plone.app.textfield.value import RichTextValue

import datetime


lorem = """
Vivamus dictum, nunc a tincidunt semper, lectus justo maximus neque,
et pulvinar ipsum dolor at nisl. Maecenas porttitor dolor nec ante cursus
viverra. Maecenas massa nunc, semper vitae pulvinar at, semper
at metus. Cras a fermentum diam. Sed a lobortis
risus, efficitur tincidunt lorem.
"""

bio_fr_text = """
<h4>Savoir-faire opérationnels</h4>
<ul>
<li>Utiliser les méthodes de prévention et
de gestion des risques<br/></li>
</ul>
<h4>Lieu d'exercice</h4>
<ul>
<li>L’activité s’exerce généralement au sein d'un service informatique<br/>
</li>
</ul>
<h3>Dipl&ocirc;me exig&eacute;</h3>
<ul>
<li>Doctorat, diplôme d’ingénieur<br/></li>
</ul>
<h3>Formations et expérience professionnelle souhaitables</h3>
<ul><li>Filière informatique</li></ul>
"""

bio_alt1_text = """
<h2>ALT 1 The RichTextValue<a class="headerlink" href="#the-richtextvalue"
title="Permalink to this headline">¶</a></h2>
<p>The <code class="docutils literal"><span class="pre">RichText</span>
</code> field does not store a string. Instead, it stores a
<code class="docutils literal"><span class="pre">RichTextValue</span>
</code> object. This is an immutable object that has the
following properties:</p>
<dl class="docutils">
<dt><code class="docutils literal"><span class="pre">raw</span></code></dt>
<dd>a unicode string with the original input markup;</dd>
<dt><code class="docutils literal"><span class="pre">mimeType</span></code>
</dt>
<dd>the MIME type of the original markup, e.g.
<code class="docutils literal"><span class="pre">text/html</span></code> or
<code class="docutils literal"><span class="pre">text/structured</span>
</code>;</dd>
<dt><code class="docutils literal"><span class="pre">encoding</span></code>
</dt>
<dd>the default character encoding used when transforming the input markup.
Most likely, this will be UTF-8;</dd>
<dt><code class="docutils literal"><span class="pre">raw_encoded</span>
</code></dt>
<dd>the raw input encoded in the given encoding;</dd>
<dt><code class="docutils literal"><span class="pre">outputMimeType</span>
</code></dt>
<dd>the MIME type of the default output, taken from the field at the time of
instantiation;</dd>
<dt><code class="docutils literal"><span class="pre">output</span></code></dt>
<dd>a unicode object representing the transformed output. If possible, this
is cached persistently until the <code class="docutils literal">
<span class="pre">RichTextValue</span></code> is replaced with a
new one (as happens when an edit form is saved, for example).</dd>
</dl>
"""
bio_alt2_text = """
<h2>ALT 2 The RichTextValue<a class="headerlink" href="#the-richtextvalue"
title="Permalink to this headline">¶</a></h2>
<p>The <code class="docutils literal"><span class="pre">RichText</span>
</code> field does not store a string. Instead, it stores a
<code class="docutils literal"><span class="pre">RichTextValue</span>
</code> object. This is an immutable object that has the
following properties:</p>
<dl class="docutils">
<dt><code class="docutils literal"><span class="pre">raw</span></code></dt>
<dd>a unicode string with the original input markup;</dd>
<dt><code class="docutils literal"><span class="pre">mimeType</span></code>
</dt>
<dd>the MIME type of the original markup, e.g.
<code class="docutils literal"><span class="pre">text/html</span></code> or
<code class="docutils literal"><span class="pre">text/structured</span>
</code>;</dd>
<dt><code class="docutils literal"><span class="pre">encoding</span></code>
</dt>
<dd>the default character encoding used when transforming the input markup.
Most likely, this will be UTF-8;</dd>
<dt><code class="docutils literal"><span class="pre">raw_encoded</span>
</code></dt>
<dd>the raw input encoded in the given encoding;</dd>
<dt><code class="docutils literal"><span class="pre">outputMimeType</span>
</code></dt>
<dd>the MIME type of the default output, taken from the field at the time of
instantiation;</dd>
<dt><code class="docutils literal"><span class="pre">output</span></code></dt>
<dd>a unicode object representing the transformed output. If possible, this
is cached persistently until the <code class="docutils literal">
<span class="pre">RichTextValue</span></code> is replaced with a
new one (as happens when an edit form is saved, for example).</dd>
</dl>
"""
bio_alt1 = RichTextValue(bio_alt1_text, 'text/plain', 'text/html')
bio_alt2 = RichTextValue(bio_alt2_text, 'text/plain', 'text/html')

presentation = RichTextValue(bio_fr_text, 'text/plain', 'text/html')

missionA = {}
missionA['title'] = u'Première mission'
missionA['description'] = u'Il faut être très hardi pour aller là-bas !'
missionA['start_date'] = datetime.datetime(2016, 5, 1)
missionA['end_date'] = datetime.datetime(2016, 6, 1)
missionA['presentation'] = presentation
missionA['image'] = u'1800-IMGA0042.JPG'
missionA['img_author'] = u'S. Hervé'
missionA['thumbnail'] = u'900-IMGA0042.JPG'
missionA['doc'] = None
missionA['display_one'] = True
missionA['presentation_one'] = bio_alt1
missionA['display_two'] = True
missionA['presentation_two'] = bio_alt2


missionB = {}
missionB['title'] = u'Deuxième mission'
missionB['description'] = u'Et là, on a de la chance de revenir entiers !'
missionB['start_date'] = datetime.datetime(2016, 7, 21)
missionB['end_date'] = datetime.datetime(2016, 8, 10)
missionB['presentation'] = presentation
missionB['image'] = u'1800-IMGA0045.JPG'
missionB['img_author'] = u'H. Seb'
missionB['thumbnail'] = u'900-IMGA0045.JPG'
missionB['doc'] = None
missionB['display_one'] = True
missionB['presentation_one'] = bio_alt1
missionB['display_two'] = True
missionB['presentation_two'] = bio_alt2


missionC = {}
missionC['title'] = u'Troisième mission'
missionC['description'] = u'Et là, on a de la chance de revenir entiers !'
missionC['start_date'] = datetime.datetime(2015, 8, 21)
missionC['end_date'] = datetime.datetime(2015, 9, 10)
missionC['presentation'] = presentation
missionC['image'] = u'1800-IMGA0052.JPG'
missionC['img_author'] = u'H. Seb'
missionC['thumbnail'] = u'900-IMGA0052.JPG'
missionC['doc'] = None
missionC['display_one'] = True
missionC['presentation_one'] = bio_alt1
missionC['display_two'] = True
missionC['presentation_two'] = bio_alt2


missionD = {}
missionD['title'] = u'Quatrième mission'
missionD['description'] = u'Et là, on a de la chance de revenir entiers !'
missionD['start_date'] = datetime.datetime(2015, 1, 21)
missionD['end_date'] = datetime.datetime(2015, 3, 10)
missionD['presentation'] = presentation
missionD['image'] = u'1800-IMGA0054.JPG'
missionD['img_author'] = u'H. Seb'
missionD['thumbnail'] = u'900-IMGA0054.JPG'
missionD['doc'] = None
missionD['display_one'] = True
missionD['presentation_one'] = bio_alt1
missionD['display_two'] = True
missionD['presentation_two'] = bio_alt2

missions = []
missions.append(missionA)
missions.append(missionB)
missions.append(missionC)
missions.append(missionD)
