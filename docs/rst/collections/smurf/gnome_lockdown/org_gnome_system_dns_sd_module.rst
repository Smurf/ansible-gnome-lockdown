.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_dns_sd_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_system_dns_sd module -- Manages GNOME GSettings for org.gnome.system.dns\_sd
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_system_dns_sd`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.system.dns\_sd' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-display-local"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_dns_sd_module__parameter-display-local:

      .. rst-class:: ansible-option-title

      **display-local**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-display-local" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      How to display local DNS\-SD services

      How DNS\-SD services are displayed in the "network:///" location. Possible values are "merged", "separate" (the Local Network folder) and "disabled".


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"merged"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-display-local_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_dns_sd_module__parameter-display-local_locked:

      .. rst-class:: ansible-option-title

      **display-local_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-display-local_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'display\-local' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-extra-domains"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_dns_sd_module__parameter-extra-domains:

      .. rst-class:: ansible-option-title

      **extra-domains**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-extra-domains" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Extra domains to look for DNS\-SD services in

      Comma separated list of DNS\-SD domains that should be visible in the "network:///" location.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-extra-domains_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_dns_sd_module__parameter-extra-domains_locked:

      .. rst-class:: ansible-option-title

      **extra-domains_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-extra-domains_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'extra\-domains' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.system.dns_sd
      org_gnome_system_dns_sd:
        display-local: "merged"
        display-local_locked: true
        extra-domains: ""
        extra-domains_locked: true



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
