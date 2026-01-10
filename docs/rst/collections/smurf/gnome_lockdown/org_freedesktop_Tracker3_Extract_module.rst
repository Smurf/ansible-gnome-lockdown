.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Extract_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_freedesktop_Tracker3_Extract module -- Manages GNOME GSettings for org.freedesktop.Tracker3.Extract
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_freedesktop_Tracker3_Extract`.

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

- This module allows for the configuration of GSettings keys within the 'org.freedesktop.Tracker3.Extract' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-max-bytes"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Extract_module__parameter-max-bytes:

      .. rst-class:: ansible-option-title

      **max-bytes**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-max-bytes" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Max bytes to extract

      Maximum number of UTF\-8 bytes to extract.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1048576`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-max-bytes_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Extract_module__parameter-max-bytes_locked:

      .. rst-class:: ansible-option-title

      **max-bytes_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-max-bytes_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'max\-bytes' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-text-allowlist"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Extract_module__parameter-text-allowlist:

      .. rst-class:: ansible-option-title

      **text-allowlist**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-text-allowlist" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Text file allowlist

      Filename patterns for plain text documents that should be indexed


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[ '\*.txt', '\*.md', '\*.mdwn' ]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-text-allowlist_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Extract_module__parameter-text-allowlist_locked:

      .. rst-class:: ansible-option-title

      **text-allowlist_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-text-allowlist_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'text\-allowlist' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wait-for-miner-fs"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Extract_module__parameter-wait-for-miner-fs:

      .. rst-class:: ansible-option-title

      **wait-for-miner-fs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wait-for-miner-fs" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Wait for FS miner to be done before extracting

      When true, tracker\-extract will wait for tracker\-miner\-fs to be done crawling before extracting meta\-data. This option is useful on constrained environment where it is important to list files as fast as possible and can wait to get meta\-data later.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wait-for-miner-fs_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Extract_module__parameter-wait-for-miner-fs_locked:

      .. rst-class:: ansible-option-title

      **wait-for-miner-fs_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wait-for-miner-fs_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'wait\-for\-miner\-fs' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.freedesktop.Tracker3.Extract
      org_freedesktop_Tracker3_Extract:
        max-bytes: 1048576
        max-bytes_locked: true
        text-allowlist: "[ '*.txt', '*.md', '*.mdwn' ]"
        text-allowlist_locked: true



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
