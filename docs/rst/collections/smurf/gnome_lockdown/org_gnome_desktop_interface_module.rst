.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_desktop_interface module -- Manages GNOME GSettings for org.gnome.desktop.interface
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_desktop_interface`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.desktop.interface' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-accent-color"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-accent-color:

      .. rst-class:: ansible-option-title

      **accent-color**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-accent-color" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Accent color

      The preferred accent color for the user interface. Valid values are "blue", "teal", "green", "yellow", "orange", "red", "pink", "purple", "slate".


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"blue"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-accent-color_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-accent-color_locked:

      .. rst-class:: ansible-option-title

      **accent-color_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-accent-color_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'accent\-color' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-avatar-directories"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-avatar-directories:

      .. rst-class:: ansible-option-title

      **avatar-directories**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-avatar-directories" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Directories with avatar faces

      Directories to override the default avatar faces installed by gnome\-control\-center.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-avatar-directories_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-avatar-directories_locked:

      .. rst-class:: ansible-option-title

      **avatar-directories_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-avatar-directories_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'avatar\-directories' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-can-change-accels"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-can-change-accels:

      .. rst-class:: ansible-option-title

      **can-change-accels**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-can-change-accels" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Can Change Accels

      Whether the user can dynamically type a new accelerator when positioned over an active menuitem.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-can-change-accels_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-can-change-accels_locked:

      .. rst-class:: ansible-option-title

      **can-change-accels_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-can-change-accels_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'can\-change\-accels' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clock-format"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-clock-format:

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

      Whether the clock displays in 24h or 12h format

      Whether the clock displays in 24h or 12h format


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"24h"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clock-format_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-clock-format_locked:

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
        <div class="ansibleOptionAnchor" id="parameter-clock-show-date"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-clock-show-date:

      .. rst-class:: ansible-option-title

      **clock-show-date**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clock-show-date" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show date in clock

      If true, display date in the clock, in addition to time.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clock-show-date_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-clock-show-date_locked:

      .. rst-class:: ansible-option-title

      **clock-show-date_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clock-show-date_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'clock\-show\-date' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clock-show-seconds"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-clock-show-seconds:

      .. rst-class:: ansible-option-title

      **clock-show-seconds**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clock-show-seconds" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether the clock shows seconds

      If true, display seconds in the clock.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clock-show-seconds_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-clock-show-seconds_locked:

      .. rst-class:: ansible-option-title

      **clock-show-seconds_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clock-show-seconds_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'clock\-show\-seconds' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clock-show-weekday"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-clock-show-weekday:

      .. rst-class:: ansible-option-title

      **clock-show-weekday**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clock-show-weekday" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show weekday in clock

      If true, display weekday in the clock, in addition to time.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clock-show-weekday_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-clock-show-weekday_locked:

      .. rst-class:: ansible-option-title

      **clock-show-weekday_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clock-show-weekday_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'clock\-show\-weekday' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-color-scheme"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-color-scheme:

      .. rst-class:: ansible-option-title

      **color-scheme**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-color-scheme" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Color scheme

      The preferred color scheme for the user interface. Valid values are “default”, “prefer\-dark”, “prefer\-light”.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"default"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-color-scheme_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-color-scheme_locked:

      .. rst-class:: ansible-option-title

      **color-scheme_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-color-scheme_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'color\-scheme' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cursor-blink"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-cursor-blink:

      .. rst-class:: ansible-option-title

      **cursor-blink**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cursor-blink" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cursor Blink

      Whether the cursor should blink.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cursor-blink-time"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-cursor-blink-time:

      .. rst-class:: ansible-option-title

      **cursor-blink-time**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cursor-blink-time" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cursor Blink Time

      Length of the cursor blink cycle, in milliseconds.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1200`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cursor-blink-time_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-cursor-blink-time_locked:

      .. rst-class:: ansible-option-title

      **cursor-blink-time_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cursor-blink-time_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'cursor\-blink\-time' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cursor-blink-timeout"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-cursor-blink-timeout:

      .. rst-class:: ansible-option-title

      **cursor-blink-timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cursor-blink-timeout" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cursor Blink Timeout

      Time after which the cursor stops blinking, in seconds.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`10`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cursor-blink-timeout_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-cursor-blink-timeout_locked:

      .. rst-class:: ansible-option-title

      **cursor-blink-timeout_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cursor-blink-timeout_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'cursor\-blink\-timeout' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cursor-blink_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-cursor-blink_locked:

      .. rst-class:: ansible-option-title

      **cursor-blink_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cursor-blink_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'cursor\-blink' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cursor-size"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-cursor-size:

      .. rst-class:: ansible-option-title

      **cursor-size**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cursor-size" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cursor size

      Size of the cursor used as cursor theme.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`24`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cursor-size_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-cursor-size_locked:

      .. rst-class:: ansible-option-title

      **cursor-size_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cursor-size_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'cursor\-size' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cursor-theme"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-cursor-theme:

      .. rst-class:: ansible-option-title

      **cursor-theme**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cursor-theme" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cursor theme

      Cursor theme name. Used only by Xservers that support the Xcursor extension.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Adwaita"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cursor-theme_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-cursor-theme_locked:

      .. rst-class:: ansible-option-title

      **cursor-theme_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cursor-theme_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'cursor\-theme' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-document-font-name"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-document-font-name:

      .. rst-class:: ansible-option-title

      **document-font-name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-document-font-name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Document font

      Name of the default font used for reading documents.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Adwaita Sans 11"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-document-font-name_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-document-font-name_locked:

      .. rst-class:: ansible-option-title

      **document-font-name_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-document-font-name_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'document\-font\-name' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable-animations"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-enable-animations:

      .. rst-class:: ansible-option-title

      **enable-animations**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-animations" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable Animations

      Whether animations should be displayed. Note: This is a global key, it changes the behaviour of the window manager, the panel etc.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable-animations_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-enable-animations_locked:

      .. rst-class:: ansible-option-title

      **enable-animations_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-animations_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'enable\-animations' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable-hot-corners"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-enable-hot-corners:

      .. rst-class:: ansible-option-title

      **enable-hot-corners**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-hot-corners" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable hot corners

      If true, the activities overview can be accessed by moving the mouse to the top\-left corner.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable-hot-corners_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-enable-hot-corners_locked:

      .. rst-class:: ansible-option-title

      **enable-hot-corners_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-hot-corners_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'enable\-hot\-corners' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-font-antialiasing"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-font-antialiasing:

      .. rst-class:: ansible-option-title

      **font-antialiasing**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-font-antialiasing" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Antialiasing

      The type of antialiasing to use when rendering fonts. Possible values are: “none” for no antialiasing, “grayscale” for standard grayscale antialiasing, and “rgba” for subpixel antialiasing (LCD screens only).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"grayscale"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-font-antialiasing_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-font-antialiasing_locked:

      .. rst-class:: ansible-option-title

      **font-antialiasing_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-font-antialiasing_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'font\-antialiasing' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-font-hinting"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-font-hinting:

      .. rst-class:: ansible-option-title

      **font-hinting**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-font-hinting" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Hinting

      The type of hinting to use when rendering fonts. Possible values are: “none” for no hinting and “slight” for fitting only to the Y\-axis like Microsoft’s ClearType, DirectWrite and Adobe’s proprietary font rendering engine. Ignores native hinting within the font, generates hints algorithmically. Used on Ubuntu by default. Recommended. The meaning of “medium” and “full” depends on the font format (.ttf, .otf, .pfa/.pfb) and the installed version of FreeType. They usually try to fit glyphs to both the X and the Y axis (except for .otf: Y\-only). This can lead to distortion and/or inconsistent rendering depending on the quality of the font, the font format and the state of FreeType’s font engines.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"slight"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-font-hinting_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-font-hinting_locked:

      .. rst-class:: ansible-option-title

      **font-hinting_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-font-hinting_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'font\-hinting' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-font-name"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-font-name:

      .. rst-class:: ansible-option-title

      **font-name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-font-name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Default font

      Name of the default font used by gtk+.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Adwaita Sans 11"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-font-name_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-font-name_locked:

      .. rst-class:: ansible-option-title

      **font-name_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-font-name_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'font\-name' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-font-rendering"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-font-rendering:

      .. rst-class:: ansible-option-title

      **font-rendering**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-font-rendering" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Font rendering

      Preference to indicate whether font rendering should follow the low\-level \`font\-hinting\` and \`font\-antialiasing\` and \`font\-rgba\-order\` settings, or take environmental factors such as screen resolution and scaling into account. Possible values are: "manual" for respecting the low\-level settings, or "automatic" for letting the toolkit make its own decisions.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"automatic"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-font-rendering_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-font-rendering_locked:

      .. rst-class:: ansible-option-title

      **font-rendering_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-font-rendering_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'font\-rendering' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-font-rgba-order"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-font-rgba-order:

      .. rst-class:: ansible-option-title

      **font-rgba-order**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-font-rgba-order" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      RGBA order

      The order of subpixel elements on an LCD screen; only used when antialiasing is set to “rgba”. Possible values are: “rgb” for red on left (most common), “bgr” for blue on left, “vrgb” for red on top, “vbgr” for red on bottom.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"rgb"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-font-rgba-order_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-font-rgba-order_locked:

      .. rst-class:: ansible-option-title

      **font-rgba-order_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-font-rgba-order_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'font\-rgba\-order' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-color-palette"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-color-palette:

      .. rst-class:: ansible-option-title

      **gtk-color-palette**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-color-palette" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Palette used in the color selector

      Palette used in the color selector as defined by the “gtk\-color\-palette” setting


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"black:white:gray50:red:purple:blue:light blue:green:yellow:orange:lavender:brown:goldenrod4:dodger blue:pink:light green:gray10:gray30:gray75:gray90"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-color-palette_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-color-palette_locked:

      .. rst-class:: ansible-option-title

      **gtk-color-palette_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-color-palette_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'gtk\-color\-palette' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-color-scheme"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-color-scheme:

      .. rst-class:: ansible-option-title

      **gtk-color-scheme**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-color-scheme" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of symbolic names and color equivalents

      A “\\n” separated list of “name:color” as defined by the “gtk\-color\-scheme” setting


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-color-scheme_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-color-scheme_locked:

      .. rst-class:: ansible-option-title

      **gtk-color-scheme_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-color-scheme_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'gtk\-color\-scheme' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-enable-primary-paste"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-enable-primary-paste:

      .. rst-class:: ansible-option-title

      **gtk-enable-primary-paste**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-enable-primary-paste" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable the primary paste selection

      If true, gtk+ uses the primary paste selection, usually triggered by a middle mouse button click.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-enable-primary-paste_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-enable-primary-paste_locked:

      .. rst-class:: ansible-option-title

      **gtk-enable-primary-paste_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-enable-primary-paste_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'gtk\-enable\-primary\-paste' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-im-module"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-im-module:

      .. rst-class:: ansible-option-title

      **gtk-im-module**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-im-module" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      GTK IM Module

      Name of the input method module used by GTK+.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-im-module_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-im-module_locked:

      .. rst-class:: ansible-option-title

      **gtk-im-module_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-im-module_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'gtk\-im\-module' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-im-preedit-style"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-im-preedit-style:

      .. rst-class:: ansible-option-title

      **gtk-im-preedit-style**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-im-preedit-style" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      GTK IM Preedit Style

      Name of the GTK+ input method Preedit Style used by gtk+.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"callback"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-im-preedit-style_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-im-preedit-style_locked:

      .. rst-class:: ansible-option-title

      **gtk-im-preedit-style_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-im-preedit-style_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'gtk\-im\-preedit\-style' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-im-status-style"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-im-status-style:

      .. rst-class:: ansible-option-title

      **gtk-im-status-style**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-im-status-style" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      GTK IM Status Style

      Name of the GTK+ input method Status Style used by gtk+.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"callback"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-im-status-style_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-im-status-style_locked:

      .. rst-class:: ansible-option-title

      **gtk-im-status-style_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-im-status-style_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'gtk\-im\-status\-style' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-key-theme"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-key-theme:

      .. rst-class:: ansible-option-title

      **gtk-key-theme**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-key-theme" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Gtk+ Keybinding Theme

      Basename of the default keybinding theme used by gtk+.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Default"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-key-theme_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-key-theme_locked:

      .. rst-class:: ansible-option-title

      **gtk-key-theme_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-key-theme_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'gtk\-key\-theme' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-theme"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-theme:

      .. rst-class:: ansible-option-title

      **gtk-theme**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-theme" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Gtk+ Theme

      Basename of the default theme used by gtk+.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Adwaita"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-theme_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-theme_locked:

      .. rst-class:: ansible-option-title

      **gtk-theme_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-theme_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'gtk\-theme' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-timeout-initial"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-timeout-initial:

      .. rst-class:: ansible-option-title

      **gtk-timeout-initial**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-timeout-initial" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Timeout before click repeat

      Timeout in milliseconds before a click starts repeating (on spinner buttons for example).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`200`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-timeout-initial_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-timeout-initial_locked:

      .. rst-class:: ansible-option-title

      **gtk-timeout-initial_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-timeout-initial_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'gtk\-timeout\-initial' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-timeout-repeat"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-timeout-repeat:

      .. rst-class:: ansible-option-title

      **gtk-timeout-repeat**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-timeout-repeat" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Timeout between click repeats

      Timeout in milliseconds between repeated clicks when a button is left pressed.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`20`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gtk-timeout-repeat_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-gtk-timeout-repeat_locked:

      .. rst-class:: ansible-option-title

      **gtk-timeout-repeat_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gtk-timeout-repeat_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'gtk\-timeout\-repeat' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-theme"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-icon-theme:

      .. rst-class:: ansible-option-title

      **icon-theme**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-theme" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Icon Theme

      Icon theme to use for the panel, nautilus etc.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Adwaita"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icon-theme_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-icon-theme_locked:

      .. rst-class:: ansible-option-title

      **icon-theme_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icon-theme_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'icon\-theme' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-locate-pointer"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-locate-pointer:

      .. rst-class:: ansible-option-title

      **locate-pointer**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-locate-pointer" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Highlights the current location of the pointer.

      If true, pressing a key will highlight the current pointer location on screen.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-locate-pointer_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-locate-pointer_locked:

      .. rst-class:: ansible-option-title

      **locate-pointer_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-locate-pointer_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'locate\-pointer' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-menubar-accel"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-menubar-accel:

      .. rst-class:: ansible-option-title

      **menubar-accel**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-menubar-accel" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Menubar accelerator

      Keyboard shortcut to open the menu bars.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"F10"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-menubar-accel_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-menubar-accel_locked:

      .. rst-class:: ansible-option-title

      **menubar-accel_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-menubar-accel_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'menubar\-accel' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-menubar-detachable"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-menubar-detachable:

      .. rst-class:: ansible-option-title

      **menubar-detachable**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-menubar-detachable" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Menubar Detachable

      Whether the user can detach menubars and move them around.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-menubar-detachable_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-menubar-detachable_locked:

      .. rst-class:: ansible-option-title

      **menubar-detachable_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-menubar-detachable_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'menubar\-detachable' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-menus-have-tearoff"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-menus-have-tearoff:

      .. rst-class:: ansible-option-title

      **menus-have-tearoff**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-menus-have-tearoff" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Menus Have Tearoff

      Whether menus should have a tearoff.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-menus-have-tearoff_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-menus-have-tearoff_locked:

      .. rst-class:: ansible-option-title

      **menus-have-tearoff_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-menus-have-tearoff_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'menus\-have\-tearoff' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-monospace-font-name"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-monospace-font-name:

      .. rst-class:: ansible-option-title

      **monospace-font-name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-monospace-font-name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Monospace font

      Name of a monospaced (fixed\-width) font for use in locations like terminals.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Adwaita Mono 11"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-monospace-font-name_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-monospace-font-name_locked:

      .. rst-class:: ansible-option-title

      **monospace-font-name_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-monospace-font-name_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'monospace\-font\-name' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-overlay-scrolling"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-overlay-scrolling:

      .. rst-class:: ansible-option-title

      **overlay-scrolling**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-overlay-scrolling" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow overlay scrolling

      Whether scrollbars should be overlayed as indicators. Depending on input devices in use, permanent scrollbars may still be displayed.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-overlay-scrolling_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-overlay-scrolling_locked:

      .. rst-class:: ansible-option-title

      **overlay-scrolling_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-overlay-scrolling_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'overlay\-scrolling' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-scaling-factor"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-scaling-factor:

      .. rst-class:: ansible-option-title

      **scaling-factor**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-scaling-factor" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Window scaling factor

      Integer factor used to scale windows by. For use on high\-dpi screens. 0 means pick automatically based on monitor.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"0"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-scaling-factor_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-scaling-factor_locked:

      .. rst-class:: ansible-option-title

      **scaling-factor_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-scaling-factor_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'scaling\-factor' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-battery-percentage"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-show-battery-percentage:

      .. rst-class:: ansible-option-title

      **show-battery-percentage**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-battery-percentage" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show battery percentage

      If true, display battery percentage in the status menu, in addition to the icon.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-battery-percentage_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-show-battery-percentage_locked:

      .. rst-class:: ansible-option-title

      **show-battery-percentage_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-battery-percentage_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-battery\-percentage' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-text-scaling-factor"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-text-scaling-factor:

      .. rst-class:: ansible-option-title

      **text-scaling-factor**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-text-scaling-factor" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Text scaling factor

      Factor used to enlarge or reduce text display, without changing font size.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"1.0"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-text-scaling-factor_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-text-scaling-factor_locked:

      .. rst-class:: ansible-option-title

      **text-scaling-factor_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-text-scaling-factor_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'text\-scaling\-factor' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toolbar-detachable"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-toolbar-detachable:

      .. rst-class:: ansible-option-title

      **toolbar-detachable**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toolbar-detachable" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Toolbar Detachable

      Whether the user can detach toolbars and move them around.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toolbar-detachable_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-toolbar-detachable_locked:

      .. rst-class:: ansible-option-title

      **toolbar-detachable_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toolbar-detachable_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'toolbar\-detachable' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toolbar-icons-size"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-toolbar-icons-size:

      .. rst-class:: ansible-option-title

      **toolbar-icons-size**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toolbar-icons-size" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Toolbar Icon Size

      Size of icons in toolbars, either “small” or “large”.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"large"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toolbar-icons-size_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-toolbar-icons-size_locked:

      .. rst-class:: ansible-option-title

      **toolbar-icons-size_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toolbar-icons-size_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'toolbar\-icons\-size' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toolbar-style"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-toolbar-style:

      .. rst-class:: ansible-option-title

      **toolbar-style**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toolbar-style" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Toolbar Style

      Toolbar Style. Valid values are “both”, “both\-horiz”, “icons”, and “text”.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"both\-horiz"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toolbar-style_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-toolbar-style_locked:

      .. rst-class:: ansible-option-title

      **toolbar-style_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toolbar-style_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'toolbar\-style' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toolkit-accessibility"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-toolkit-accessibility:

      .. rst-class:: ansible-option-title

      **toolkit-accessibility**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toolkit-accessibility" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable Toolkit Accessibility

      Whether toolkits should load accessibility related modules.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toolkit-accessibility_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_interface_module__parameter-toolkit-accessibility_locked:

      .. rst-class:: ansible-option-title

      **toolkit-accessibility_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toolkit-accessibility_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'toolkit\-accessibility' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.desktop.interface
      org_gnome_desktop_interface:
        toolkit-accessibility: false
        toolkit-accessibility_locked: true
        enable-animations: true
        enable-animations_locked: true



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
