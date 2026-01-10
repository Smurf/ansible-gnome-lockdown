.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator module -- Manages GNOME GSettings for org.gnome.shell.extensions.appindicator
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.shell.extensions.appindicator' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-custom-icons"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-custom-icons:

      .. rst-class:: ansible-option-title

      **custom-icons**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-custom-icons" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Custom icons

      Replace any icons with custom icons from themes


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-custom-icons_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-custom-icons_locked:

      .. rst-class:: ansible-option-title

      **custom-icons_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-custom-icons_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'custom\-icons' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-brightness"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-icon-brightness:

      .. rst-class:: ansible-option-title

      **icon-brightness**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-brightness" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Brightness

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"0.0"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-brightness_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-icon-brightness_locked:

      .. rst-class:: ansible-option-title

      **icon-brightness_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-brightness_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'icon\-brightness' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-contrast"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-icon-contrast:

      .. rst-class:: ansible-option-title

      **icon-contrast**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-contrast" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Contrast

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"0.0"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-contrast_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-icon-contrast_locked:

      .. rst-class:: ansible-option-title

      **icon-contrast_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-contrast_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'icon\-contrast' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-opacity"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-icon-opacity:

      .. rst-class:: ansible-option-title

      **icon-opacity**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-opacity" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Opacity

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`240`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-opacity_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-icon-opacity_locked:

      .. rst-class:: ansible-option-title

      **icon-opacity_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-opacity_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'icon\-opacity' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-saturation"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-icon-saturation:

      .. rst-class:: ansible-option-title

      **icon-saturation**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-saturation" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Saturation

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"0.0"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-saturation_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-icon-saturation_locked:

      .. rst-class:: ansible-option-title

      **icon-saturation_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-saturation_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'icon\-saturation' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-size"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-icon-size:

      .. rst-class:: ansible-option-title

      **icon-size**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-size" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Icon size

      Icon size in pixel


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`0`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-size_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-icon-size_locked:

      .. rst-class:: ansible-option-title

      **icon-size_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-size_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'icon\-size' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-spacing"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-icon-spacing:

      .. rst-class:: ansible-option-title

      **icon-spacing**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-spacing" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Icon spacing

      Icon spacing within the tray


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`12`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-spacing_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-icon-spacing_locked:

      .. rst-class:: ansible-option-title

      **icon-spacing_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-spacing_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'icon\-spacing' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-legacy-tray-enabled"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-legacy-tray-enabled:

      .. rst-class:: ansible-option-title

      **legacy-tray-enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-legacy-tray-enabled" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable legacy tray icons support

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-legacy-tray-enabled_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-legacy-tray-enabled_locked:

      .. rst-class:: ansible-option-title

      **legacy-tray-enabled_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-legacy-tray-enabled_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'legacy\-tray\-enabled' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tray-order"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-tray-order:

      .. rst-class:: ansible-option-title

      **tray-order**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tray-order" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Order in tray

      Set where the Icon tray should appear among other trays


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tray-order_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-tray-order_locked:

      .. rst-class:: ansible-option-title

      **tray-order_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tray-order_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'tray\-order' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tray-pos"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-tray-pos:

      .. rst-class:: ansible-option-title

      **tray-pos**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tray-pos" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Position in tray

      Set where the Icon tray should appear in Gnome tray


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"right"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tray-pos_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_extensions_appindicator_module__parameter-tray-pos_locked:

      .. rst-class:: ansible-option-title

      **tray-pos_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tray-pos_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'tray\-pos' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.shell.extensions.appindicator
      org_gnome_shell_extensions_appindicator:
        legacy-tray-enabled: true
        legacy-tray-enabled_locked: true
        icon-saturation: "0.0"
        icon-saturation_locked: true



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
