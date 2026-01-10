.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_desktop_wm_preferences module -- Manages GNOME GSettings for org.gnome.desktop.wm.preferences
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_desktop_wm_preferences`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.desktop.wm.preferences' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-action-double-click-titlebar"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-action-double-click-titlebar:

      .. rst-class:: ansible-option-title

      **action-double-click-titlebar**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-action-double-click-titlebar" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Action on title bar double\-click

      This option determines the effects of double\-clicking on the title bar. Current valid options are “toggle\-maximize” which will maximize/unmaximize the window, “toggle\-maximize\-horizontally” and “toggle\-maximize\-vertically” which will maximize/unmaximize the window in that direction only, “minimize” which will minimize the window, “menu” which will display the window menu, “lower” which will put the window behind all the others, and “none” which will not do anything.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"toggle\-maximize"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-action-double-click-titlebar_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-action-double-click-titlebar_locked:

      .. rst-class:: ansible-option-title

      **action-double-click-titlebar_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-action-double-click-titlebar_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'action\-double\-click\-titlebar' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-action-middle-click-titlebar"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-action-middle-click-titlebar:

      .. rst-class:: ansible-option-title

      **action-middle-click-titlebar**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-action-middle-click-titlebar" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Action on title bar middle\-click

      This option determines the effects of middle\-clicking on the title bar. Current valid options are “toggle\-maximize” which will maximize/unmaximize the window, “toggle\-maximize\-horizontally” and “toggle\-maximize\-vertically” which will maximize/unmaximize the window in that direction only, “minimize” which will minimize the window, “menu” which will display the window menu, “lower” which will put the window behind all the others, and “none” which will not do anything.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-action-middle-click-titlebar_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-action-middle-click-titlebar_locked:

      .. rst-class:: ansible-option-title

      **action-middle-click-titlebar_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-action-middle-click-titlebar_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'action\-middle\-click\-titlebar' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-action-right-click-titlebar"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-action-right-click-titlebar:

      .. rst-class:: ansible-option-title

      **action-right-click-titlebar**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-action-right-click-titlebar" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Action on title bar right\-click

      This option determines the effects of right\-clicking on the title bar. Current valid options are “toggle\-maximize” which will maximize/unmaximize the window, “toggle\-maximize\-horizontally” and “toggle\-maximize\-vertically” which will maximize/unmaximize the window in that direction only, “minimize” which will minimize the window, “menu” which will display the window menu, “lower” which will put the window behind all the others, and “none” which will not do anything.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"menu"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-action-right-click-titlebar_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-action-right-click-titlebar_locked:

      .. rst-class:: ansible-option-title

      **action-right-click-titlebar_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-action-right-click-titlebar_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'action\-right\-click\-titlebar' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-audible-bell"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-audible-bell:

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

      System Bell is Audible

      Determines whether applications or the system can generate audible “beeps”; may be used in conjunction with “visual bell” to allow silent “beeps”.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-audible-bell_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-audible-bell_locked:

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
        <div class="ansibleOptionAnchor" id="parameter-auto-raise"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-auto-raise:

      .. rst-class:: ansible-option-title

      **auto-raise**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-raise" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Automatically raises the focused window

      If set to true, and the focus mode is either “sloppy” or “mouse” then the focused window will be automatically raised after a delay specified by the auto\-raise\-delay key. This is not related to clicking on a window to raise it, nor to entering a window during drag\-and\-drop.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-raise-delay"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-auto-raise-delay:

      .. rst-class:: ansible-option-title

      **auto-raise-delay**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-raise-delay" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Delay in milliseconds for the auto raise option

      The time delay before raising a window if auto\-raise is set to true. The delay is given in thousandths of a second.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`500`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-raise-delay_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-auto-raise-delay_locked:

      .. rst-class:: ansible-option-title

      **auto-raise-delay_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-raise-delay_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'auto\-raise\-delay' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-raise_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-auto-raise_locked:

      .. rst-class:: ansible-option-title

      **auto-raise_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-raise_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'auto\-raise' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-button-layout"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-button-layout:

      .. rst-class:: ansible-option-title

      **button-layout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-button-layout" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Arrangement of buttons on the titlebar

      Arrangement of buttons on the titlebar. The value should be a string, such as “menu:minimize,maximize,spacer,close”; the colon separates the left corner of the window from the right corner, and the button names are comma\-separated. Duplicate buttons are not allowed. Unknown button names are silently ignored so that buttons can be added in future metacity versions without breaking older versions. A special spacer tag can be used to insert some space between two adjacent buttons.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"appmenu:close"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-button-layout_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-button-layout_locked:

      .. rst-class:: ansible-option-title

      **button-layout_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-button-layout_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'button\-layout' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-workarounds"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-disable-workarounds:

      .. rst-class:: ansible-option-title

      **disable-workarounds**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-workarounds" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable misfeatures that are required by old or broken applications

      Some applications disregard specifications in ways that result in window manager misfeatures. This option puts the WM in a rigorously correct mode, which gives a more consistent user interface, provided one does not need to run any misbehaving applications.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-workarounds_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-disable-workarounds_locked:

      .. rst-class:: ansible-option-title

      **disable-workarounds_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-workarounds_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-workarounds' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-focus-mode"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-focus-mode:

      .. rst-class:: ansible-option-title

      **focus-mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-focus-mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Window focus mode

      The window focus mode indicates how windows are activated. It has three possible values; “click” means windows must be clicked in order to focus them, “sloppy” means windows are focused when the mouse enters the window, and “mouse” means windows are focused when the mouse enters the window and unfocused when the mouse leaves the window.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"click"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-focus-mode_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-focus-mode_locked:

      .. rst-class:: ansible-option-title

      **focus-mode_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-focus-mode_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'focus\-mode' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-focus-new-windows"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-focus-new-windows:

      .. rst-class:: ansible-option-title

      **focus-new-windows**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-focus-new-windows" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Control how new windows get focus

      This option provides additional control over how newly created windows get focus. It has two possible values; “smart” applies the user’s normal focus mode, and “strict” results in new windows not being given focus automatically.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"smart"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-focus-new-windows_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-focus-new-windows_locked:

      .. rst-class:: ansible-option-title

      **focus-new-windows_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-focus-new-windows_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'focus\-new\-windows' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mouse-button-modifier"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-mouse-button-modifier:

      .. rst-class:: ansible-option-title

      **mouse-button-modifier**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mouse-button-modifier" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Modifier to use for modified window click actions

      Clicking a window while holding down this modifier key will move the window (left click), resize the window (middle click), or show the window menu (right click). The middle and right click operations may be swapped using the “resize\-with\-right\-button” key. Modifier is expressed as “\<Alt\>” or “\<Super\>” for example.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"\<Super\>"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mouse-button-modifier_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-mouse-button-modifier_locked:

      .. rst-class:: ansible-option-title

      **mouse-button-modifier_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mouse-button-modifier_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'mouse\-button\-modifier' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-num-workspaces"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-num-workspaces:

      .. rst-class:: ansible-option-title

      **num-workspaces**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-num-workspaces" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of workspaces

      Number of workspaces. Must be more than zero, and has a fixed maximum to prevent making the desktop unusable by accidentally asking for too many workspaces.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`4`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-num-workspaces_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-num-workspaces_locked:

      .. rst-class:: ansible-option-title

      **num-workspaces_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-num-workspaces_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'num\-workspaces' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-raise-on-click"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-raise-on-click:

      .. rst-class:: ansible-option-title

      **raise-on-click**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-raise-on-click" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether windows should be raised when their client area is clicked

      The default, true, indicates that a window will be raised whenever its client area or its frame is clicked. Setting this to false means that a window will not be raised if it is clicked on the client area. To raise it, one can click anywhere in the window’s frame, or Super\-click on any part of the window. This mode is useful if one uses many overlapping windows.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-raise-on-click_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-raise-on-click_locked:

      .. rst-class:: ansible-option-title

      **raise-on-click_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-raise-on-click_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'raise\-on\-click' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-resize-with-right-button"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-resize-with-right-button:

      .. rst-class:: ansible-option-title

      **resize-with-right-button**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-resize-with-right-button" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to resize with the right button

      Set this to true to resize with the right button and show a menu with the middle button while holding down the key given in “mouse\-button\-modifier”; set it to false to make it work the opposite way around.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-resize-with-right-button_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-resize-with-right-button_locked:

      .. rst-class:: ansible-option-title

      **resize-with-right-button_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-resize-with-right-button_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'resize\-with\-right\-button' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-theme"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-theme:

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

      Current theme

      The theme determines the appearance of window borders, titlebar, and so forth. DEPRECATED: This key is deprecated and ignored.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Adwaita"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-theme_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-theme_locked:

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
        <div class="ansibleOptionAnchor" id="parameter-titlebar-font"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-titlebar-font:

      .. rst-class:: ansible-option-title

      **titlebar-font**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-titlebar-font" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Window title font

      A font description string describing a font for window titlebars. The size from the description will only be used if the titlebar\-font\-size option is set to 0. Also, this option is disabled if the titlebar\-uses\-desktop\-font option is set to true.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Adwaita Sans Bold 11"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-titlebar-font_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-titlebar-font_locked:

      .. rst-class:: ansible-option-title

      **titlebar-font_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-titlebar-font_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'titlebar\-font' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-titlebar-uses-system-font"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-titlebar-uses-system-font:

      .. rst-class:: ansible-option-title

      **titlebar-uses-system-font**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-titlebar-uses-system-font" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use standard system font in window titles

      If true, ignore the titlebar\-font option, and use the standard application font for window titles.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-titlebar-uses-system-font_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-titlebar-uses-system-font_locked:

      .. rst-class:: ansible-option-title

      **titlebar-uses-system-font_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-titlebar-uses-system-font_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'titlebar\-uses\-system\-font' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-visual-bell"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-visual-bell:

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

      Enable Visual Bell

      Turns on a visual indication when an application or the system issues a “bell” or “beep”; useful for the hard\-of\-hearing and for use in noisy environments.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-visual-bell-type"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-visual-bell-type:

      .. rst-class:: ansible-option-title

      **visual-bell-type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-visual-bell-type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Visual Bell Type

      Tells the WM how to implement the visual indication that the system bell or another application “bell” indicator has been rung. Currently there are two valid values, “fullscreen\-flash”, which causes a fullscreen white\-black flash, and “frame\-flash” which causes the titlebar of the application which sent the bell signal to flash. If the application which sent the bell is unknown (as is usually the case for the default “system beep”), the currently focused window’s titlebar is flashed.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"fullscreen\-flash"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-visual-bell-type_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-visual-bell-type_locked:

      .. rst-class:: ansible-option-title

      **visual-bell-type_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-visual-bell-type_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'visual\-bell\-type' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-visual-bell_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-visual-bell_locked:

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

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workspace-names"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-workspace-names:

      .. rst-class:: ansible-option-title

      **workspace-names**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workspace-names" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The names of the workspaces

      Defines the names that should be assigned to workspaces. If the list is too long for the current number of workspaces, names in excess will be ignored. If the list is too short, or includes empty names, missing values will be replaced with the default (“Workspace N”).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workspace-names_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_wm_preferences_module__parameter-workspace-names_locked:

      .. rst-class:: ansible-option-title

      **workspace-names_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workspace-names_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'workspace\-names' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.desktop.wm.preferences
      org_gnome_desktop_wm_preferences:
        mouse-button-modifier: "<Super>"
        mouse-button-modifier_locked: true
        resize-with-right-button: false
        resize-with-right-button_locked: true



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
