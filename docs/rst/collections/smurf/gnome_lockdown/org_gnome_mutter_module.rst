.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_mutter module -- Manages GNOME GSettings for org.gnome.mutter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_mutter`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.mutter' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-attach-modal-dialogs"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-attach-modal-dialogs:

      .. rst-class:: ansible-option-title

      **attach-modal-dialogs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attach-modal-dialogs" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Attach modal dialogs

      When true, instead of having independent titlebars, modal dialogs appear attached to the titlebar of the parent window and are moved together with the parent window.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attach-modal-dialogs_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-attach-modal-dialogs_locked:

      .. rst-class:: ansible-option-title

      **attach-modal-dialogs_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attach-modal-dialogs_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'attach\-modal\-dialogs' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-maximize"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-auto-maximize:

      .. rst-class:: ansible-option-title

      **auto-maximize**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-maximize" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Auto maximize nearly monitor sized windows

      If enabled, new windows that are initially the size of the monitor automatically get maximized.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-maximize_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-auto-maximize_locked:

      .. rst-class:: ansible-option-title

      **auto-maximize_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-maximize_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'auto\-maximize' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-center-new-windows"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-center-new-windows:

      .. rst-class:: ansible-option-title

      **center-new-windows**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-center-new-windows" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Place new windows in the center

      When true, the new windows will always be put in the center of the active screen of the monitor.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-center-new-windows_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-center-new-windows_locked:

      .. rst-class:: ansible-option-title

      **center-new-windows_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-center-new-windows_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'center\-new\-windows' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-check-alive-timeout"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-check-alive-timeout:

      .. rst-class:: ansible-option-title

      **check-alive-timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-check-alive-timeout" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Timeout for check\-alive ping

      Number of milliseconds a client has to respond to a ping request in order to not be detected as frozen. Using 0 will disable the alive check completely.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"5000"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-check-alive-timeout_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-check-alive-timeout_locked:

      .. rst-class:: ansible-option-title

      **check-alive-timeout_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-check-alive-timeout_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'check\-alive\-timeout' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-draggable-border-width"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-draggable-border-width:

      .. rst-class:: ansible-option-title

      **draggable-border-width**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-draggable-border-width" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Draggable border width

      The amount of total draggable borders. If the theme’s visible borders are not enough, invisible borders will be added to meet this value.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`10`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-draggable-border-width_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-draggable-border-width_locked:

      .. rst-class:: ansible-option-title

      **draggable-border-width_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-draggable-border-width_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'draggable\-border\-width' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dynamic-workspaces"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-dynamic-workspaces:

      .. rst-class:: ansible-option-title

      **dynamic-workspaces**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dynamic-workspaces" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Workspaces are managed dynamically

      Determines whether workspaces are managed dynamically or whether there’s a static number of workspaces (determined by the num\-workspaces key in org.gnome.desktop.wm.preferences).


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dynamic-workspaces_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-dynamic-workspaces_locked:

      .. rst-class:: ansible-option-title

      **dynamic-workspaces_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dynamic-workspaces_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'dynamic\-workspaces' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-edge-tiling"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-edge-tiling:

      .. rst-class:: ansible-option-title

      **edge-tiling**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-edge-tiling" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable edge tiling when dropping windows on screen edges

      If enabled, dropping windows on vertical screen edges maximizes them vertically and resizes them horizontally to cover half of the available area. Dropping windows on the top screen edge maximizes them completely.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-edge-tiling_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-edge-tiling_locked:

      .. rst-class:: ansible-option-title

      **edge-tiling_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-edge-tiling_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'edge\-tiling' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-experimental-features"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-experimental-features:

      .. rst-class:: ansible-option-title

      **experimental-features**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-experimental-features" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable experimental features

      To enable experimental features, add the feature keyword to the list. Whether the feature requires restarting the compositor depends on the given feature. Any experimental feature is not required to still be available, or configurable. Don’t expect adding anything in this setting to be future proof. Currently possible keywords: • “scale\-monitor\-framebuffer” — makes mutter default to layout logical monitors in a logical pixel coordinate space, while scaling monitor framebuffers instead of window content, to manage HiDPI monitors. Does not require a restart. • “kms\-modifiers” — makes mutter always allocate scanout buffers with explicit modifiers, if supported by the driver. Requires a restart. • “autoclose\-xwayland” — automatically terminates Xwayland if all relevant X11 clients are gone. Requires a restart. • “variable\-refresh\-rate” — makes mutter dynamically adjust the refresh rate of the monitor when applicable if supported by the monitor, GPU and DRM driver. Configurable in Settings. Requires a restart. • “xwayland\-native\-scaling” — lets Xwayland clients use their native scaling support. If scaling is not supported by client, the client will be unscaled. Setting only takes effect when “scale\-monitor\-framebuffer” is enabled as well.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-experimental-features_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-experimental-features_locked:

      .. rst-class:: ansible-option-title

      **experimental-features_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-experimental-features_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'experimental\-features' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-focus-change-on-pointer-rest"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-focus-change-on-pointer-rest:

      .. rst-class:: ansible-option-title

      **focus-change-on-pointer-rest**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-focus-change-on-pointer-rest" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Delay focus changes until the pointer stops moving

      If set to true, and the focus mode is either “sloppy” or “mouse” then the focus will not be changed immediately when entering a window, but only after the pointer stops moving.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-focus-change-on-pointer-rest_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-focus-change-on-pointer-rest_locked:

      .. rst-class:: ansible-option-title

      **focus-change-on-pointer-rest_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-focus-change-on-pointer-rest_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'focus\-change\-on\-pointer\-rest' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-locate-pointer-key"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-locate-pointer-key:

      .. rst-class:: ansible-option-title

      **locate-pointer-key**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-locate-pointer-key" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Modifier to use to locate the pointer

      This key will initiate the “locate pointer” action.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Control\_L"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-locate-pointer-key_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-locate-pointer-key_locked:

      .. rst-class:: ansible-option-title

      **locate-pointer-key_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-locate-pointer-key_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'locate\-pointer\-key' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-output-luminance"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-output-luminance:

      .. rst-class:: ansible-option-title

      **output-luminance**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-output-luminance" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Per output luminance settings

      Per output and color mode luminance setting. Each entry consists of a tuple with connector, vendor, product, serial, and a color mode, as well as an associated floating point value representing the output luminance in percent (%). The default when not specified is 100%.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-output-luminance_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-output-luminance_locked:

      .. rst-class:: ansible-option-title

      **output-luminance_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-output-luminance_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'output\-luminance' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-overlay-key"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-overlay-key:

      .. rst-class:: ansible-option-title

      **overlay-key**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-overlay-key" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Modifier to use for extended window management operations

      This key will initiate the “overlay”, which is a combination window overview and application launching system. The default is intended to be the “Windows key” on PC hardware. It’s expected that this binding either the default or set to the empty string.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Super"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-overlay-key_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-overlay-key_locked:

      .. rst-class:: ansible-option-title

      **overlay-key_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-overlay-key_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'overlay\-key' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workspaces-only-on-primary"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-workspaces-only-on-primary:

      .. rst-class:: ansible-option-title

      **workspaces-only-on-primary**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workspaces-only-on-primary" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Workspaces only on primary

      Determines whether workspace switching should happen for windows on all monitors or only for windows on the primary monitor.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workspaces-only-on-primary_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_mutter_module__parameter-workspaces-only-on-primary_locked:

      .. rst-class:: ansible-option-title

      **workspaces-only-on-primary_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workspaces-only-on-primary_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'workspaces\-only\-on\-primary' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.mutter
      org_gnome_mutter:
        overlay-key: "Super"
        overlay-key_locked: true
        attach-modal-dialogs: false
        attach-modal-dialogs_locked: true



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
