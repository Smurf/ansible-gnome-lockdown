.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_FTS_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_freedesktop_Tracker3_FTS module -- Manages GNOME GSettings for org.freedesktop.Tracker3.FTS
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_freedesktop_Tracker3_FTS`.

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

- This module allows for the configuration of GSettings keys within the 'org.freedesktop.Tracker3.FTS' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-enable-stemmer"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_FTS_module__parameter-enable-stemmer:

      .. rst-class:: ansible-option-title

      **enable-stemmer**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-stemmer" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable stemmer

      Simplify the words to their root to provide more results. E.g. “shelves” and “shelf” to “shel”


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable-stemmer_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_FTS_module__parameter-enable-stemmer_locked:

      .. rst-class:: ansible-option-title

      **enable-stemmer_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-stemmer_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'enable\-stemmer' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable-unaccent"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_FTS_module__parameter-enable-unaccent:

      .. rst-class:: ansible-option-title

      **enable-unaccent**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-unaccent" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable unaccent

      Translate accented characters to the equivalent unaccented. E.g. “Idéa” to “Idea” for improved matching.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable-unaccent_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_FTS_module__parameter-enable-unaccent_locked:

      .. rst-class:: ansible-option-title

      **enable-unaccent_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-unaccent_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'enable\-unaccent' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignore-numbers"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_FTS_module__parameter-ignore-numbers:

      .. rst-class:: ansible-option-title

      **ignore-numbers**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignore-numbers" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Ignore numbers

      If enabled, numbers will not be indexed.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignore-numbers_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_FTS_module__parameter-ignore-numbers_locked:

      .. rst-class:: ansible-option-title

      **ignore-numbers_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignore-numbers_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'ignore\-numbers' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.freedesktop.Tracker3.FTS
      org_freedesktop_Tracker3_FTS:
        enable-stemmer: false
        enable-stemmer_locked: true
        enable-unaccent: true
        enable-unaccent_locked: true



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
