.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_desktop_privacy module -- Manages GNOME GSettings for org.gnome.desktop.privacy
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_desktop_privacy`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.desktop.privacy' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-disable-camera"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-disable-camera:

      .. rst-class:: ansible-option-title

      **disable-camera**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-camera" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Don’t allow applications to access the camera

      If TRUE, applications should not use the camera.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-camera_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-disable-camera_locked:

      .. rst-class:: ansible-option-title

      **disable-camera_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-camera_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-camera' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-microphone"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-disable-microphone:

      .. rst-class:: ansible-option-title

      **disable-microphone**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-microphone" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Don’t allow applications to access the microphone

      If TRUE, applications should not use the microphone.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-microphone_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-disable-microphone_locked:

      .. rst-class:: ansible-option-title

      **disable-microphone_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-microphone_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-microphone' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-sound-output"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-disable-sound-output:

      .. rst-class:: ansible-option-title

      **disable-sound-output**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-sound-output" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Don’t allow applications to output sound

      If TRUE, applications should not make sound.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable-sound-output_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-disable-sound-output_locked:

      .. rst-class:: ansible-option-title

      **disable-sound-output_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable-sound-output_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'disable\-sound\-output' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hide-identity"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-hide-identity:

      .. rst-class:: ansible-option-title

      **hide-identity**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hide-identity" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Controls visibility of personal information

      If set to true, the system will make an effort to not divulge the user’s identity on screen or on the network.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hide-identity_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-hide-identity_locked:

      .. rst-class:: ansible-option-title

      **hide-identity_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hide-identity_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'hide\-identity' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-old-files-age"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-old-files-age:

      .. rst-class:: ansible-option-title

      **old-files-age**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-old-files-age" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of days to keep trash and temporary files

      Consider trash and temporary files old after this many days.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"30"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-old-files-age_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-old-files-age_locked:

      .. rst-class:: ansible-option-title

      **old-files-age_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-old-files-age_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'old\-files\-age' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-privacy-screen"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-privacy-screen:

      .. rst-class:: ansible-option-title

      **privacy-screen**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-privacy-screen" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether the privacy screen is enabled

      If the underlying hardware has privacy screen support and this setting is enabled, the panels supporting this technology will be obscured from lateral view.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-privacy-screen_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-privacy-screen_locked:

      .. rst-class:: ansible-option-title

      **privacy-screen_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-privacy-screen_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'privacy\-screen' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-recent-files-max-age"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-recent-files-max-age:

      .. rst-class:: ansible-option-title

      **recent-files-max-age**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-recent-files-max-age" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of days to remember recently used files for

      Recently used files will be remembered for this many days. If set to 0, recent files will not be remembered; if set to \-1, they will be retained indefinitely.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`\-1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-recent-files-max-age_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-recent-files-max-age_locked:

      .. rst-class:: ansible-option-title

      **recent-files-max-age_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-recent-files-max-age_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'recent\-files\-max\-age' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-remember-app-usage"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-remember-app-usage:

      .. rst-class:: ansible-option-title

      **remember-app-usage**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-remember-app-usage" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to remember application usage

      If FALSE, application usage will not be monitored and recorded.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-remember-app-usage_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-remember-app-usage_locked:

      .. rst-class:: ansible-option-title

      **remember-app-usage_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-remember-app-usage_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'remember\-app\-usage' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-remember-recent-files"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-remember-recent-files:

      .. rst-class:: ansible-option-title

      **remember-recent-files**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-remember-recent-files" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to remember recently used files

      If FALSE, applications will not remember recently used files.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-remember-recent-files_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-remember-recent-files_locked:

      .. rst-class:: ansible-option-title

      **remember-recent-files_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-remember-recent-files_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'remember\-recent\-files' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-remove-old-temp-files"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-remove-old-temp-files:

      .. rst-class:: ansible-option-title

      **remove-old-temp-files**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-remove-old-temp-files" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to remove old temporary files automatically

      If TRUE, automatically remove temporary files when they are older than “old\-files\-age” days.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-remove-old-temp-files_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-remove-old-temp-files_locked:

      .. rst-class:: ansible-option-title

      **remove-old-temp-files_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-remove-old-temp-files_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'remove\-old\-temp\-files' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-remove-old-trash-files"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-remove-old-trash-files:

      .. rst-class:: ansible-option-title

      **remove-old-trash-files**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-remove-old-trash-files" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to remove old files from the trash automatically

      If TRUE, automatically remove files from the trash when they are older than “old\-files\-age” days.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-remove-old-trash-files_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-remove-old-trash-files_locked:

      .. rst-class:: ansible-option-title

      **remove-old-trash-files_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-remove-old-trash-files_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'remove\-old\-trash\-files' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-report-technical-problems"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-report-technical-problems:

      .. rst-class:: ansible-option-title

      **report-technical-problems**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-report-technical-problems" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Send reports of technical problems to the vendor

      If TRUE, anonymized reports will be sent automatically to the vendor.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-report-technical-problems_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-report-technical-problems_locked:

      .. rst-class:: ansible-option-title

      **report-technical-problems_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-report-technical-problems_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'report\-technical\-problems' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-send-software-usage-stats"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-send-software-usage-stats:

      .. rst-class:: ansible-option-title

      **send-software-usage-stats**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-send-software-usage-stats" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Send statistics when applications are removed or installed

      If FALSE, no anonymous installation or removal information will be sent to the vendor.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-send-software-usage-stats_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-send-software-usage-stats_locked:

      .. rst-class:: ansible-option-title

      **send-software-usage-stats_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-send-software-usage-stats_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'send\-software\-usage\-stats' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-full-name-in-top-bar"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-show-full-name-in-top-bar:

      .. rst-class:: ansible-option-title

      **show-full-name-in-top-bar**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-full-name-in-top-bar" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show full name in the user menu

      Whether the users full name is shown in the user menu or not.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-full-name-in-top-bar_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-show-full-name-in-top-bar_locked:

      .. rst-class:: ansible-option-title

      **show-full-name-in-top-bar_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-full-name-in-top-bar_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-full\-name\-in\-top\-bar' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-usb-protection"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-usb-protection:

      .. rst-class:: ansible-option-title

      **usb-protection**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-usb-protection" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to protect USB devices

      If the USBGuard service is present and this setting is enabled, USB devices will be protected as configured in the usb\-protection\-level setting.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-usb-protection-level"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-usb-protection-level:

      .. rst-class:: ansible-option-title

      **usb-protection-level**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-usb-protection-level" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      When USB devices should be rejected

      If set to “lockscreen”, only when the lock screen is present new USB devices will be rejected; if set to “always”, all new USB devices will always be rejected.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"lockscreen"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-usb-protection-level_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-usb-protection-level_locked:

      .. rst-class:: ansible-option-title

      **usb-protection-level_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-usb-protection-level_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'usb\-protection\-level' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-usb-protection_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_desktop_privacy_module__parameter-usb-protection_locked:

      .. rst-class:: ansible-option-title

      **usb-protection_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-usb-protection_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'usb\-protection' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.desktop.privacy
      org_gnome_desktop_privacy:
        hide-identity: false
        hide-identity_locked: true
        show-full-name-in-top-bar: true
        show-full-name-in-top-bar_locked: true



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
