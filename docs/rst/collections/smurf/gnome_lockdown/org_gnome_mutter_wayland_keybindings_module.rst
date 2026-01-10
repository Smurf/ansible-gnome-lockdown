.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings module -- Manages GNOME GSettings for org.gnome.mutter.wayland.keybindings
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.mutter.wayland.keybindings' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-restore-shortcuts"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-restore-shortcuts:

      .. rst-class:: ansible-option-title

      **restore-shortcuts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-restore-shortcuts" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Re\-enable shortcuts

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>Escape']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-restore-shortcuts_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-restore-shortcuts_locked:

      .. rst-class:: ansible-option-title

      **restore-shortcuts_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-restore-shortcuts_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'restore\-shortcuts' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-1"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-1:

      .. rst-class:: ansible-option-title

      **switch-to-session-1**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-1" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to VT 1

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Primary\>\<Alt\>F1']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-10"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-10:

      .. rst-class:: ansible-option-title

      **switch-to-session-10**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-10" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to VT 10

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Primary\>\<Alt\>F10']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-10_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-10_locked:

      .. rst-class:: ansible-option-title

      **switch-to-session-10_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-10_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-session\-10' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-11"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-11:

      .. rst-class:: ansible-option-title

      **switch-to-session-11**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-11" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to VT 11

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Primary\>\<Alt\>F11']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-11_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-11_locked:

      .. rst-class:: ansible-option-title

      **switch-to-session-11_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-11_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-session\-11' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-12"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-12:

      .. rst-class:: ansible-option-title

      **switch-to-session-12**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-12" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to VT 12

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Primary\>\<Alt\>F12']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-12_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-12_locked:

      .. rst-class:: ansible-option-title

      **switch-to-session-12_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-12_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-session\-12' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-1_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-1_locked:

      .. rst-class:: ansible-option-title

      **switch-to-session-1_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-1_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-session\-1' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-2"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-2:

      .. rst-class:: ansible-option-title

      **switch-to-session-2**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-2" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to VT 2

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Primary\>\<Alt\>F2']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-2_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-2_locked:

      .. rst-class:: ansible-option-title

      **switch-to-session-2_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-2_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-session\-2' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-3"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-3:

      .. rst-class:: ansible-option-title

      **switch-to-session-3**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-3" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to VT 3

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Primary\>\<Alt\>F3']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-3_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-3_locked:

      .. rst-class:: ansible-option-title

      **switch-to-session-3_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-3_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-session\-3' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-4"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-4:

      .. rst-class:: ansible-option-title

      **switch-to-session-4**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-4" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to VT 4

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Primary\>\<Alt\>F4']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-4_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-4_locked:

      .. rst-class:: ansible-option-title

      **switch-to-session-4_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-4_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-session\-4' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-5"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-5:

      .. rst-class:: ansible-option-title

      **switch-to-session-5**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-5" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to VT 5

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Primary\>\<Alt\>F5']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-5_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-5_locked:

      .. rst-class:: ansible-option-title

      **switch-to-session-5_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-5_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-session\-5' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-6"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-6:

      .. rst-class:: ansible-option-title

      **switch-to-session-6**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-6" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to VT 6

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Primary\>\<Alt\>F6']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-6_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-6_locked:

      .. rst-class:: ansible-option-title

      **switch-to-session-6_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-6_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-session\-6' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-7"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-7:

      .. rst-class:: ansible-option-title

      **switch-to-session-7**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-7" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to VT 7

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Primary\>\<Alt\>F7']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-7_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-7_locked:

      .. rst-class:: ansible-option-title

      **switch-to-session-7_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-7_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-session\-7' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-8"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-8:

      .. rst-class:: ansible-option-title

      **switch-to-session-8**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-8" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to VT 8

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Primary\>\<Alt\>F8']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-8_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-8_locked:

      .. rst-class:: ansible-option-title

      **switch-to-session-8_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-8_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-session\-8' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-9"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-9:

      .. rst-class:: ansible-option-title

      **switch-to-session-9**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-9" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to VT 9

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Primary\>\<Alt\>F9']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-session-9_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_wayland_keybindings_module__parameter-switch-to-session-9_locked:

      .. rst-class:: ansible-option-title

      **switch-to-session-9_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-session-9_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-session\-9' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.mutter.wayland.keybindings
      org_gnome_mutter_wayland_keybindings:
        switch-to-session-1: "['<Primary><Alt>F1']"
        switch-to-session-1_locked: true
        switch-to-session-2: "['<Primary><Alt>F2']"
        switch-to-session-2_locked: true



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
