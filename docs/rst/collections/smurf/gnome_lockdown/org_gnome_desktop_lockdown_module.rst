.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_desktop_lockdown module -- Manages GNOME GSettings for org.gnome.desktop.lockdown
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_desktop_lockdown`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.desktop.lockdown' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-disable-application-handlers"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-application-handlers:

      .. rst-class:: ansible-option-title

      **disable-application-handlers**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-application-handlers" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable URL and MIME type handlers

      Prevent running any URL or MIME type handler applications.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-application-handlers_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-application-handlers_locked:

      .. rst-class:: ansible-option-title

      **disable-application-handlers_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-application-handlers_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-application\-handlers' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-command-line"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-command-line:

      .. rst-class:: ansible-option-title

      **disable-command-line**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-command-line" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable command line

      Prevent the user from accessing the terminal or specifying a command line to be executed. For example, this would disable access to the panel’s “Run Application” dialog.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-command-line_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-command-line_locked:

      .. rst-class:: ansible-option-title

      **disable-command-line_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-command-line_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-command\-line' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-lock-screen"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-lock-screen:

      .. rst-class:: ansible-option-title

      **disable-lock-screen**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-lock-screen" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable lock screen

      Prevent the user from locking their screen.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-lock-screen_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-lock-screen_locked:

      .. rst-class:: ansible-option-title

      **disable-lock-screen_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-lock-screen_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-lock\-screen' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-log-out"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-log-out:

      .. rst-class:: ansible-option-title

      **disable-log-out**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-log-out" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable log out

      Prevent the user from logging out.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-log-out_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-log-out_locked:

      .. rst-class:: ansible-option-title

      **disable-log-out_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-log-out_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-log\-out' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-print-setup"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-print-setup:

      .. rst-class:: ansible-option-title

      **disable-print-setup**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-print-setup" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable print setup

      Prevent the user from modifying print settings. For example, this would disable access to all applications’ “Print Setup” dialogs.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-print-setup_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-print-setup_locked:

      .. rst-class:: ansible-option-title

      **disable-print-setup_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-print-setup_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-print\-setup' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-printing"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-printing:

      .. rst-class:: ansible-option-title

      **disable-printing**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-printing" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable printing

      Prevent the user from printing. For example, this would disable access to all applications’ “Print” dialogs.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-printing_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-printing_locked:

      .. rst-class:: ansible-option-title

      **disable-printing_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-printing_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-printing' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-save-to-disk"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-save-to-disk:

      .. rst-class:: ansible-option-title

      **disable-save-to-disk**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-save-to-disk" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable saving files to disk

      Prevent the user from saving files to disk. For example, this would disable access to all applications’ “Save as” dialogs.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-save-to-disk_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-save-to-disk_locked:

      .. rst-class:: ansible-option-title

      **disable-save-to-disk_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-save-to-disk_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-save\-to\-disk' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-show-password"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-show-password:

      .. rst-class:: ansible-option-title

      **disable-show-password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-show-password" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable password showing

      Disable the "Show Password" menu item in password entries.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-show-password_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-show-password_locked:

      .. rst-class:: ansible-option-title

      **disable-show-password_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-show-password_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-show\-password' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-user-switching"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-user-switching:

      .. rst-class:: ansible-option-title

      **disable-user-switching**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-user-switching" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable user switching

      Prevent the user from switching to another account while their session is active.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-user-switching_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-disable-user-switching_locked:

      .. rst-class:: ansible-option-title

      **disable-user-switching_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-user-switching_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-user\-switching' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mount-removable-storage-devices-as-read-only"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-mount-removable-storage-devices-as-read-only:

      .. rst-class:: ansible-option-title

      **mount-removable-storage-devices-as-read-only**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mount-removable-storage-devices-as-read-only" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Mount removable storage devices as read\-only

      Prevent users from writing or modifying files on removable storage devices (i.e. flash disks, mobile phones, cameras).


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mount-removable-storage-devices-as-read-only_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-mount-removable-storage-devices-as-read-only_locked:

      .. rst-class:: ansible-option-title

      **mount-removable-storage-devices-as-read-only_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mount-removable-storage-devices-as-read-only_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'mount\-removable\-storage\-devices\-as\-read\-only' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-user-administration-disabled"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-user-administration-disabled:

      .. rst-class:: ansible-option-title

      **user-administration-disabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-user-administration-disabled" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable user administration

      Stop the user from modifying user accounts. By default, we allow adding and removing users, as well as changing other users settings.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-user-administration-disabled_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_lockdown_module__parameter-user-administration-disabled_locked:

      .. rst-class:: ansible-option-title

      **user-administration-disabled_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-user-administration-disabled_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'user\-administration\-disabled' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.desktop.lockdown
      org_gnome_desktop_lockdown:
        disable-command-line: false
        disable-command-line_locked: true
        disable-save-to-disk: false
        disable-save-to-disk_locked: true



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
