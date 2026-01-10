.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_Evince module -- Manages GNOME GSettings for org.gnome.Evince
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_Evince`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.Evince' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-allow-links-change-zoom"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-allow-links-change-zoom:

      .. rst-class:: ansible-option-title

      **allow-links-change-zoom**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-allow-links-change-zoom" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow links to change the zoom level.

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-allow-links-change-zoom_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-allow-links-change-zoom_locked:

      .. rst-class:: ansible-option-title

      **allow-links-change-zoom_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-allow-links-change-zoom_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'allow\-links\-change\-zoom' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-reload"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-auto-reload:

      .. rst-class:: ansible-option-title

      **auto-reload**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-reload" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Automatically reload the document

      The document is automatically reloaded on file change.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-reload_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-auto-reload_locked:

      .. rst-class:: ansible-option-title

      **auto-reload_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-reload_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'auto\-reload' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-document-directory"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-document-directory:

      .. rst-class:: ansible-option-title

      **document-directory**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-document-directory" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The URI of the directory last used to open or save a document

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"nothing"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-document-directory_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-document-directory_locked:

      .. rst-class:: ansible-option-title

      **document-directory_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-document-directory_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'document\-directory' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-override-restrictions"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-override-restrictions:

      .. rst-class:: ansible-option-title

      **override-restrictions**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-override-restrictions" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Override document restrictions

      Override document restrictions, like restriction to copy or to print.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-override-restrictions_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-override-restrictions_locked:

      .. rst-class:: ansible-option-title

      **override-restrictions_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-override-restrictions_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'override\-restrictions' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-page-cache-size"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-page-cache-size:

      .. rst-class:: ansible-option-title

      **page-cache-size**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-page-cache-size" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Page cache size in MiB

      The maximum size that will be used to cache rendered pages, limits maximum zoom level.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"50"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-page-cache-size_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-page-cache-size_locked:

      .. rst-class:: ansible-option-title

      **page-cache-size_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-page-cache-size_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'page\-cache\-size' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-pictures-directory"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-pictures-directory:

      .. rst-class:: ansible-option-title

      **pictures-directory**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-pictures-directory" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The URI of the directory last used to save a picture

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"nothing"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-pictures-directory_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-pictures-directory_locked:

      .. rst-class:: ansible-option-title

      **pictures-directory_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-pictures-directory_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'pictures\-directory' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-caret-navigation-message"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-show-caret-navigation-message:

      .. rst-class:: ansible-option-title

      **show-caret-navigation-message**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-caret-navigation-message" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show a dialog to confirm that the user wants to activate the caret navigation.

      Description \- Schema Blank


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-caret-navigation-message_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Evince_module__parameter-show-caret-navigation-message_locked:

      .. rst-class:: ansible-option-title

      **show-caret-navigation-message_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-caret-navigation-message_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-caret\-navigation\-message' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.Evince
      org_gnome_Evince:
        override-restrictions: true
        override-restrictions_locked: true
        auto-reload: true
        auto-reload_locked: true



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
