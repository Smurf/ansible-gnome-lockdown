.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_ColorChooser_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gtk_gtk4_Settings_ColorChooser module -- Manages GNOME GSettings for org.gtk.gtk4.Settings.ColorChooser
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gtk_gtk4_Settings_ColorChooser`.

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

- This module allows for the configuration of GSettings keys within the 'org.gtk.gtk4.Settings.ColorChooser' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-custom-colors"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_ColorChooser_module__parameter-custom-colors:

      .. rst-class:: ansible-option-title

      **custom-colors**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-custom-colors" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Custom colors

      An array of custom colors to show in the color chooser. Each color is specified as a tuple of four doubles, specifying RGBA values between 0 and 1.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-custom-colors_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_ColorChooser_module__parameter-custom-colors_locked:

      .. rst-class:: ansible-option-title

      **custom-colors_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-custom-colors_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'custom\-colors' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-selected-color"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_ColorChooser_module__parameter-selected-color:

      .. rst-class:: ansible-option-title

      **selected-color**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-selected-color" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The selected color

      The selected color, described as a tuple whose first member is a boolean that is true if a color was selected, and the remaining four members are four doubles, specifying RGBA values between 0 and 1.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"(false,1.0,1.0,1.0,1.0)"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-selected-color_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_ColorChooser_module__parameter-selected-color_locked:

      .. rst-class:: ansible-option-title

      **selected-color_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-selected-color_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'selected\-color' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gtk.gtk4.Settings.ColorChooser
      org_gtk_gtk4_Settings_ColorChooser:
        custom-colors: []
        custom-colors_locked: true
        selected-color: "(false,1.0,1.0,1.0,1.0)"
        selected-color_locked: true



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
