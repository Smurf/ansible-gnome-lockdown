.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_calendar_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_calendar module -- Manages GNOME GSettings for org.gnome.calendar
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_calendar`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.calendar' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-active-view"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calendar_module__parameter-active-view:

      .. rst-class:: ansible-option-title

      **active-view**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-active-view" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Type of the active view

      Type of the active window view, default value is: monthly view


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"month"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-active-view_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calendar_module__parameter-active-view_locked:

      .. rst-class:: ansible-option-title

      **active-view_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-active-view_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'active\-view' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-weather-settings"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calendar_module__parameter-weather-settings:

      .. rst-class:: ansible-option-title

      **weather-settings**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-weather-settings" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Weather Service Configuration

      Whether weather reports are shown, automatic locations are used and a location\-name


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"(true, true, '', nothing)"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-weather-settings_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calendar_module__parameter-weather-settings_locked:

      .. rst-class:: ansible-option-title

      **weather-settings_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-weather-settings_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'weather\-settings' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-week-view-zoom-level"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calendar_module__parameter-week-view-zoom-level:

      .. rst-class:: ansible-option-title

      **week-view-zoom-level**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-week-view-zoom-level" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Zoom level of the week grid

      The current zoom level of the week grid


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"1.0"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-week-view-zoom-level_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calendar_module__parameter-week-view-zoom-level_locked:

      .. rst-class:: ansible-option-title

      **week-view-zoom-level_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-week-view-zoom-level_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'week\-view\-zoom\-level' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-maximized"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calendar_module__parameter-window-maximized:

      .. rst-class:: ansible-option-title

      **window-maximized**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-maximized" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Window maximized

      Window maximized state


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-maximized_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calendar_module__parameter-window-maximized_locked:

      .. rst-class:: ansible-option-title

      **window-maximized_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-maximized_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'window\-maximized' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-size"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calendar_module__parameter-window-size:

      .. rst-class:: ansible-option-title

      **window-size**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-size" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Window size

      Window size (width and height).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"(768, 600)"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-size_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calendar_module__parameter-window-size_locked:

      .. rst-class:: ansible-option-title

      **window-size_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-size_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'window\-size' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.calendar
      org_gnome_calendar:
        window-maximized: true
        window-maximized_locked: true
        window-size: "(768, 600)"
        window-size_locked: true



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
