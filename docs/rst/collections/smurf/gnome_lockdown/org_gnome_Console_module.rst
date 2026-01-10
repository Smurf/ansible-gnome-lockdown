.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_Console module -- Manages GNOME GSettings for org.gnome.Console
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_Console`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.Console' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-audible-bell"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-audible-bell:

      .. rst-class:: ansible-option-title

      **audible-bell**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-audible-bell" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-audible-bell_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-audible-bell_locked:

      .. rst-class:: ansible-option-title

      **audible-bell_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-audible-bell_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'audible\-bell' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-custom-font"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-custom-font:

      .. rst-class:: ansible-option-title

      **custom-font**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-custom-font" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-custom-font_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-custom-font_locked:

      .. rst-class:: ansible-option-title

      **custom-font_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-custom-font_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'custom\-font' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-custom-liveries"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-custom-liveries:

      .. rst-class:: ansible-option-title

      **custom-liveries**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-custom-liveries" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"{}"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-custom-liveries_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-custom-liveries_locked:

      .. rst-class:: ansible-option-title

      **custom-liveries_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-custom-liveries_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'custom\-liveries' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-font-scale"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-font-scale:

      .. rst-class:: ansible-option-title

      **font-scale**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-font-scale" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"1.0"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-font-scale_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-font-scale_locked:

      .. rst-class:: ansible-option-title

      **font-scale_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-font-scale_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'font\-scale' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignore-scrollback-limit"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-ignore-scrollback-limit:

      .. rst-class:: ansible-option-title

      **ignore-scrollback-limit**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignore-scrollback-limit" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignore-scrollback-limit_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-ignore-scrollback-limit_locked:

      .. rst-class:: ansible-option-title

      **ignore-scrollback-limit_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignore-scrollback-limit_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'ignore\-scrollback\-limit' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-last-window-maximised"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-last-window-maximised:

      .. rst-class:: ansible-option-title

      **last-window-maximised**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-last-window-maximised" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-last-window-maximised_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-last-window-maximised_locked:

      .. rst-class:: ansible-option-title

      **last-window-maximised_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-last-window-maximised_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'last\-window\-maximised' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-last-window-size"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-last-window-size:

      .. rst-class:: ansible-option-title

      **last-window-size**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-last-window-size" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"(\-1, \-1)"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-last-window-size_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-last-window-size_locked:

      .. rst-class:: ansible-option-title

      **last-window-size_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-last-window-size_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'last\-window\-size' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-livery"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-livery:

      .. rst-class:: ansible-option-title

      **livery**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-livery" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"9f1374fd\-f199\-429f\-bae6\-9cf1260f6e3e"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-livery_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-livery_locked:

      .. rst-class:: ansible-option-title

      **livery_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-livery_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'livery' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-restore-window-size"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-restore-window-size:

      .. rst-class:: ansible-option-title

      **restore-window-size**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-restore-window-size" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-restore-window-size_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-restore-window-size_locked:

      .. rst-class:: ansible-option-title

      **restore-window-size_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-restore-window-size_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'restore\-window\-size' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-scrollback-lines"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-scrollback-lines:

      .. rst-class:: ansible-option-title

      **scrollback-lines**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-scrollback-lines" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"10000"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-scrollback-lines_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-scrollback-lines_locked:

      .. rst-class:: ansible-option-title

      **scrollback-lines_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-scrollback-lines_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'scrollback\-lines' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-shell"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-shell:

      .. rst-class:: ansible-option-title

      **shell**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-shell" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-shell_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-shell_locked:

      .. rst-class:: ansible-option-title

      **shell_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-shell_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'shell' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-software-flow-control"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-software-flow-control:

      .. rst-class:: ansible-option-title

      **software-flow-control**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-software-flow-control" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-software-flow-control_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-software-flow-control_locked:

      .. rst-class:: ansible-option-title

      **software-flow-control_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-software-flow-control_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'software\-flow\-control' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-theme"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-theme:

      .. rst-class:: ansible-option-title

      **theme**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-theme" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"night"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-theme_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-theme_locked:

      .. rst-class:: ansible-option-title

      **theme_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-theme_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'theme' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-transparency"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-transparency:

      .. rst-class:: ansible-option-title

      **transparency**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-transparency" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-transparency_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-transparency_locked:

      .. rst-class:: ansible-option-title

      **transparency_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-transparency_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'transparency' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-use-system-font"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-use-system-font:

      .. rst-class:: ansible-option-title

      **use-system-font**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-use-system-font" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-use-system-font_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-use-system-font_locked:

      .. rst-class:: ansible-option-title

      **use-system-font_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-use-system-font_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'use\-system\-font' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-visual-bell"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-visual-bell:

      .. rst-class:: ansible-option-title

      **visual-bell**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-visual-bell" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Summary \- Schema Blank

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-visual-bell_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Console_module__parameter-visual-bell_locked:

      .. rst-class:: ansible-option-title

      **visual-bell_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-visual-bell_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'visual\-bell' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.Console
      org_gnome_Console:
        theme: "night"
        theme_locked: true
        font-scale: "1.0"
        font-scale_locked: true



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
