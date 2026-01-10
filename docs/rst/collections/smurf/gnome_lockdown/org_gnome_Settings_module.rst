.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_Settings_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_Settings module -- Manages GNOME GSettings for org.gnome.Settings
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_Settings`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.Settings' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-last-panel"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Settings_module__parameter-last-panel:

      .. rst-class:: ansible-option-title

      **last-panel**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-last-panel" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The identifier for the last Settings panel to be opened

      The identifier for the last Settings panel to be opened. Unrecognised values will be ignored and the first panel in the list selected.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-last-panel_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Settings_module__parameter-last-panel_locked:

      .. rst-class:: ansible-option-title

      **last-panel_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-last-panel_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'last\-panel' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-development-warning"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Settings_module__parameter-show-development-warning:

      .. rst-class:: ansible-option-title

      **show-development-warning**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-development-warning" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show warning when running a development build of Settings

      Whether Settings should show a warning when running a development build.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-development-warning_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Settings_module__parameter-show-development-warning_locked:

      .. rst-class:: ansible-option-title

      **show-development-warning_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-development-warning_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-development\-warning' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-state"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Settings_module__parameter-window-state:

      .. rst-class:: ansible-option-title

      **window-state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Initial state of the window

      A tuple containing the initial width, height and maximized state of the app window.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"(\-1, \-1, false)"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-state_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Settings_module__parameter-window-state_locked:

      .. rst-class:: ansible-option-title

      **window-state_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-state_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'window\-state' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.Settings
      org_gnome_Settings:
        last-panel: ""
        last-panel_locked: true
        show-development-warning: true
        show-development-warning_locked: true



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
