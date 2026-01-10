.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_SimpleScan module -- Manages GNOME GSettings for org.gnome.SimpleScan
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_SimpleScan`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.SimpleScan' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-brightness"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-brightness:

      .. rst-class:: ansible-option-title

      **brightness**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-brightness" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Brightness of scan

      The brightness adjustment from \-100 to 100 (0 being none).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`0`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-brightness_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-brightness_locked:

      .. rst-class:: ansible-option-title

      **brightness_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-brightness_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'brightness' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-contrast"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-contrast:

      .. rst-class:: ansible-option-title

      **contrast**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-contrast" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Contrast of scan

      The contrast adjustment from \-100 to 100 (0 being none).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`0`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-contrast_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-contrast_locked:

      .. rst-class:: ansible-option-title

      **contrast_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-contrast_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'contrast' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-document-type"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-document-type:

      .. rst-class:: ansible-option-title

      **document-type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-document-type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Type of document being scanned

      Type of document being scanned. This setting decides on the scan resolution, colors and post\-processing.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"photo"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-document-type_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-document-type_locked:

      .. rst-class:: ansible-option-title

      **document-type_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-document-type_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'document\-type' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jpeg-quality"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-jpeg-quality:

      .. rst-class:: ansible-option-title

      **jpeg-quality**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jpeg-quality" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Quality value to use for JPEG compression

      Quality value to use for JPEG compression.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`75`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jpeg-quality_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-jpeg-quality_locked:

      .. rst-class:: ansible-option-title

      **jpeg-quality_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jpeg-quality_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'jpeg\-quality' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-page-delay"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-page-delay:

      .. rst-class:: ansible-option-title

      **page-delay**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-page-delay" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Delay in millisecond between pages

      Delay in millisecond between pages.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1000`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-page-delay_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-page-delay_locked:

      .. rst-class:: ansible-option-title

      **page-delay_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-page-delay_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'page\-delay' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-page-side"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-page-side:

      .. rst-class:: ansible-option-title

      **page-side**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-page-side" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Page side to scan

      The page side to scan.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"both"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-page-side_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-page-side_locked:

      .. rst-class:: ansible-option-title

      **page-side_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-page-side_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'page\-side' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-paper-height"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-paper-height:

      .. rst-class:: ansible-option-title

      **paper-height**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-paper-height" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Height of paper in tenths of a mm

      The height of the paper in tenths of a mm (or 0 for automatic paper detection).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`0`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-paper-height_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-paper-height_locked:

      .. rst-class:: ansible-option-title

      **paper-height_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-paper-height_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'paper\-height' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-paper-width"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-paper-width:

      .. rst-class:: ansible-option-title

      **paper-width**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-paper-width" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Width of paper in tenths of a mm

      The width of the paper in tenths of a mm (or 0 for automatic paper detection).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`0`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-paper-width_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-paper-width_locked:

      .. rst-class:: ansible-option-title

      **paper-width_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-paper-width_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'paper\-width' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-photo-dpi"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-photo-dpi:

      .. rst-class:: ansible-option-title

      **photo-dpi**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-photo-dpi" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Resolution for image scans

      The resolution in dots\-per\-inch to use when scanning images.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`300`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-photo-dpi_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-photo-dpi_locked:

      .. rst-class:: ansible-option-title

      **photo-dpi_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-photo-dpi_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'photo\-dpi' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-postproc-arguments"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-postproc-arguments:

      .. rst-class:: ansible-option-title

      **postproc-arguments**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-postproc-arguments" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Additional arguments for the postprocessing script

      Additional arguments for the postprocessing script.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-postproc-arguments_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-postproc-arguments_locked:

      .. rst-class:: ansible-option-title

      **postproc-arguments_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-postproc-arguments_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'postproc\-arguments' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-postproc-enabled"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-postproc-enabled:

      .. rst-class:: ansible-option-title

      **postproc-enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-postproc-enabled" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether or not postprocessing is enabled

      Whether or not postprocessing is enabled.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-postproc-enabled_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-postproc-enabled_locked:

      .. rst-class:: ansible-option-title

      **postproc-enabled_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-postproc-enabled_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'postproc\-enabled' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-postproc-keep-original"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-postproc-keep-original:

      .. rst-class:: ansible-option-title

      **postproc-keep-original**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-postproc-keep-original" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether or not to keep the original, unprocessed file

      Whether or not to keep the original, unprocessed file. The "\_orig" filename will be added to the filename immediately before the file extension.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-postproc-keep-original_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-postproc-keep-original_locked:

      .. rst-class:: ansible-option-title

      **postproc-keep-original_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-postproc-keep-original_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'postproc\-keep\-original' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-postproc-script"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-postproc-script:

      .. rst-class:: ansible-option-title

      **postproc-script**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-postproc-script" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The path to the postprocessing script

      The path to the postprocessing script.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-postproc-script_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-postproc-script_locked:

      .. rst-class:: ansible-option-title

      **postproc-script_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-postproc-script_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'postproc\-script' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save-directory"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-save-directory:

      .. rst-class:: ansible-option-title

      **save-directory**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-save-directory" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Directory to save files to

      The directory to save files to. Defaults to the documents directory if unset.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save-directory_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-save-directory_locked:

      .. rst-class:: ansible-option-title

      **save-directory_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-save-directory_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'save\-directory' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save-format"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-save-format:

      .. rst-class:: ansible-option-title

      **save-format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-save-format" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      File format that is used for saving image files

      MIME type that is used for saving image files. Examples of supported MIME types: image/jpeg, image/png, application/pdf


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"application/pdf"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save-format_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-save-format_locked:

      .. rst-class:: ansible-option-title

      **save-format_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-save-format_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'save\-format' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-selected-device"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-selected-device:

      .. rst-class:: ansible-option-title

      **selected-device**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-selected-device" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Device to scan from

      SANE device to acquire images from.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-selected-device_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-selected-device_locked:

      .. rst-class:: ansible-option-title

      **selected-device_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-selected-device_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'selected\-device' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-text-dpi"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-text-dpi:

      .. rst-class:: ansible-option-title

      **text-dpi**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-text-dpi" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Resolution for text scans

      The resolution in dots\-per\-inch to use when scanning text.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`150`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-text-dpi_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_SimpleScan_module__parameter-text-dpi_locked:

      .. rst-class:: ansible-option-title

      **text-dpi_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-text-dpi_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'text\-dpi' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.SimpleScan
      org_gnome_SimpleScan:
        selected-device: ""
        selected-device_locked: true
        document-type: "photo"
        document-type_locked: true



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
