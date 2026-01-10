.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_sound_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_desktop_sound module -- Manages GNOME GSettings for org.gnome.desktop.sound
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_desktop_sound`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.desktop.sound' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-allow-volume-above-100-percent"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_sound_module__parameter-allow-volume-above-100-percent:

      .. rst-class:: ansible-option-title

      **allow-volume-above-100-percent**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-allow-volume-above-100-percent" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow volume above 100%

      Whether volume can be set above 100%, using software amplification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-allow-volume-above-100-percent_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_sound_module__parameter-allow-volume-above-100-percent_locked:

      .. rst-class:: ansible-option-title

      **allow-volume-above-100-percent_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-allow-volume-above-100-percent_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'allow\-volume\-above\-100\-percent' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-event-sounds"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_sound_module__parameter-event-sounds:

      .. rst-class:: ansible-option-title

      **event-sounds**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-event-sounds" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Sounds for events

      Whether to play sounds on user events.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-event-sounds_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_sound_module__parameter-event-sounds_locked:

      .. rst-class:: ansible-option-title

      **event-sounds_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-event-sounds_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'event\-sounds' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-input-feedback-sounds"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_sound_module__parameter-input-feedback-sounds:

      .. rst-class:: ansible-option-title

      **input-feedback-sounds**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-input-feedback-sounds" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Input feedback sounds

      Whether to play sounds on input events.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-input-feedback-sounds_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_sound_module__parameter-input-feedback-sounds_locked:

      .. rst-class:: ansible-option-title

      **input-feedback-sounds_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-input-feedback-sounds_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'input\-feedback\-sounds' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-theme-name"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_sound_module__parameter-theme-name:

      .. rst-class:: ansible-option-title

      **theme-name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-theme-name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Sound theme name

      The XDG sound theme to use for event sounds.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"freedesktop"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-theme-name_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_sound_module__parameter-theme-name_locked:

      .. rst-class:: ansible-option-title

      **theme-name_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-theme-name_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'theme\-name' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.desktop.sound
      org_gnome_desktop_sound:
        event-sounds: true
        event-sounds_locked: true
        theme-name: "freedesktop"
        theme-name_locked: true



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
