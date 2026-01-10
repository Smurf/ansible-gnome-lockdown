.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_location_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_system_location module -- Manages GNOME GSettings for org.gnome.system.location
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_system_location`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.system.location' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-enabled"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_location_module__parameter-enabled:

      .. rst-class:: ansible-option-title

      **enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enabled" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Geolocation services are enabled.

      If true, applications are allowed to access location information.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enabled_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_location_module__parameter-enabled_locked:

      .. rst-class:: ansible-option-title

      **enabled_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enabled_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'enabled' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-max-accuracy-level"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_location_module__parameter-max-accuracy-level:

      .. rst-class:: ansible-option-title

      **max-accuracy-level**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-max-accuracy-level" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The maximum accuracy level of location.

      Configures the maximum level of location accuracy applications are allowed to see. Valid options are “country”, “city”, “neighborhood”, “street”, and “exact” (typically requires GPS receiver). Please keep in mind that this only controls what GeoClue will allow applications to see and they can find user’s location on their own using network resources (albeit with street\-level accuracy at best).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"exact"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-max-accuracy-level_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_location_module__parameter-max-accuracy-level_locked:

      .. rst-class:: ansible-option-title

      **max-accuracy-level_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-max-accuracy-level_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'max\-accuracy\-level' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.system.location
      org_gnome_system_location:
        enabled: false
        enabled_locked: true
        max-accuracy-level: "exact"
        max-accuracy-level_locked: true



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
