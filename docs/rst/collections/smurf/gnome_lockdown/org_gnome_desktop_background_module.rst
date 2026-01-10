.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_desktop_background module -- Manages GNOME GSettings for org.gnome.desktop.background
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_desktop_background`.

.. version_added

.. rst-class:: ansible-version-added

New in smurf.gnome\_lockdown 1.0.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows for the configuration of GSettings keys within the 'org.gnome.desktop.background' schema.
- It supports setting default values and locking keys to enforce system\-wide policies.


.. Aliases


.. Requirements






.. Options

Parameters
----------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-color-shading-type"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-color-shading-type:

      .. rst-class:: ansible-option-title

      **color-shading-type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-color-shading-type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Color Shading Type

      How to shade the background color. Possible values are “horizontal”, “vertical”, and “solid”.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"solid"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-color-shading-type_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-color-shading-type_locked:

      .. rst-class:: ansible-option-title

      **color-shading-type_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-color-shading-type_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'color\-shading\-type' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-opacity"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-picture-opacity:

      .. rst-class:: ansible-option-title

      **picture-opacity**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-opacity" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Picture Opacity

      Opacity with which to draw the background picture.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`100`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-opacity_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-picture-opacity_locked:

      .. rst-class:: ansible-option-title

      **picture-opacity_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-opacity_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'picture\-opacity' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-options"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-picture-options:

      .. rst-class:: ansible-option-title

      **picture-options**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-options" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Picture Options

      Determines how the image set by wallpaper\_filename is rendered. Possible values are “none”, “wallpaper”, “centered”, “scaled”, “stretched”, “zoom”, “spanned”.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"zoom"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-options_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-picture-options_locked:

      .. rst-class:: ansible-option-title

      **picture-options_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-options_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'picture\-options' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-uri"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-picture-uri:

      .. rst-class:: ansible-option-title

      **picture-uri**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-uri" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Picture URI

      URI to use for the background image. Note that the backend only supports local (file://) URIs.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"file:///usr/share/backgrounds/gnome/adwaita\-l.jpg"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-uri-dark"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-picture-uri-dark:

      .. rst-class:: ansible-option-title

      **picture-uri-dark**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-uri-dark" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Picture URI (dark)

      URI to use for the background image. Note that the backend only supports local (file://) URIs.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"file:///usr/share/backgrounds/gnome/adwaita\-d.jpg"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-uri-dark_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-picture-uri-dark_locked:

      .. rst-class:: ansible-option-title

      **picture-uri-dark_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-uri-dark_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'picture\-uri\-dark' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-uri_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-picture-uri_locked:

      .. rst-class:: ansible-option-title

      **picture-uri_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-uri_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'picture\-uri' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-primary-color"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-primary-color:

      .. rst-class:: ansible-option-title

      **primary-color**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-primary-color" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Primary Color

      Left or Top color when drawing gradients, or the solid color.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"#023c88"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-primary-color_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-primary-color_locked:

      .. rst-class:: ansible-option-title

      **primary-color_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-primary-color_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'primary\-color' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-secondary-color"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-secondary-color:

      .. rst-class:: ansible-option-title

      **secondary-color**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-secondary-color" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Secondary Color

      Right or Bottom color when drawing gradients, not used for solid color.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"#5789ca"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-secondary-color_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-secondary-color_locked:

      .. rst-class:: ansible-option-title

      **secondary-color_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-secondary-color_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'secondary\-color' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-desktop-icons"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-show-desktop-icons:

      .. rst-class:: ansible-option-title

      **show-desktop-icons**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-desktop-icons" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Have file manager handle the desktop

      If set to true, then file manager will draw the icons on the desktop.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-desktop-icons_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_background_module__parameter-show-desktop-icons_locked:

      .. rst-class:: ansible-option-title

      **show-desktop-icons_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-desktop-icons_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-desktop\-icons' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    - name: Configure and lock GNOME desktop settings for org.gnome.desktop.background
      org_gnome_desktop_background:
        picture-options: "zoom"
        picture-options_locked: true
        picture-uri: "file:///usr/share/backgrounds/gnome/adwaita-l.jpg"
        picture-uri_locked: true



.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Autogenerated by ansible-gnome-lockdown


.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/Smurf/ansible-gnome-lockdown/issues"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/Smurf/ansible-gnome-lockdown"
    external: true


.. Parsing errors
