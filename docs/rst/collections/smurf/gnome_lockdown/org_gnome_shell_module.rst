.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_shell module -- Manages GNOME GSettings for org.gnome.shell
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_shell`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.shell' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-allow-extension-installation"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-allow-extension-installation:

      .. rst-class:: ansible-option-title

      **allow-extension-installation**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-allow-extension-installation" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow extension installation

      Allow users to install extensions in their home folder. If disabled, the InstallRemoteExtension D\-Bus method will fail, and extensions are only loaded from system directories on startup. It does not affect extensions that are already loaded, so a change only takes full effect on the next login.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-allow-extension-installation_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-allow-extension-installation_locked:

      .. rst-class:: ansible-option-title

      **allow-extension-installation_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-allow-extension-installation_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'allow\-extension\-installation' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-always-show-log-out"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-always-show-log-out:

      .. rst-class:: ansible-option-title

      **always-show-log-out**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-always-show-log-out" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Always show the “Log Out” action in the system menu

      This key overrides the automatic hiding of the “Log out” action in the system menu for logged\-in situations where there is a single, local, non\-system user and only a single available session type (e.g. GNOME on Wayland).


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-always-show-log-out_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-always-show-log-out_locked:

      .. rst-class:: ansible-option-title

      **always-show-log-out_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-always-show-log-out_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'always\-show\-log\-out' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-app-picker-layout"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-app-picker-layout:

      .. rst-class:: ansible-option-title

      **app-picker-layout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-app-picker-layout" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Layout of the app picker

      Layout of the app picker. Each entry in the array is a page. Pages are stored in the order they appear in GNOME Shell. Each page contains an “application id” → 'data' pair. Currently, the following values are stored as 'data': • “position”: the position of the application icon in the page


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[{ 'org.gnome.Geary.desktop': \<{'position': \<0\>}\>, 'org.gnome.Contacts.desktop': \<{'position': \<1\>}\>, 'org.gnome.Weather.desktop': \<{'position': \<2\>}\>, 'org.gnome.clocks.desktop': \<{'position': \<3\>}\>, 'org.gnome.Maps.desktop': \<{'position': \<4\>}\>, 'org.gnome.Music.desktop': \<{'position': \<5\>}\>, 'simple\-scan.desktop': \<{'position': \<6\>}\>, 'org.gnome.Settings.desktop': \<{'position': \<7\>}\>, 'org.gnome.Boxes.desktop': \<{'position': \<8\>}\>, 'org.gnome.Totem.desktop': \<{'position': \<9\>}\>, 'org.gnome.Snapshot.desktop': \<{'position': \<10\>}\>, 'org.gnome.Characters.desktop': \<{'position': \<11\>}\>, 'Utilities': \<{'position': \<12\>}\>, 'System': \<{'position': \<13\>}\>, 'org.gnome.Console.desktop': \<{'position': \<14\>}\>, 'org.gnome.Tour.desktop': \<{'position': \<15\>}\>, 'yelp.desktop': \<{'position': \<16\>}\> }]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-app-picker-layout_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-app-picker-layout_locked:

      .. rst-class:: ansible-option-title

      **app-picker-layout_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-app-picker-layout_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'app\-picker\-layout' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-command-history"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-command-history:

      .. rst-class:: ansible-option-title

      **command-history**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-command-history" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      History for command (Alt\-F2) dialog

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-command-history_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-command-history_locked:

      .. rst-class:: ansible-option-title

      **command-history_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-command-history_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'command\-history' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-development-tools"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-development-tools:

      .. rst-class:: ansible-option-title

      **development-tools**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-development-tools" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable internal tools useful for developers and testers from Alt\-F2

      Allows access to internal debugging and monitoring tools using the Alt\-F2 dialog.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-development-tools_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-development-tools_locked:

      .. rst-class:: ansible-option-title

      **development-tools_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-development-tools_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'development\-tools' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-extension-version-validation"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-disable-extension-version-validation:

      .. rst-class:: ansible-option-title

      **disable-extension-version-validation**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-extension-version-validation" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disables the validation of extension version compatibility

      GNOME Shell will only load extensions that claim to support the current running version. Enabling this option will disable this check and try to load all extensions regardless of the versions they claim to support.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-extension-version-validation_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-disable-extension-version-validation_locked:

      .. rst-class:: ansible-option-title

      **disable-extension-version-validation_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-extension-version-validation_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-extension\-version\-validation' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-user-extensions"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-disable-user-extensions:

      .. rst-class:: ansible-option-title

      **disable-user-extensions**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-user-extensions" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable user extensions

      Disable all extensions the user has enabled without affecting the “enabled\-extension” setting.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-user-extensions_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-disable-user-extensions_locked:

      .. rst-class:: ansible-option-title

      **disable-user-extensions_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-user-extensions_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-user\-extensions' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disabled-extensions"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-disabled-extensions:

      .. rst-class:: ansible-option-title

      **disabled-extensions**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disabled-extensions" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      UUIDs of extensions to force disabling

      GNOME Shell extensions have a UUID property; this key lists extensions which should be disabled, even if loaded as part of the current mode. You can also manipulate this list with the EnableExtension and DisableExtension D\-Bus methods on org.gnome.Shell. This key takes precedence over the “enabled\-extensions” setting.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disabled-extensions_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-disabled-extensions_locked:

      .. rst-class:: ansible-option-title

      **disabled-extensions_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disabled-extensions_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disabled\-extensions' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enabled-extensions"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-enabled-extensions:

      .. rst-class:: ansible-option-title

      **enabled-extensions**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enabled-extensions" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      UUIDs of extensions to enable

      GNOME Shell extensions have a UUID property; this key lists extensions which should be loaded. Any extension that wants to be loaded needs to be in this list. You can also manipulate this list with the EnableExtension and DisableExtension D\-Bus methods on org.gnome.Shell.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enabled-extensions_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-enabled-extensions_locked:

      .. rst-class:: ansible-option-title

      **enabled-extensions_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enabled-extensions_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'enabled\-extensions' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-favorite-apps"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-favorite-apps:

      .. rst-class:: ansible-option-title

      **favorite-apps**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-favorite-apps" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of desktop file IDs for favorite applications

      The applications corresponding to these identifiers will be displayed in the favorites area.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[ 'org.mozilla.firefox.desktop', 'org.gnome.Calendar.desktop', 'org.gnome.Nautilus.desktop', 'org.gnome.Software.desktop', 'org.gnome.TextEditor.desktop', 'org.gnome.Calculator.desktop' ]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-favorite-apps_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-favorite-apps_locked:

      .. rst-class:: ansible-option-title

      **favorite-apps_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-favorite-apps_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'favorite\-apps' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-last-selected-power-profile"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-last-selected-power-profile:

      .. rst-class:: ansible-option-title

      **last-selected-power-profile**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-last-selected-power-profile" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The last selected non\-default power profile

      Some systems support more than two power profiles. In order to still support toggling between two profiles, this key records the last selected non\-default profile.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"power\-saver"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-last-selected-power-profile_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-last-selected-power-profile_locked:

      .. rst-class:: ansible-option-title

      **last-selected-power-profile_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-last-selected-power-profile_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'last\-selected\-power\-profile' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-looking-glass-history"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-looking-glass-history:

      .. rst-class:: ansible-option-title

      **looking-glass-history**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-looking-glass-history" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      History for the looking glass dialog

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-looking-glass-history_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-looking-glass-history_locked:

      .. rst-class:: ansible-option-title

      **looking-glass-history_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-looking-glass-history_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'looking\-glass\-history' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-remember-mount-password"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-remember-mount-password:

      .. rst-class:: ansible-option-title

      **remember-mount-password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-remember-mount-password" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to remember password for mounting encrypted or remote filesystems

      The shell will request a password when an encrypted device or a remote filesystem is mounted. If the password can be saved for future use a “Remember Password” checkbox will be present. This key sets the default state of the checkbox.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-remember-mount-password_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-remember-mount-password_locked:

      .. rst-class:: ansible-option-title

      **remember-mount-password_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-remember-mount-password_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'remember\-mount\-password' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-welcome-dialog-last-shown-version"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-welcome-dialog-last-shown-version:

      .. rst-class:: ansible-option-title

      **welcome-dialog-last-shown-version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-welcome-dialog-last-shown-version" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The last version the “Welcome to GNOME” dialog was shown for

      This key determines for which version the “Welcome to GNOME” dialog was last shown. An empty string represents the oldest possible version, and a huge number will represent versions that do not exist yet. This huge number can be used to effectively disable the dialog.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-welcome-dialog-last-shown-version_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_shell_module__parameter-welcome-dialog-last-shown-version_locked:

      .. rst-class:: ansible-option-title

      **welcome-dialog-last-shown-version_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-welcome-dialog-last-shown-version_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'welcome\-dialog\-last\-shown\-version' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.shell
      org_gnome_shell:
        development-tools: true
        development-tools_locked: true
        enabled-extensions: []
        enabled-extensions_locked: true



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
