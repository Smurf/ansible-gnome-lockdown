.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_calculator module -- Manages GNOME GSettings for org.gnome.calculator
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_calculator`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.calculator' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-accuracy"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-accuracy:

      .. rst-class:: ansible-option-title

      **accuracy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-accuracy" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Accuracy value

      The number of digits displayed after the numeric point


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`9`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-accuracy_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-accuracy_locked:

      .. rst-class:: ansible-option-title

      **accuracy_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-accuracy_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'accuracy' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-angle-units"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-angle-units:

      .. rst-class:: ansible-option-title

      **angle-units**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-angle-units" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Angle units

      The angle units to use


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"degrees"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-angle-units_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-angle-units_locked:

      .. rst-class:: ansible-option-title

      **angle-units_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-angle-units_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'angle\-units' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-base"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-base:

      .. rst-class:: ansible-option-title

      **base**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-base" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Numeric Base

      The numeric base


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`10`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-base_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-base_locked:

      .. rst-class:: ansible-option-title

      **base_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-base_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'base' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-button-mode"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-button-mode:

      .. rst-class:: ansible-option-title

      **button-mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-button-mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Button mode

      The button mode


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"basic"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-button-mode_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-button-mode_locked:

      .. rst-class:: ansible-option-title

      **button-mode_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-button-mode_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'button\-mode' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-number-format"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-number-format:

      .. rst-class:: ansible-option-title

      **number-format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-number-format" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number format

      The format to display numbers in


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"automatic"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-number-format_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-number-format_locked:

      .. rst-class:: ansible-option-title

      **number-format_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-number-format_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'number\-format' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-precision"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-precision:

      .. rst-class:: ansible-option-title

      **precision**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-precision" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Internal precision

      The internal precision used with the MPFR library


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`2000`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-precision_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-precision_locked:

      .. rst-class:: ansible-option-title

      **precision_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-precision_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'precision' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-refresh-interval"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-refresh-interval:

      .. rst-class:: ansible-option-title

      **refresh-interval**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-refresh-interval" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Currency update interval

      How often the currency exchange rates should be updated. A value of 0 means the currency exchange rates won't be fetched from the network at all.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`604800`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-refresh-interval_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-refresh-interval_locked:

      .. rst-class:: ansible-option-title

      **refresh-interval_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-refresh-interval_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'refresh\-interval' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-thousands"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-show-thousands:

      .. rst-class:: ansible-option-title

      **show-thousands**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-thousands" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show Thousands Separators

      Indicates whether thousands separators are shown in large numbers.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-thousands_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-show-thousands_locked:

      .. rst-class:: ansible-option-title

      **show-thousands_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-thousands_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-thousands' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-zeroes"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-show-zeroes:

      .. rst-class:: ansible-option-title

      **show-zeroes**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-zeroes" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show Trailing Zeroes

      Indicates whether any trailing zeroes after the numeric point should be shown in the display value.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-zeroes_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-show-zeroes_locked:

      .. rst-class:: ansible-option-title

      **show-zeroes_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-zeroes_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-zeroes' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-source-currency"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-source-currency:

      .. rst-class:: ansible-option-title

      **source-currency**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-source-currency" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Source currency

      Currency of the current calculation


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-source-currency_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-source-currency_locked:

      .. rst-class:: ansible-option-title

      **source-currency_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-source-currency_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'source\-currency' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-source-units"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-source-units:

      .. rst-class:: ansible-option-title

      **source-units**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-source-units" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Source units

      Units of the current calculation


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"degree"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-source-units_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-source-units_locked:

      .. rst-class:: ansible-option-title

      **source-units_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-source-units_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'source\-units' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-target-currency"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-target-currency:

      .. rst-class:: ansible-option-title

      **target-currency**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-target-currency" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Target currency

      Currency to convert the current calculation into


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-target-currency_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-target-currency_locked:

      .. rst-class:: ansible-option-title

      **target-currency_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-target-currency_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'target\-currency' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-target-units"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-target-units:

      .. rst-class:: ansible-option-title

      **target-units**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-target-units" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Target units

      Units to convert the current calculation into


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"radian"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-target-units_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-target-units_locked:

      .. rst-class:: ansible-option-title

      **target-units_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-target-units_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'target\-units' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-maximized"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-window-maximized:

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

      Window maximized

      Whether the last closed window was maximized.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-maximized_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-window-maximized_locked:

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
        <div class="ansibleOptionAnchor" id="parameter-window-position"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-window-position:

      .. rst-class:: ansible-option-title

      **window-position**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-position" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Window position

      Window position (x and y) of the last closed window.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"(\-1, \-1)"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-position_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-window-position_locked:

      .. rst-class:: ansible-option-title

      **window-position_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-position_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'window\-position' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-size"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-window-size:

      .. rst-class:: ansible-option-title

      **window-size**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-size" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Window size

      Window size (width and height) of the last closed window.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"(\-1, \-1)"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-window-size_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-window-size_locked:

      .. rst-class:: ansible-option-title

      **window-size_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-window-size_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'window\-size' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-word-size"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-word-size:

      .. rst-class:: ansible-option-title

      **word-size**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-word-size" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Word size

      The size of the words used in bitwise operations


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`64`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-word-size_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_calculator_module__parameter-word-size_locked:

      .. rst-class:: ansible-option-title

      **word-size_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-word-size_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'word\-size' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.calculator
      org_gnome_calculator:
        accuracy: 9
        accuracy_locked: true
        word-size: 64
        word-size_locked: true



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
