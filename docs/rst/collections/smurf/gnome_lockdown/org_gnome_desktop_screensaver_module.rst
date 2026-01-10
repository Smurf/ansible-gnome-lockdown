.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_desktop_screensaver module -- Manages GNOME GSettings for org.gnome.desktop.screensaver
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_desktop_screensaver`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.desktop.screensaver' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-color-shading-type"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-color-shading-type:

      .. rst-class:: ansible-option-title

      **color-shading-type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-color-shading-type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Color Shading Type

      How to shade the background color. Possible values are “horizontal”, “vertical”, and “solid”.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"solid"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-color-shading-type_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-color-shading-type_locked:

      .. rst-class:: ansible-option-title

      **color-shading-type_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-color-shading-type_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'color\-shading\-type' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-embedded-keyboard-command"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-embedded-keyboard-command:

      .. rst-class:: ansible-option-title

      **embedded-keyboard-command**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-embedded-keyboard-command" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Embedded keyboard command

      The command that will be run, if the “embedded\_keyboard\_enabled” key is set to TRUE, to embed a keyboard widget into the window. This command should implement an XEMBED plug interface and output a window XID on the standard output. DEPRECATED: This key is deprecated and ignored.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-embedded-keyboard-command_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-embedded-keyboard-command_locked:

      .. rst-class:: ansible-option-title

      **embedded-keyboard-command_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-embedded-keyboard-command_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'embedded\-keyboard\-command' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-embedded-keyboard-enabled"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-embedded-keyboard-enabled:

      .. rst-class:: ansible-option-title

      **embedded-keyboard-enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-embedded-keyboard-enabled" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow embedding a keyboard into the window

      Set this to TRUE to allow embedding a keyboard into the window when trying to unlock. The “keyboard\_command” key must be set with the appropriate command. DEPRECATED: This key is deprecated and ignored.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-embedded-keyboard-enabled_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-embedded-keyboard-enabled_locked:

      .. rst-class:: ansible-option-title

      **embedded-keyboard-enabled_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-embedded-keyboard-enabled_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'embedded\-keyboard\-enabled' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-idle-activation-enabled"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-idle-activation-enabled:

      .. rst-class:: ansible-option-title

      **idle-activation-enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-idle-activation-enabled" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Activate when idle

      Set this to TRUE to activate the screensaver when the session is idle. DEPRECATED: This key is deprecated and ignored. Set org.gnome.desktop.session idle\-delay to 0 if you do not want to activate the screensaver.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-idle-activation-enabled_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-idle-activation-enabled_locked:

      .. rst-class:: ansible-option-title

      **idle-activation-enabled_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-idle-activation-enabled_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'idle\-activation\-enabled' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lock-delay"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-lock-delay:

      .. rst-class:: ansible-option-title

      **lock-delay**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lock-delay" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Time before locking

      The number of seconds after screensaver activation before locking the screen.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"0"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lock-delay_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-lock-delay_locked:

      .. rst-class:: ansible-option-title

      **lock-delay_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lock-delay_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'lock\-delay' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lock-enabled"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-lock-enabled:

      .. rst-class:: ansible-option-title

      **lock-enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lock-enabled" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Lock on activation

      Set this to TRUE to lock the screen when the screensaver goes active.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lock-enabled_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-lock-enabled_locked:

      .. rst-class:: ansible-option-title

      **lock-enabled_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lock-enabled_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'lock\-enabled' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-logout-command"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-logout-command:

      .. rst-class:: ansible-option-title

      **logout-command**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logout-command" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Logout command

      The command to invoke when the logout button is clicked. This command should simply log the user out without any interaction. This key has effect only if the “logout\_enable” key is set to TRUE. DEPRECATED: This key is deprecated and ignored.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-logout-command_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-logout-command_locked:

      .. rst-class:: ansible-option-title

      **logout-command_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logout-command_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'logout\-command' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-logout-delay"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-logout-delay:

      .. rst-class:: ansible-option-title

      **logout-delay**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logout-delay" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Time before logout option

      The number of seconds after the screensaver activation before a logout option will appear in the unlock dialog. This key has effect only if the “logout\_enable” key is set to TRUE. DEPRECATED: This key is deprecated and ignored


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"7200"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-logout-delay_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-logout-delay_locked:

      .. rst-class:: ansible-option-title

      **logout-delay_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logout-delay_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'logout\-delay' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-logout-enabled"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-logout-enabled:

      .. rst-class:: ansible-option-title

      **logout-enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logout-enabled" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow logout

      Set this to TRUE to offer an option in the unlock dialog to allow logging out after a delay. The delay is specified in the “logout\_delay” key. DEPRECATED: This key is deprecated and ignored.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-logout-enabled_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-logout-enabled_locked:

      .. rst-class:: ansible-option-title

      **logout-enabled_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logout-enabled_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'logout\-enabled' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-opacity"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-picture-opacity:

      .. rst-class:: ansible-option-title

      **picture-opacity**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-opacity" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Picture Opacity

      Opacity with which to draw the background picture.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`100`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-opacity_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-picture-opacity_locked:

      .. rst-class:: ansible-option-title

      **picture-opacity_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-opacity_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'picture\-opacity' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-options"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-picture-options:

      .. rst-class:: ansible-option-title

      **picture-options**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-options" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Picture Options

      Determines how the image set by wallpaper\_filename is rendered. Possible values are “none”, “wallpaper”, “centered”, “scaled”, “stretched”, “zoom”, “spanned”.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"zoom"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-options_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-picture-options_locked:

      .. rst-class:: ansible-option-title

      **picture-options_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-options_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'picture\-options' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-uri"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-picture-uri:

      .. rst-class:: ansible-option-title

      **picture-uri**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-uri" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Picture URI

      URI to use for the background image. Note that the backend only supports local (file://) URIs.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"file:///usr/share/backgrounds/gnome/adwaita\-timed.xml"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-picture-uri_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-picture-uri_locked:

      .. rst-class:: ansible-option-title

      **picture-uri_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-picture-uri_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'picture\-uri' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-primary-color"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-primary-color:

      .. rst-class:: ansible-option-title

      **primary-color**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-primary-color" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Primary Color

      Left or Top color when drawing gradients, or the solid color.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"#023c88"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-primary-color_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-primary-color_locked:

      .. rst-class:: ansible-option-title

      **primary-color_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-primary-color_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'primary\-color' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-secondary-color"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-secondary-color:

      .. rst-class:: ansible-option-title

      **secondary-color**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-secondary-color" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Secondary Color

      Right or Bottom color when drawing gradients, not used for solid color.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"#5789ca"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-secondary-color_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-secondary-color_locked:

      .. rst-class:: ansible-option-title

      **secondary-color_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-secondary-color_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'secondary\-color' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-full-name-in-top-bar"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-show-full-name-in-top-bar:

      .. rst-class:: ansible-option-title

      **show-full-name-in-top-bar**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-full-name-in-top-bar" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show full name in the lock screen

      Whether the user’s full name is shown in the lock screen or not. This only affects the screen shield, the name is always shown in the unlock dialog.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-full-name-in-top-bar_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-show-full-name-in-top-bar_locked:

      .. rst-class:: ansible-option-title

      **show-full-name-in-top-bar_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-full-name-in-top-bar_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-full\-name\-in\-top\-bar' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-status-message-enabled"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-status-message-enabled:

      .. rst-class:: ansible-option-title

      **status-message-enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-status-message-enabled" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow the session status message to be displayed

      Allow the session status message to be displayed when the screen is locked. DEPRECATED: This key is deprecated and ignored.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-status-message-enabled_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-status-message-enabled_locked:

      .. rst-class:: ansible-option-title

      **status-message-enabled_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-status-message-enabled_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'status\-message\-enabled' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-user-switch-enabled"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-user-switch-enabled:

      .. rst-class:: ansible-option-title

      **user-switch-enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-user-switch-enabled" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow user switching

      Set this to TRUE to offer an option in the unlock dialog to switch to a different user account.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-user-switch-enabled_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_screensaver_module__parameter-user-switch-enabled_locked:

      .. rst-class:: ansible-option-title

      **user-switch-enabled_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-user-switch-enabled_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'user\-switch\-enabled' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.desktop.screensaver
      org_gnome_desktop_screensaver:
        idle-activation-enabled: true
        idle-activation-enabled_locked: true
        lock-enabled: true
        lock-enabled_locked: true



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
