.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_SessionManager_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_SessionManager module -- Manages GNOME GSettings for org.gnome.SessionManager
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_SessionManager`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.SessionManager' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-auto-save-session"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SessionManager_module__parameter-auto-save-session:

      .. rst-class:: ansible-option-title

      **auto-save-session**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-save-session" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Save sessions

      If enabled, gnome\-session will save the session automatically.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-save-session-one-shot"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SessionManager_module__parameter-auto-save-session-one-shot:

      .. rst-class:: ansible-option-title

      **auto-save-session-one-shot**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-save-session-one-shot" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Save this session

      When enabled, gnome\-session will automatically save the next session at log out even if auto saving is disabled.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-save-session-one-shot_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SessionManager_module__parameter-auto-save-session-one-shot_locked:

      .. rst-class:: ansible-option-title

      **auto-save-session-one-shot_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-save-session-one-shot_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'auto\-save\-session\-one\-shot' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-save-session_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SessionManager_module__parameter-auto-save-session_locked:

      .. rst-class:: ansible-option-title

      **auto-save-session_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-save-session_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'auto\-save\-session' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-logout-prompt"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SessionManager_module__parameter-logout-prompt:

      .. rst-class:: ansible-option-title

      **logout-prompt**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logout-prompt" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Logout prompt

      If enabled, gnome\-session will prompt the user before ending a session.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-logout-prompt_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SessionManager_module__parameter-logout-prompt_locked:

      .. rst-class:: ansible-option-title

      **logout-prompt_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logout-prompt_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'logout\-prompt' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-fallback-warning"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SessionManager_module__parameter-show-fallback-warning:

      .. rst-class:: ansible-option-title

      **show-fallback-warning**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-fallback-warning" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show the fallback warning

      If enabled, gnome\-session will display a warning dialog after login if the session was automatically fallen back.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-fallback-warning_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SessionManager_module__parameter-show-fallback-warning_locked:

      .. rst-class:: ansible-option-title

      **show-fallback-warning_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-fallback-warning_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-fallback\-warning' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.SessionManager
      org_gnome_SessionManager:
        auto-save-session: false
        auto-save-session_locked: true
        auto-save-session-one-shot: false
        auto-save-session-one-shot_locked: true



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
