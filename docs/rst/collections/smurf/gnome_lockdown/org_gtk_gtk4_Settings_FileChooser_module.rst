.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser module -- Manages GNOME GSettings for org.gtk.gtk4.Settings.FileChooser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser`.

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

- This module allows for the configuration of GSettings keys within the 'org.gtk.gtk4.Settings.FileChooser' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-clock-format"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-clock-format:

      .. rst-class:: ansible-option-title

      **clock-format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clock-format" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Time format

      Whether the time is shown in 24h or 12h format.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"24h"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clock-format_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-clock-format_locked:

      .. rst-class:: ansible-option-title

      **clock-format_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clock-format_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'clock\-format' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-date-format"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-date-format:

      .. rst-class:: ansible-option-title

      **date-format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-date-format" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Date format

      The amount of detail to show in the Modified column.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"regular"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-date-format_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-date-format_locked:

      .. rst-class:: ansible-option-title

      **date-format_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-date-format_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'date\-format' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-expand-folders"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-expand-folders:

      .. rst-class:: ansible-option-title

      **expand-folders**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-expand-folders" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expand folders

      This key is deprecated; do not use it.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-expand-folders_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-expand-folders_locked:

      .. rst-class:: ansible-option-title

      **expand-folders_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-expand-folders_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'expand\-folders' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-location-mode"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-location-mode:

      .. rst-class:: ansible-option-title

      **location-mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-location-mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Location mode

      Controls whether the file chooser shows just a path bar, or a visible entry for the filename as well, for the benefit of typing\-oriented users. The possible values for these modes are "path\-bar" and "filename\-entry".


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"path\-bar"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-location-mode_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-location-mode_locked:

      .. rst-class:: ansible-option-title

      **location-mode_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-location-mode_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'location\-mode' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-hidden"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-show-hidden:

      .. rst-class:: ansible-option-title

      **show-hidden**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-hidden" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show hidden files

      Controls whether the file chooser shows hidden files or not.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-hidden_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-show-hidden_locked:

      .. rst-class:: ansible-option-title

      **show-hidden_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-hidden_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-hidden' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-size-column"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-show-size-column:

      .. rst-class:: ansible-option-title

      **show-size-column**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-size-column" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show file sizes

      Controls whether the file chooser shows a column with file sizes.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-size-column_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-show-size-column_locked:

      .. rst-class:: ansible-option-title

      **show-size-column_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-size-column_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-size\-column' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-type-column"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-show-type-column:

      .. rst-class:: ansible-option-title

      **show-type-column**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-type-column" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show file types

      Controls whether the file chooser shows a column with file types.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-type-column_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-show-type-column_locked:

      .. rst-class:: ansible-option-title

      **show-type-column_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-type-column_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-type\-column' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sidebar-width"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-sidebar-width:

      .. rst-class:: ansible-option-title

      **sidebar-width**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sidebar-width" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Sidebar width

      Width in pixels of the file chooser's places sidebar.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`\-1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sidebar-width_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-sidebar-width_locked:

      .. rst-class:: ansible-option-title

      **sidebar-width_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sidebar-width_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'sidebar\-width' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sort-column"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-sort-column:

      .. rst-class:: ansible-option-title

      **sort-column**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sort-column" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Sort column

      Can be one of "name", "modified", or "size". It controls which of the columns in the file chooser is used for sorting the list of files.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"name"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sort-column_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-sort-column_locked:

      .. rst-class:: ansible-option-title

      **sort-column_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sort-column_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'sort\-column' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sort-directories-first"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-sort-directories-first:

      .. rst-class:: ansible-option-title

      **sort-directories-first**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sort-directories-first" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show folders first

      If set to true, then folders are shown before files in the list.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sort-directories-first_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-sort-directories-first_locked:

      .. rst-class:: ansible-option-title

      **sort-directories-first_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sort-directories-first_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'sort\-directories\-first' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sort-order"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-sort-order:

      .. rst-class:: ansible-option-title

      **sort-order**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sort-order" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Sort order

      Can be one of the strings "ascending" or "descending".


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"ascending"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sort-order_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-sort-order_locked:

      .. rst-class:: ansible-option-title

      **sort-order_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sort-order_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'sort\-order' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-startup-mode"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-startup-mode:

      .. rst-class:: ansible-option-title

      **startup-mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-startup-mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Startup mode

      Either "recent" or "cwd"; controls whether the file chooser starts up showing the list of recently\-used files, or the contents of the current working directory.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"recent"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-startup-mode_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-startup-mode_locked:

      .. rst-class:: ansible-option-title

      **startup-mode_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-startup-mode_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'startup\-mode' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-type-format"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-type-format:

      .. rst-class:: ansible-option-title

      **type-format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-type-format" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Type format

      Different ways to show the 'Type' column information. Example outputs for a video mp4 file: 'mime' \-\> 'video/mp4' 'description' \-\> 'MPEG\-4 video' 'category' \-\> 'Video'


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"category"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-type-format_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-type-format_locked:

      .. rst-class:: ansible-option-title

      **type-format_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-type-format_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'type\-format' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-view-type"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-view-type:

      .. rst-class:: ansible-option-title

      **view-type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-view-type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      View type

      Whether the files are shown in a list or in a grid.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"list"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-view-type_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-view-type_locked:

      .. rst-class:: ansible-option-title

      **view-type_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-view-type_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'view\-type' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-position"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-window-position:

      .. rst-class:: ansible-option-title

      **window-position**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-position" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Window position

      This key is ignored.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"(\-1, \-1)"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-position_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-window-position_locked:

      .. rst-class:: ansible-option-title

      **window-position_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-position_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'window\-position' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-size"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-window-size:

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

      The size (width, height) of the GtkFileChooserDialog's window, in pixels.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"(\-1, \-1)"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-size_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_FileChooser_module__parameter-window-size_locked:

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

    - name: Configure and lock GNOME desktop settings for org.gtk.gtk4.Settings.FileChooser
      org_gtk_gtk4_Settings_FileChooser:
        location-mode: "path-bar"
        location-mode_locked: true
        show-hidden: false
        show-hidden_locked: true



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
