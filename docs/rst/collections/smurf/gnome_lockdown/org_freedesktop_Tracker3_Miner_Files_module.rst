.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files module -- Manages GNOME GSettings for org.freedesktop.Tracker3.Miner.Files
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files`.

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

- This module allows for the configuration of GSettings keys within the 'org.freedesktop.Tracker3.Miner.Files' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-crawling-interval"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-crawling-interval:

      .. rst-class:: ansible-option-title

      **crawling-interval**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crawling-interval" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Crawling interval

      Interval in days to check whether the filesystem is up to date in the database. 0 forces crawling anytime, \-1 forces it only after unclean shutdowns, and \-2 disables it entirely.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`\-1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crawling-interval_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-crawling-interval_locked:

      .. rst-class:: ansible-option-title

      **crawling-interval_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crawling-interval_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'crawling\-interval' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable-monitors"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-enable-monitors:

      .. rst-class:: ansible-option-title

      **enable-monitors**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-monitors" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable monitors

      Set to false to completely disable any file monitoring


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable-monitors_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-enable-monitors_locked:

      .. rst-class:: ansible-option-title

      **enable-monitors_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-monitors_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'enable\-monitors' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignored-directories"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-ignored-directories:

      .. rst-class:: ansible-option-title

      **ignored-directories**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignored-directories" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Ignored directories

      List of directories to avoid


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[ 'po', 'CVS', 'core\-dumps', 'lost+found' ]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignored-directories-with-content"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-ignored-directories-with-content:

      .. rst-class:: ansible-option-title

      **ignored-directories-with-content**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignored-directories-with-content" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Ignored directories with content

      Avoid any directory containing a file blocklisted here


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[ '.trackerignore', '.git', '.hg', '.nomedia' ]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignored-directories-with-content_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-ignored-directories-with-content_locked:

      .. rst-class:: ansible-option-title

      **ignored-directories-with-content_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignored-directories-with-content_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'ignored\-directories\-with\-content' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignored-directories_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-ignored-directories_locked:

      .. rst-class:: ansible-option-title

      **ignored-directories_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignored-directories_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'ignored\-directories' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignored-files"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-ignored-files:

      .. rst-class:: ansible-option-title

      **ignored-files**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignored-files" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Ignored files

      List of file patterns to avoid


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[ '\*~', '\*.o', '\*.la', '\*.lo' , '\*.loT', '\*.in', '\*.m4', '\*.rej', '\*.gmo', '\*.orig', '\*.pc', '\*.omf', '\*.aux', '\*.tmp', '\*.vmdk', '\*.vm\*', '\*.nvram', '\*.part', '\*.rcore', '\*.lzo', 'autom4te', 'conftest', 'confstat', 'Makefile', 'SCCS', 'ltmain.sh', 'libtool', 'config.status', 'confdefs.h', 'configure', '#\*#', '~$\*.doc?', '~$\*.dot?', '~$\*.xls?', '~$\*.xlt?', '~$\*.xlam', '~$\*.ppt?', '~$\*.pot?', '~$\*.ppam', '~$\*.ppsm', '~$\*.ppsx', '~$\*.vsd?', '~$\*.vss?', '~$\*.vst?', '\*.directory' ]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ignored-files_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-ignored-files_locked:

      .. rst-class:: ansible-option-title

      **ignored-files_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ignored-files_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'ignored\-files' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index-on-battery"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-index-on-battery:

      .. rst-class:: ansible-option-title

      **index-on-battery**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index-on-battery" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Index when running on battery

      Set to true to index while running on battery


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index-on-battery-first-time"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-index-on-battery-first-time:

      .. rst-class:: ansible-option-title

      **index-on-battery-first-time**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index-on-battery-first-time" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Perform initial indexing when running on battery

      Set to true to index while running on battery for the first time only


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index-on-battery-first-time_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-index-on-battery-first-time_locked:

      .. rst-class:: ansible-option-title

      **index-on-battery-first-time_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index-on-battery-first-time_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'index\-on\-battery\-first\-time' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index-on-battery_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-index-on-battery_locked:

      .. rst-class:: ansible-option-title

      **index-on-battery_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index-on-battery_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'index\-on\-battery' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index-optical-discs"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-index-optical-discs:

      .. rst-class:: ansible-option-title

      **index-optical-discs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index-optical-discs" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Index optical discs

      Set to true to enable indexing CDs, DVDs, and generally optical media (if removable devices are not indexed, optical discs won’t be either)


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index-optical-discs_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-index-optical-discs_locked:

      .. rst-class:: ansible-option-title

      **index-optical-discs_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index-optical-discs_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'index\-optical\-discs' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index-recursive-directories"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-index-recursive-directories:

      .. rst-class:: ansible-option-title

      **index-recursive-directories**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index-recursive-directories" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Directories to index recursively

      List of directories to index recursively, Special values include: ‘&DESKTOP’, ‘&DOCUMENTS’, ‘&DOWNLOAD’, ‘&MUSIC’, ‘&PICTURES’, ‘&PUBLIC\_SHARE’, ‘&TEMPLATES’, ‘&VIDEOS’. See /etc/xdg/user\-dirs.defaults and $HOME/.config/user\-dirs.default


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[ '&DESKTOP', '&DOCUMENTS', '&MUSIC', '&PICTURES', '&VIDEOS' ]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index-recursive-directories_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-index-recursive-directories_locked:

      .. rst-class:: ansible-option-title

      **index-recursive-directories_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index-recursive-directories_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'index\-recursive\-directories' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index-removable-devices"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-index-removable-devices:

      .. rst-class:: ansible-option-title

      **index-removable-devices**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index-removable-devices" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Index removable devices

      Set to true to enable indexing mounted directories for removable devices.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index-removable-devices_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-index-removable-devices_locked:

      .. rst-class:: ansible-option-title

      **index-removable-devices_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index-removable-devices_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'index\-removable\-devices' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index-single-directories"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-index-single-directories:

      .. rst-class:: ansible-option-title

      **index-single-directories**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index-single-directories" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Directories to index non\-recursively

      List of directories to index without inspecting subfolders, Special values include: ‘&DESKTOP’, ‘&DOCUMENTS’, ‘&DOWNLOAD’, ‘&MUSIC’, ‘&PICTURES’, ‘&PUBLIC\_SHARE’, ‘&TEMPLATES’, ‘&VIDEOS’. See /etc/xdg/user\-dirs.defaults and $HOME/.config/user\-dirs.default


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[ '$HOME', '&DOWNLOAD' ]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index-single-directories_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-index-single-directories_locked:

      .. rst-class:: ansible-option-title

      **index-single-directories_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index-single-directories_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'index\-single\-directories' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-initial-sleep"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-initial-sleep:

      .. rst-class:: ansible-option-title

      **initial-sleep**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-initial-sleep" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Initial sleep

      Initial sleep time, in seconds.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`15`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-initial-sleep_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-initial-sleep_locked:

      .. rst-class:: ansible-option-title

      **initial-sleep_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-initial-sleep_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'initial\-sleep' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-low-disk-space-limit"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-low-disk-space-limit:

      .. rst-class:: ansible-option-title

      **low-disk-space-limit**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-low-disk-space-limit" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Low disk space limit

      Disk space threshold in percent at which to pause indexing, or \-1 to disable.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`\-1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-low-disk-space-limit_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-low-disk-space-limit_locked:

      .. rst-class:: ansible-option-title

      **low-disk-space-limit_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-low-disk-space-limit_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'low\-disk\-space\-limit' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-removable-days-threshold"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-removable-days-threshold:

      .. rst-class:: ansible-option-title

      **removable-days-threshold**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-removable-days-threshold" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Removable devices’ data permanence threshold

      Threshold in days after which files from removables devices will be removed from database if not mounted. 0 means never, maximum is 365.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`3`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-removable-days-threshold_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-removable-days-threshold_locked:

      .. rst-class:: ansible-option-title

      **removable-days-threshold_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-removable-days-threshold_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'removable\-days\-threshold' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-throttle"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-throttle:

      .. rst-class:: ansible-option-title

      **throttle**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-throttle" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Throttle

      Indexing speed, the higher the slower.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`0`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-throttle_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_freedesktop_Tracker3_Miner_Files_module__parameter-throttle_locked:

      .. rst-class:: ansible-option-title

      **throttle_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-throttle_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'throttle' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.freedesktop.Tracker3.Miner.Files
      org_freedesktop_Tracker3_Miner_Files:
        initial-sleep: 15
        initial-sleep_locked: true
        throttle: 0
        throttle_locked: true



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
