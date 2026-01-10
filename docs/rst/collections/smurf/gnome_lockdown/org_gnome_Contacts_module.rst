.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_Contacts module -- Manages GNOME GSettings for org.gnome.Contacts
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_Contacts`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.Contacts' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-did-initial-setup"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module__parameter-did-initial-setup:

      .. rst-class:: ansible-option-title

      **did-initial-setup**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-did-initial-setup" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      First\-time setup done.

      Set to true after the user has run the first\-time setup wizard.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-did-initial-setup_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module__parameter-did-initial-setup_locked:

      .. rst-class:: ansible-option-title

      **did-initial-setup_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-did-initial-setup_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'did\-initial\-setup' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sort-on-surname"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module__parameter-sort-on-surname:

      .. rst-class:: ansible-option-title

      **sort-on-surname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sort-on-surname" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Sort contacts on surname.

      If this is set to true, the list of contacts will be sorted on their surnames. Otherwise, it will be sorted on the first names of the contacts.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sort-on-surname_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module__parameter-sort-on-surname_locked:

      .. rst-class:: ansible-option-title

      **sort-on-surname_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sort-on-surname_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'sort\-on\-surname' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-fullscreen"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module__parameter-window-fullscreen:

      .. rst-class:: ansible-option-title

      **window-fullscreen**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-fullscreen" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Is the window fullscreen

      Stores if the window is currently maximized.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-fullscreen_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module__parameter-window-fullscreen_locked:

      .. rst-class:: ansible-option-title

      **window-fullscreen_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-fullscreen_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'window\-fullscreen' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-height"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module__parameter-window-height:

      .. rst-class:: ansible-option-title

      **window-height**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-height" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The default height of the contacts window.

      If the window size has not been changed by the user yet this will be used as the initial value for the height of the window.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`600`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-height_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module__parameter-window-height_locked:

      .. rst-class:: ansible-option-title

      **window-height_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-height_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'window\-height' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-maximized"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module__parameter-window-maximized:

      .. rst-class:: ansible-option-title

      **window-maximized**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-maximized" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Is the window maximized?

      Stores if the window is currently maximized.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-maximized_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module__parameter-window-maximized_locked:

      .. rst-class:: ansible-option-title

      **window-maximized_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-maximized_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'window\-maximized' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-width"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module__parameter-window-width:

      .. rst-class:: ansible-option-title

      **window-width**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-width" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The default width of the contacts window.

      If the window size has not been changed by the user yet this will be used as the initial value for the width of the window.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`800`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-width_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_Contacts_module__parameter-window-width_locked:

      .. rst-class:: ansible-option-title

      **window-width_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-width_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'window\-width' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.Contacts
      org_gnome_Contacts:
        did-initial-setup: false
        did-initial-setup_locked: true
        sort-on-surname: false
        sort-on-surname_locked: true



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
