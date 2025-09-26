local wezterm = require 'wezterm'

return {
  enable_tab_bar = false,
  window_close_confirmation = "NeverPrompt",

  font = wezterm.font_with_fallback({
    "Consolas",
    "JetBrains Mono",
    "Ubuntu Mono",
    "monospace",
  }),
  font_size = 12.0,

  default_cursor_style = 'BlinkingBlock',
  cursor_blink_rate = 0, -- 0 = курсор не мигает

  colors = {
    foreground = "#828282",
    background = "#2e3436",

    cursor_bg = "#ffffff",
    cursor_fg = "#2e3436",
    cursor_border = "#ffffff",

    ansi = {
      "#000000", -- black
      "#b43330", -- red
      "#778809", -- green
      "#c4a000", -- yellow
      "#5a5bf9", -- blue
      "#75507b", -- magenta
      "#06989a", -- cyan
      "#d3d7cf", -- white
    },
    brights = {
      "#555753", -- bright black
      "#b43330", -- bright red
      "#778809", -- bright green
      "#edd400", -- bright yellow
      "#5a5bf9", -- bright blue
      "#ad7fa8", -- bright magenta
      "#34e2e2", -- bright cyan
      "#eeeeec", -- bright white
    },
  },
  window_padding = {
    left = 0,
    right = 0,
    top = 0,
    bottom = 0,
  },
  scrollback_lines = 5000,

  keys = {
    -- построчный скролл
    { key = "q", mods = "CTRL|SHIFT", action = wezterm.action.ScrollByLine(-1) },
    { key = "a", mods = "CTRL|SHIFT", action = wezterm.action.ScrollByLine(1) },

    -- постраничный скролл
    { key = "q", mods = "CTRL", action = wezterm.action.ScrollByPage(-1) },
    { key = "a", mods = "CTRL", action = wezterm.action.ScrollByPage(1) },

    -- полноэкранный режим
    { key = "F11", action = wezterm.action.ToggleFullScreen },

    -- Перемещение по словам (Alt+F / Alt+B)
    { key="u", mods="ALT", action=wezterm.action.SendKey{key="LeftArrow", mods="CTRL"} },
    { key="o", mods="ALT", action=wezterm.action.SendKey{key="RightArrow", mods="CTRL"} },

    -- Перемещение курсора
    {key="q", mods="ALT", action=wezterm.action.SendString("\x01")},  -- Ctrl+A → начало строки
    {key="a", mods="ALT", action=wezterm.action.SendString("\x05")},  -- Ctrl+E → конец строки

    -- Удаление всей строки независимо от позиции курсора (Ctrl+Shift+D)
    {key="d", mods="CTRL|SHIFT", action=wezterm.action.SendString("\x01\x0b")}, -- Ctrl+A + Ctrl+K

    -- История команд
    {key="i", mods="ALT", action=wezterm.action.SendKey{key="UpArrow"}},  -- Alt+I → previous-history
    {key="k", mods="ALT", action=wezterm.action.SendKey{key="DownArrow"}},  -- Alt+K → next-history

    -- Пример своих быстрых вставок
    {key="s", mods="ALT", action=wezterm.action.SendString("\x01sudo \x05")},      -- Alt+S → вставить "sudo " и поставить курсор в конец
    {key="p", mods="ALT", action=wezterm.action.SendString("\x01pacman -\x05")},   -- Alt+P → вставить "pacman -" и курсор в конец
  },
}
