.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_proxy_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_system_proxy module -- Manages GNOME GSettings for org.gnome.system.proxy
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_system_proxy`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.system.proxy' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-autoconfig-url"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_proxy_module__parameter-autoconfig-url:

      .. rst-class:: ansible-option-title

      **autoconfig-url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-autoconfig-url" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Automatic proxy configuration URL

      URL that provides proxy configuration values. When mode is “auto”, this URL is used to look up proxy information for all protocols.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-autoconfig-url_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_proxy_module__parameter-autoconfig-url_locked:

      .. rst-class:: ansible-option-title

      **autoconfig-url_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-autoconfig-url_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'autoconfig\-url' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignore-hosts"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_proxy_module__parameter-ignore-hosts:

      .. rst-class:: ansible-option-title

      **ignore-hosts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignore-hosts" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Non\-proxy hosts

      This key contains a list of hosts which are connected to directly, rather than via the proxy (if it is active). The values can be hostnames, domains (using an initial wildcard like \*.foo.com), IP host addresses (both IPv4 and IPv6) and network addresses with a netmask (something like 192.168.0.0/24).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[ 'localhost', '127.0.0.0/8', '::1' ]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignore-hosts_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_proxy_module__parameter-ignore-hosts_locked:

      .. rst-class:: ansible-option-title

      **ignore-hosts_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignore-hosts_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'ignore\-hosts' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mode"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_proxy_module__parameter-mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Proxy configuration mode

      Select the proxy configuration mode. Supported values are “none”, “manual”, “auto”. If this is “none”, then proxies are not used. If it is “auto”, the autoconfiguration URL described by the “autoconfig\-url” key is used. If it is “manual”, then the proxies described by “/system/proxy/http”, “/system/proxy/https”, “/system/proxy/ftp” and “/system/proxy/socks” will be used. Each of the 4 proxy types is enabled if its “host” key is non\-empty and its “port” key is non\-0. If an http proxy is configured, but an https proxy is not, then the http proxy is also used for https. If a SOCKS proxy is configured, it is used for all protocols, except that the http, https, and ftp proxy settings override it for those protocols only.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"none"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mode_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_proxy_module__parameter-mode_locked:

      .. rst-class:: ansible-option-title

      **mode_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mode_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'mode' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-use-same-proxy"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_proxy_module__parameter-use-same-proxy:

      .. rst-class:: ansible-option-title

      **use-same-proxy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-use-same-proxy" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use HTTP proxy for all protocols

      Whether to use the HTTP proxy for all protocols or not.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-use-same-proxy_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_system_proxy_module__parameter-use-same-proxy_locked:

      .. rst-class:: ansible-option-title

      **use-same-proxy_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-use-same-proxy_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'use\-same\-proxy' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.system.proxy
      org_gnome_system_proxy:
        mode: "none"
        mode_locked: true
        autoconfig-url: ""
        autoconfig-url_locked: true



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
