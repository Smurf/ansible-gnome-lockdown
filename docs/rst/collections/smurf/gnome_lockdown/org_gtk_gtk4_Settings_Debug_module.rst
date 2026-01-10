.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_Debug_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gtk_gtk4_Settings_Debug module -- Manages GNOME GSettings for org.gtk.gtk4.Settings.Debug
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gtk_gtk4_Settings_Debug`.

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

- This module allows for the configuration of GSettings keys within the 'org.gtk.gtk4.Settings.Debug' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-enable-inspector-keybinding"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_Debug_module__parameter-enable-inspector-keybinding:

      .. rst-class:: ansible-option-title

      **enable-inspector-keybinding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-inspector-keybinding" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable inspector keybinding

      If this setting is true, GTK lets the user open an interactive debugging window with a keybinding. The default shortcuts for the keybinding are Control\-Shift\-I and Control\-Shift\-D.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable-inspector-keybinding_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_Debug_module__parameter-enable-inspector-keybinding_locked:

      .. rst-class:: ansible-option-title

      **enable-inspector-keybinding_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-inspector-keybinding_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'enable\-inspector\-keybinding' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-inspector-warning"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_Debug_module__parameter-inspector-warning:

      .. rst-class:: ansible-option-title

      **inspector-warning**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-inspector-warning" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Inspector warning

      If this setting is true, GTK shows a warning before letting the user use the interactive debugger.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-inspector-warning_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gtk_gtk4_Settings_Debug_module__parameter-inspector-warning_locked:

      .. rst-class:: ansible-option-title

      **inspector-warning_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-inspector-warning_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'inspector\-warning' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gtk.gtk4.Settings.Debug
      org_gtk_gtk4_Settings_Debug:
        enable-inspector-keybinding: true
        enable-inspector-keybinding_locked: true
        inspector-warning: true
        inspector-warning_locked: true



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
