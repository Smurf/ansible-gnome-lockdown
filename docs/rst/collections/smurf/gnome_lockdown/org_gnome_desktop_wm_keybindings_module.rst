.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings module -- Manages GNOME GSettings for org.gnome.desktop.wm.keybindings
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.desktop.wm.keybindings' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-activate-window-menu"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-activate-window-menu:

      .. rst-class:: ansible-option-title

      **activate-window-menu**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-activate-window-menu" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Activate the window menu

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Alt\>space']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-activate-window-menu_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-activate-window-menu_locked:

      .. rst-class:: ansible-option-title

      **activate-window-menu_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-activate-window-menu_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'activate\-window\-menu' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-always-on-top"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-always-on-top:

      .. rst-class:: ansible-option-title

      **always-on-top**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-always-on-top" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Toggle window to be always on top

      Set or unset window to appear always on top


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-always-on-top_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-always-on-top_locked:

      .. rst-class:: ansible-option-title

      **always-on-top_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-always-on-top_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'always\-on\-top' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-begin-move"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-begin-move:

      .. rst-class:: ansible-option-title

      **begin-move**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-begin-move" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Alt\>F7']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-begin-move_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-begin-move_locked:

      .. rst-class:: ansible-option-title

      **begin-move_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-begin-move_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'begin\-move' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-begin-resize"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-begin-resize:

      .. rst-class:: ansible-option-title

      **begin-resize**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-begin-resize" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Resize window

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Alt\>F8']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-begin-resize_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-begin-resize_locked:

      .. rst-class:: ansible-option-title

      **begin-resize_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-begin-resize_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'begin\-resize' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-close"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-close:

      .. rst-class:: ansible-option-title

      **close**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-close" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Close window

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Alt\>F4']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-close_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-close_locked:

      .. rst-class:: ansible-option-title

      **close_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-close_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'close' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cycle-group"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-cycle-group:

      .. rst-class:: ansible-option-title

      **cycle-group**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cycle-group" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch windows of an app directly

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Alt\>F6']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cycle-group-backward"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-cycle-group-backward:

      .. rst-class:: ansible-option-title

      **cycle-group-backward**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cycle-group-backward" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Reverse switch windows of an app directly

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Shift\>\<Alt\>F6']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cycle-group-backward_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-cycle-group-backward_locked:

      .. rst-class:: ansible-option-title

      **cycle-group-backward_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cycle-group-backward_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'cycle\-group\-backward' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cycle-group_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-cycle-group_locked:

      .. rst-class:: ansible-option-title

      **cycle-group_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cycle-group_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'cycle\-group' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cycle-panels"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-cycle-panels:

      .. rst-class:: ansible-option-title

      **cycle-panels**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cycle-panels" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch system controls directly

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Control\>\<Alt\>Escape']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cycle-panels-backward"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-cycle-panels-backward:

      .. rst-class:: ansible-option-title

      **cycle-panels-backward**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cycle-panels-backward" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Reverse switch system controls directly

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Shift\>\<Control\>\<Alt\>Escape']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cycle-panels-backward_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-cycle-panels-backward_locked:

      .. rst-class:: ansible-option-title

      **cycle-panels-backward_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cycle-panels-backward_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'cycle\-panels\-backward' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cycle-panels_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-cycle-panels_locked:

      .. rst-class:: ansible-option-title

      **cycle-panels_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cycle-panels_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'cycle\-panels' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cycle-windows"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-cycle-windows:

      .. rst-class:: ansible-option-title

      **cycle-windows**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cycle-windows" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch windows directly

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Alt\>Escape']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cycle-windows-backward"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-cycle-windows-backward:

      .. rst-class:: ansible-option-title

      **cycle-windows-backward**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cycle-windows-backward" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Reverse switch windows directly

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Shift\>\<Alt\>Escape']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cycle-windows-backward_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-cycle-windows-backward_locked:

      .. rst-class:: ansible-option-title

      **cycle-windows-backward_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cycle-windows-backward_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'cycle\-windows\-backward' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cycle-windows_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-cycle-windows_locked:

      .. rst-class:: ansible-option-title

      **cycle-windows_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cycle-windows_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'cycle\-windows' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lower"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-lower:

      .. rst-class:: ansible-option-title

      **lower**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lower" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Lower window below other windows

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lower_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-lower_locked:

      .. rst-class:: ansible-option-title

      **lower_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lower_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'lower' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-maximize"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-maximize:

      .. rst-class:: ansible-option-title

      **maximize**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-maximize" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximize window

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>Up']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-maximize-horizontally"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-maximize-horizontally:

      .. rst-class:: ansible-option-title

      **maximize-horizontally**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-maximize-horizontally" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximize window horizontally

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-maximize-horizontally_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-maximize-horizontally_locked:

      .. rst-class:: ansible-option-title

      **maximize-horizontally_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-maximize-horizontally_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'maximize\-horizontally' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-maximize-vertically"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-maximize-vertically:

      .. rst-class:: ansible-option-title

      **maximize-vertically**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-maximize-vertically" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximize window vertically

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-maximize-vertically_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-maximize-vertically_locked:

      .. rst-class:: ansible-option-title

      **maximize-vertically_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-maximize-vertically_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'maximize\-vertically' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-maximize_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-maximize_locked:

      .. rst-class:: ansible-option-title

      **maximize_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-maximize_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'maximize' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-minimize"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-minimize:

      .. rst-class:: ansible-option-title

      **minimize**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-minimize" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Minimize window

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>h']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-minimize_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-minimize_locked:

      .. rst-class:: ansible-option-title

      **minimize_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-minimize_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'minimize' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-center"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-center:

      .. rst-class:: ansible-option-title

      **move-to-center**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-center" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to center of screen

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-center_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-center_locked:

      .. rst-class:: ansible-option-title

      **move-to-center_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-center_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-center' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-corner-ne"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-corner-ne:

      .. rst-class:: ansible-option-title

      **move-to-corner-ne**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-corner-ne" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to top right corner

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-corner-ne_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-corner-ne_locked:

      .. rst-class:: ansible-option-title

      **move-to-corner-ne_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-corner-ne_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-corner\-ne' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-corner-nw"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-corner-nw:

      .. rst-class:: ansible-option-title

      **move-to-corner-nw**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-corner-nw" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to top left corner

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-corner-nw_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-corner-nw_locked:

      .. rst-class:: ansible-option-title

      **move-to-corner-nw_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-corner-nw_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-corner\-nw' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-corner-se"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-corner-se:

      .. rst-class:: ansible-option-title

      **move-to-corner-se**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-corner-se" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to bottom right corner

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-corner-se_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-corner-se_locked:

      .. rst-class:: ansible-option-title

      **move-to-corner-se_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-corner-se_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-corner\-se' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-corner-sw"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-corner-sw:

      .. rst-class:: ansible-option-title

      **move-to-corner-sw**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-corner-sw" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to bottom left corner

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-corner-sw_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-corner-sw_locked:

      .. rst-class:: ansible-option-title

      **move-to-corner-sw_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-corner-sw_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-corner\-sw' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-monitor-down"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-monitor-down:

      .. rst-class:: ansible-option-title

      **move-to-monitor-down**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-monitor-down" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to the next monitor below

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>\<Shift\>Down']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-monitor-down_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-monitor-down_locked:

      .. rst-class:: ansible-option-title

      **move-to-monitor-down_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-monitor-down_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-monitor\-down' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-monitor-left"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-monitor-left:

      .. rst-class:: ansible-option-title

      **move-to-monitor-left**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-monitor-left" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to the next monitor on the left

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>\<Shift\>Left']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-monitor-left_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-monitor-left_locked:

      .. rst-class:: ansible-option-title

      **move-to-monitor-left_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-monitor-left_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-monitor\-left' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-monitor-right"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-monitor-right:

      .. rst-class:: ansible-option-title

      **move-to-monitor-right**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-monitor-right" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to the next monitor on the right

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>\<Shift\>Right']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-monitor-right_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-monitor-right_locked:

      .. rst-class:: ansible-option-title

      **move-to-monitor-right_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-monitor-right_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-monitor\-right' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-monitor-up"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-monitor-up:

      .. rst-class:: ansible-option-title

      **move-to-monitor-up**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-monitor-up" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to the next monitor above

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>\<Shift\>Up']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-monitor-up_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-monitor-up_locked:

      .. rst-class:: ansible-option-title

      **move-to-monitor-up_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-monitor-up_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-monitor\-up' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-side-e"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-side-e:

      .. rst-class:: ansible-option-title

      **move-to-side-e**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-side-e" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to right side of screen

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-side-e_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-side-e_locked:

      .. rst-class:: ansible-option-title

      **move-to-side-e_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-side-e_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-side\-e' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-side-n"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-side-n:

      .. rst-class:: ansible-option-title

      **move-to-side-n**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-side-n" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to top edge of screen

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-side-n_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-side-n_locked:

      .. rst-class:: ansible-option-title

      **move-to-side-n_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-side-n_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-side\-n' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-side-s"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-side-s:

      .. rst-class:: ansible-option-title

      **move-to-side-s**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-side-s" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to bottom edge of screen

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-side-s_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-side-s_locked:

      .. rst-class:: ansible-option-title

      **move-to-side-s_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-side-s_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-side\-s' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-side-w"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-side-w:

      .. rst-class:: ansible-option-title

      **move-to-side-w**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-side-w" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to left side of screen

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-side-w_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-side-w_locked:

      .. rst-class:: ansible-option-title

      **move-to-side-w_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-side-w_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-side\-w' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-1"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-1:

      .. rst-class:: ansible-option-title

      **move-to-workspace-1**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-1" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to workspace 1

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>\<Shift\>Home']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-10"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-10:

      .. rst-class:: ansible-option-title

      **move-to-workspace-10**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-10" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to workspace 10

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-10_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-10_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-10_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-10_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-10' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-11"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-11:

      .. rst-class:: ansible-option-title

      **move-to-workspace-11**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-11" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to workspace 11

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-11_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-11_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-11_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-11_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-11' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-12"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-12:

      .. rst-class:: ansible-option-title

      **move-to-workspace-12**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-12" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to workspace 12

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-12_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-12_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-12_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-12_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-12' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-1_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-1_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-1_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-1_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-1' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-2"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-2:

      .. rst-class:: ansible-option-title

      **move-to-workspace-2**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-2" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to workspace 2

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-2_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-2_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-2_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-2_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-2' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-3"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-3:

      .. rst-class:: ansible-option-title

      **move-to-workspace-3**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-3" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to workspace 3

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-3_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-3_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-3_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-3_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-3' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-4"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-4:

      .. rst-class:: ansible-option-title

      **move-to-workspace-4**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-4" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to workspace 4

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-4_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-4_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-4_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-4_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-4' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-5"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-5:

      .. rst-class:: ansible-option-title

      **move-to-workspace-5**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-5" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to workspace 5

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-5_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-5_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-5_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-5_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-5' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-6"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-6:

      .. rst-class:: ansible-option-title

      **move-to-workspace-6**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-6" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to workspace 6

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-6_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-6_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-6_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-6_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-6' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-7"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-7:

      .. rst-class:: ansible-option-title

      **move-to-workspace-7**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-7" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to workspace 7

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-7_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-7_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-7_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-7_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-7' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-8"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-8:

      .. rst-class:: ansible-option-title

      **move-to-workspace-8**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-8" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to workspace 8

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-8_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-8_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-8_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-8_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-8' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-9"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-9:

      .. rst-class:: ansible-option-title

      **move-to-workspace-9**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-9" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to workspace 9

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-9_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-9_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-9_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-9_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-9' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-down"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-down:

      .. rst-class:: ansible-option-title

      **move-to-workspace-down**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-down" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window one workspace down

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Control\>\<Shift\>\<Alt\>Down']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-down_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-down_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-down_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-down_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-down' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-last"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-last:

      .. rst-class:: ansible-option-title

      **move-to-workspace-last**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-last" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window to last workspace

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>\<Shift\>End']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-last_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-last_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-last_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-last_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-last' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-left"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-left:

      .. rst-class:: ansible-option-title

      **move-to-workspace-left**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-left" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window one workspace to the left

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>\<Shift\>Page\_Up','\<Super\>\<Shift\>\<Alt\>Left','\<Control\>\<Shift\>\<Alt\>Left']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-left_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-left_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-left_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-left_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-left' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-right"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-right:

      .. rst-class:: ansible-option-title

      **move-to-workspace-right**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-right" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window one workspace to the right

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>\<Shift\>Page\_Down','\<Super\>\<Shift\>\<Alt\>Right','\<Control\>\<Shift\>\<Alt\>Right']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-right_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-right_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-right_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-right_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-right' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-up"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-up:

      .. rst-class:: ansible-option-title

      **move-to-workspace-up**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-up" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Move window one workspace up

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Control\>\<Shift\>\<Alt\>Up']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-move-to-workspace-up_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-move-to-workspace-up_locked:

      .. rst-class:: ansible-option-title

      **move-to-workspace-up_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-move-to-workspace-up_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'move\-to\-workspace\-up' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-panel-main-menu"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-panel-main-menu:

      .. rst-class:: ansible-option-title

      **panel-main-menu**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-panel-main-menu" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      DEPRECATED: This key is deprecated and ignored.

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-panel-main-menu_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-panel-main-menu_locked:

      .. rst-class:: ansible-option-title

      **panel-main-menu_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-panel-main-menu_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'panel\-main\-menu' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-panel-run-dialog"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-panel-run-dialog:

      .. rst-class:: ansible-option-title

      **panel-run-dialog**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-panel-run-dialog" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show the run command prompt

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Alt\>F2']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-panel-run-dialog_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-panel-run-dialog_locked:

      .. rst-class:: ansible-option-title

      **panel-run-dialog_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-panel-run-dialog_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'panel\-run\-dialog' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-raise"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-raise:

      .. rst-class:: ansible-option-title

      **raise**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-raise" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Raise window above other windows

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-raise-or-lower"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-raise-or-lower:

      .. rst-class:: ansible-option-title

      **raise-or-lower**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-raise-or-lower" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Raise window if covered, otherwise lower it

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-raise-or-lower_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-raise-or-lower_locked:

      .. rst-class:: ansible-option-title

      **raise-or-lower_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-raise-or-lower_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'raise\-or\-lower' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-raise_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-raise_locked:

      .. rst-class:: ansible-option-title

      **raise_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-raise_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'raise' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-set-spew-mark"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-set-spew-mark:

      .. rst-class:: ansible-option-title

      **set-spew-mark**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-set-spew-mark" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Don’t use

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-set-spew-mark_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-set-spew-mark_locked:

      .. rst-class:: ansible-option-title

      **set-spew-mark_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-set-spew-mark_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'set\-spew\-mark' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-desktop"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-show-desktop:

      .. rst-class:: ansible-option-title

      **show-desktop**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-desktop" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Hide all normal windows

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-desktop_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-show-desktop_locked:

      .. rst-class:: ansible-option-title

      **show-desktop_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-desktop_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-desktop' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-applications"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-applications:

      .. rst-class:: ansible-option-title

      **switch-applications**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-applications" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch applications

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>Tab','\<Alt\>Tab']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-applications-backward"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-applications-backward:

      .. rst-class:: ansible-option-title

      **switch-applications-backward**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-applications-backward" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Reverse switch applications

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Shift\>\<Super\>Tab','\<Shift\>\<Alt\>Tab']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-applications-backward_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-applications-backward_locked:

      .. rst-class:: ansible-option-title

      **switch-applications-backward_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-applications-backward_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-applications\-backward' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-applications_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-applications_locked:

      .. rst-class:: ansible-option-title

      **switch-applications_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-applications_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-applications' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-group"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-group:

      .. rst-class:: ansible-option-title

      **switch-group**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-group" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch windows of an application

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>Above\_Tab','\<Alt\>Above\_Tab']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-group-backward"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-group-backward:

      .. rst-class:: ansible-option-title

      **switch-group-backward**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-group-backward" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Reverse switch windows of an application

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Shift\>\<Super\>Above\_Tab','\<Shift\>\<Alt\>Above\_Tab']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-group-backward_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-group-backward_locked:

      .. rst-class:: ansible-option-title

      **switch-group-backward_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-group-backward_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-group\-backward' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-group_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-group_locked:

      .. rst-class:: ansible-option-title

      **switch-group_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-group_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-group' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-input-source"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-input-source:

      .. rst-class:: ansible-option-title

      **switch-input-source**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-input-source" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch input source

      Binding to select the next input source


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>space','XF86Keyboard']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-input-source-backward"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-input-source-backward:

      .. rst-class:: ansible-option-title

      **switch-input-source-backward**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-input-source-backward" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch input source backward

      Binding to select the previous input source


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Shift\>\<Super\>space','\<Shift\>XF86Keyboard']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-input-source-backward_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-input-source-backward_locked:

      .. rst-class:: ansible-option-title

      **switch-input-source-backward_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-input-source-backward_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-input\-source\-backward' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-input-source_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-input-source_locked:

      .. rst-class:: ansible-option-title

      **switch-input-source_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-input-source_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-input\-source' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-panels"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-panels:

      .. rst-class:: ansible-option-title

      **switch-panels**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-panels" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch system controls

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Control\>\<Alt\>Tab']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-panels-backward"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-panels-backward:

      .. rst-class:: ansible-option-title

      **switch-panels-backward**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-panels-backward" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Reverse switch system controls

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Shift\>\<Control\>\<Alt\>Tab']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-panels-backward_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-panels-backward_locked:

      .. rst-class:: ansible-option-title

      **switch-panels-backward_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-panels-backward_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-panels\-backward' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-panels_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-panels_locked:

      .. rst-class:: ansible-option-title

      **switch-panels_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-panels_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-panels' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-1"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-1:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-1**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-1" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace 1

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>Home']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-10"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-10:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-10**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-10" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace 10

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-10_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-10_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-10_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-10_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-10' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-11"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-11:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-11**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-11" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace 11

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-11_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-11_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-11_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-11_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-11' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-12"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-12:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-12**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-12" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace 12

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-12_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-12_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-12_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-12_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-12' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-1_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-1_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-1_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-1_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-1' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-2"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-2:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-2**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-2" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace 2

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-2_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-2_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-2_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-2_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-2' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-3"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-3:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-3**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-3" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace 3

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-3_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-3_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-3_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-3_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-3' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-4"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-4:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-4**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-4" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace 4

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-4_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-4_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-4_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-4_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-4' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-5"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-5:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-5**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-5" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace 5

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-5_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-5_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-5_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-5_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-5' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-6"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-6:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-6**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-6" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace 6

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-6_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-6_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-6_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-6_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-6' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-7"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-7:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-7**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-7" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace 7

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-7_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-7_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-7_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-7_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-7' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-8"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-8:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-8**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-8" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace 8

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-8_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-8_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-8_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-8_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-8' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-9"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-9:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-9**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-9" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace 9

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-9_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-9_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-9_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-9_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-9' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-down"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-down:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-down**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-down" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace below

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Control\>\<Alt\>Down']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-down_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-down_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-down_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-down_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-down' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-last"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-last:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-last**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-last" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to last workspace

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>End']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-last_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-last_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-last_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-last_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-last' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-left"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-left:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-left**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-left" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace left

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>Page\_Up','\<Super\>\<Alt\>Left','\<Control\>\<Alt\>Left']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-left_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-left_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-left_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-left_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-left' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-right"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-right:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-right**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-right" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace right

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>Page\_Down','\<Super\>\<Alt\>Right','\<Control\>\<Alt\>Right']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-right_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-right_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-right_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-right_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-right' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-up"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-up:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-up**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-up" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch to workspace above

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Control\>\<Alt\>Up']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-to-workspace-up_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-to-workspace-up_locked:

      .. rst-class:: ansible-option-title

      **switch-to-workspace-up_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-to-workspace-up_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-to\-workspace\-up' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-windows"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-windows:

      .. rst-class:: ansible-option-title

      **switch-windows**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-windows" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Switch windows

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-windows-backward"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-windows-backward:

      .. rst-class:: ansible-option-title

      **switch-windows-backward**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-windows-backward" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Reverse switch windows

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-windows-backward_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-windows-backward_locked:

      .. rst-class:: ansible-option-title

      **switch-windows-backward_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-windows-backward_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-windows\-backward' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-switch-windows_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-switch-windows_locked:

      .. rst-class:: ansible-option-title

      **switch-windows_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-switch-windows_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'switch\-windows' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toggle-above"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-toggle-above:

      .. rst-class:: ansible-option-title

      **toggle-above**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toggle-above" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Toggle window always appearing on top

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toggle-above_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-toggle-above_locked:

      .. rst-class:: ansible-option-title

      **toggle-above_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toggle-above_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'toggle\-above' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toggle-fullscreen"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-toggle-fullscreen:

      .. rst-class:: ansible-option-title

      **toggle-fullscreen**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toggle-fullscreen" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Toggle fullscreen mode

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toggle-fullscreen_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-toggle-fullscreen_locked:

      .. rst-class:: ansible-option-title

      **toggle-fullscreen_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toggle-fullscreen_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'toggle\-fullscreen' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toggle-maximized"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-toggle-maximized:

      .. rst-class:: ansible-option-title

      **toggle-maximized**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toggle-maximized" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Toggle maximization state

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Alt\>F10']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toggle-maximized_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-toggle-maximized_locked:

      .. rst-class:: ansible-option-title

      **toggle-maximized_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toggle-maximized_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'toggle\-maximized' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toggle-on-all-workspaces"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-toggle-on-all-workspaces:

      .. rst-class:: ansible-option-title

      **toggle-on-all-workspaces**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toggle-on-all-workspaces" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Toggle window on all workspaces or one

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toggle-on-all-workspaces_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-toggle-on-all-workspaces_locked:

      .. rst-class:: ansible-option-title

      **toggle-on-all-workspaces_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toggle-on-all-workspaces_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'toggle\-on\-all\-workspaces' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-unmaximize"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-unmaximize:

      .. rst-class:: ansible-option-title

      **unmaximize**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-unmaximize" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Restore window

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"['\<Super\>Down','\<Alt\>F5']"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-unmaximize_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_keybindings_module__parameter-unmaximize_locked:

      .. rst-class:: ansible-option-title

      **unmaximize_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-unmaximize_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'unmaximize' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.desktop.wm.keybindings
      org_gnome_desktop_wm_keybindings:
        switch-to-workspace-1: "['<Super>Home']"
        switch-to-workspace-1_locked: true
        switch-to-workspace-2: []
        switch-to-workspace-2_locked: true



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
