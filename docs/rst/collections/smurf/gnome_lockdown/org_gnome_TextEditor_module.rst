.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module:

.. Anchors: short name for ansible.builtin

.. Title

smurf.gnome_lockdown.org_gnome_TextEditor module -- Manages GNOME GSettings for org.gnome.TextEditor
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `smurf.gnome_lockdown collection <https://galaxy.ansible.com/ui/repo/published/smurf/gnome_lockdown/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install smurf.gnome\_lockdown`.

    To use it in a playbook, specify: :code:`smurf.gnome_lockdown.org_gnome_TextEditor`.

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

- This module allows for the configuration of GSettings keys within the 'org.gnome.TextEditor' schema.
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
        <div class="ansibleOptionAnchor" id="parameter-auto-indent"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-auto-indent:

      .. rst-class:: ansible-option-title

      **auto-indent**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-indent" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Auto Indent

      Automatically indent new lines copying the previous line's indentation.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-indent_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-auto-indent_locked:

      .. rst-class:: ansible-option-title

      **auto-indent_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-indent_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'auto\-indent' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-save-delay"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-auto-save-delay:

      .. rst-class:: ansible-option-title

      **auto-save-delay**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-save-delay" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Auto Save Delay

      The delay in seconds to wait before auto\-saving a draft.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"3"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto-save-delay_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-auto-save-delay_locked:

      .. rst-class:: ansible-option-title

      **auto-save-delay_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto-save-delay_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'auto\-save\-delay' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-custom-font"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-custom-font:

      .. rst-class:: ansible-option-title

      **custom-font**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-custom-font" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Custom Font

      A custom font to use in the editor.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Monospace 11"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-custom-font_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-custom-font_locked:

      .. rst-class:: ansible-option-title

      **custom-font_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-custom-font_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'custom\-font' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-discover-settings"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-discover-settings:

      .. rst-class:: ansible-option-title

      **discover-settings**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-discover-settings" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Discover File Settings

      If enabled, then Text Editor will try to discover file settings from modelines, editorconfig, or per\-language defaults.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-discover-settings_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-discover-settings_locked:

      .. rst-class:: ansible-option-title

      **discover-settings_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-discover-settings_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'discover\-settings' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-draw-spaces"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-draw-spaces:

      .. rst-class:: ansible-option-title

      **draw-spaces**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-draw-spaces" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Draw Spaces

      The various types of spaces to draw in the editor.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"[]"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-draw-spaces_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-draw-spaces_locked:

      .. rst-class:: ansible-option-title

      **draw-spaces_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-draw-spaces_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'draw\-spaces' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable-snippets"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-enable-snippets:

      .. rst-class:: ansible-option-title

      **enable-snippets**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-snippets" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable Snippets

      Enable the use of snippets registered with GtkSourceView from within the editor.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable-snippets_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-enable-snippets_locked:

      .. rst-class:: ansible-option-title

      **enable-snippets_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable-snippets_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'enable\-snippets' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-highlight-current-line"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-highlight-current-line:

      .. rst-class:: ansible-option-title

      **highlight-current-line**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-highlight-current-line" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Highlight current line

      If enabled, the current line will be highlighted.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-highlight-current-line_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-highlight-current-line_locked:

      .. rst-class:: ansible-option-title

      **highlight-current-line_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-highlight-current-line_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'highlight\-current\-line' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-highlight-matching-brackets"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-highlight-matching-brackets:

      .. rst-class:: ansible-option-title

      **highlight-matching-brackets**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-highlight-matching-brackets" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Highlight Matching Brackets

      Highlight matching brackets and braces.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-highlight-matching-brackets_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-highlight-matching-brackets_locked:

      .. rst-class:: ansible-option-title

      **highlight-matching-brackets_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-highlight-matching-brackets_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'highlight\-matching\-brackets' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-indent-style"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-indent-style:

      .. rst-class:: ansible-option-title

      **indent-style**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-indent-style" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indentation Style

      Whether the editor should insert multiple spaces characters instead of tabs.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"tab"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-indent-style_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-indent-style_locked:

      .. rst-class:: ansible-option-title

      **indent-style_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-indent-style_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'indent\-style' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-indent-width"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-indent-width:

      .. rst-class:: ansible-option-title

      **indent-width**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-indent-width" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indent Width

      The number of spaces to indent or \-1 to use tab\-width.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`\-1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-indent-width_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-indent-width_locked:

      .. rst-class:: ansible-option-title

      **indent-width_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-indent-width_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'indent\-width' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-keybindings"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-keybindings:

      .. rst-class:: ansible-option-title

      **keybindings**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-keybindings" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Keybindings

      The keybindings to use within Text Editor.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"default"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-keybindings_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-keybindings_locked:

      .. rst-class:: ansible-option-title

      **keybindings_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-keybindings_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'keybindings' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-last-save-directory"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-last-save-directory:

      .. rst-class:: ansible-option-title

      **last-save-directory**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-last-save-directory" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Last Save Directory

      The directory last used in a save or save\-as dialog.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-last-save-directory_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-last-save-directory_locked:

      .. rst-class:: ansible-option-title

      **last-save-directory_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-last-save-directory_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'last\-save\-directory' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-line-height"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-line-height:

      .. rst-class:: ansible-option-title

      **line-height**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-line-height" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Line Height

      The line height to use for the selected font.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"1.2"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-line-height_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-line-height_locked:

      .. rst-class:: ansible-option-title

      **line-height_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-line-height_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'line\-height' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-recolor-window"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-recolor-window:

      .. rst-class:: ansible-option-title

      **recolor-window**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-recolor-window" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Recolor Window

      Use the style\-scheme to recolor the application window.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-recolor-window_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-recolor-window_locked:

      .. rst-class:: ansible-option-title

      **recolor-window_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-recolor-window_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'recolor\-window' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-restore-session"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-restore-session:

      .. rst-class:: ansible-option-title

      **restore-session**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-restore-session" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Restore session

      When Text Editor is running, restore the previous session.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-restore-session_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-restore-session_locked:

      .. rst-class:: ansible-option-title

      **restore-session_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-restore-session_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'restore\-session' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-right-margin-position"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-right-margin-position:

      .. rst-class:: ansible-option-title

      **right-margin-position**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-right-margin-position" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Right Margin Position

      The position in characters at which the right margin should be displayed.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"80"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-right-margin-position_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-right-margin-position_locked:

      .. rst-class:: ansible-option-title

      **right-margin-position_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-right-margin-position_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'right\-margin\-position' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-grid"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-show-grid:

      .. rst-class:: ansible-option-title

      **show-grid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-grid" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show Background Grid

      If enabled, a blueprint style grid is printed on the editor background.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-grid_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-show-grid_locked:

      .. rst-class:: ansible-option-title

      **show-grid_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-grid_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-grid' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-line-numbers"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-show-line-numbers:

      .. rst-class:: ansible-option-title

      **show-line-numbers**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-line-numbers" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show Line Numbers

      Whether line numbers should be displayed next to each line.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-line-numbers_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-show-line-numbers_locked:

      .. rst-class:: ansible-option-title

      **show-line-numbers_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-line-numbers_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-line\-numbers' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-map"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-show-map:

      .. rst-class:: ansible-option-title

      **show-map**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-map" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show Overview Map

      If enabled, an overview map of the file will be displayed to the side of the editor.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-map_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-show-map_locked:

      .. rst-class:: ansible-option-title

      **show-map_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-map_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-map' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-right-margin"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-show-right-margin:

      .. rst-class:: ansible-option-title

      **show-right-margin**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-right-margin" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Show Right Margin

      Whether a margin line should be displayed on the right of the editor.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-show-right-margin_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-show-right-margin_locked:

      .. rst-class:: ansible-option-title

      **show-right-margin_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-show-right-margin_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'show\-right\-margin' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-spellcheck"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-spellcheck:

      .. rst-class:: ansible-option-title

      **spellcheck**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-spellcheck" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Automatically check spelling

      If enabled, then Text Editor will check spelling as you type.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-spellcheck_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-spellcheck_locked:

      .. rst-class:: ansible-option-title

      **spellcheck_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-spellcheck_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'spellcheck' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-style-scheme"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-style-scheme:

      .. rst-class:: ansible-option-title

      **style-scheme**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-style-scheme" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Style Scheme

      The style scheme to use by the editor. It may translate this into a dark format when available.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"Adwaita"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-style-scheme_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-style-scheme_locked:

      .. rst-class:: ansible-option-title

      **style-scheme_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-style-scheme_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'style\-scheme' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-style-variant"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-style-variant:

      .. rst-class:: ansible-option-title

      **style-variant**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-style-variant" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Style Variant

      Use the light or dark variant of the GTK theme and/or GtkSourceView style scheme.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"follow"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-style-variant_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-style-variant_locked:

      .. rst-class:: ansible-option-title

      **style-variant_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-style-variant_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'style\-variant' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tab-width"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-tab-width:

      .. rst-class:: ansible-option-title

      **tab-width**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tab-width" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Tab Width

      The number of spaces represented by a tab.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"8"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tab-width_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-tab-width_locked:

      .. rst-class:: ansible-option-title

      **tab-width_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tab-width_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'tab\-width' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-use-system-font"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-use-system-font:

      .. rst-class:: ansible-option-title

      **use-system-font**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-use-system-font" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use System Font

      Whether the default system monospace font should be used.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-use-system-font_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-use-system-font_locked:

      .. rst-class:: ansible-option-title

      **use-system-font_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-use-system-font_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'use\-system\-font' key to prevent user modification.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrap-text"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-wrap-text:

      .. rst-class:: ansible-option-title

      **wrap-text**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrap-text" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Text Wrapping

      Whether text should be wrapped.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wrap-text_locked"></div>

      .. _ansible_collections.smurf.gnome_lockdown.org_gnome_TextEditor_module__parameter-wrap-text_locked:

      .. rst-class:: ansible-option-title

      **wrap-text_locked**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wrap-text_locked" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If set to true, locks the 'wrap\-text' key to prevent user modification.


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

    - name: Configure and lock GNOME desktop settings for org.gnome.TextEditor
      org_gnome_TextEditor:
        auto-save-delay: 3
        auto-save-delay_locked: true
        style-variant: "follow"
        style-variant_locked: true



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
