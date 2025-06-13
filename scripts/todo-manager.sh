#!/usr/bin/env bash
# todo-manager.sh: Simple CLI for managing a TODO list in a plaintext file
# Usage:
#   ./todo-manager.sh add "Buy groceries"
#   ./todo-manager.sh list
#   ./todo-manager.sh done 2
#   ./todo-manager.sh help

set -euo pipefail
IFS=$'\n\t'

# Default storage directory and file (can be overridden with TODO_DIR env var)
TODO_DIR="${TODO_DIR:-$HOME/.todo-manager}"
TODO_FILE="$TODO_DIR/todo.txt"

# Ensure storage directory and file exist
mkdir -p "$TODO_DIR"
touch "$TODO_FILE"

show_help() {
  cat <<EOF
Usage: $0 COMMAND [ARGS]

Commands:
  add "TASK DESCRIPTION"   Add a new task
  list                      List all tasks
  done INDEX                Mark task at INDEX as completed
  help                      Show this help message

Examples:
  $0 add "Write blog post"
  $0 list
  $0 done 3
EOF
}

add_task() {
  local desc="$1"
  # Prefix incomplete tasks with [ ]
  echo "[ ] $desc" >> "$TODO_FILE"
  echo "Added: $desc"
}

list_tasks() {
  if [[ ! -s "$TODO_FILE" ]]; then
    echo "No tasks found."
    return
  fi

  local i=1
  while IFS= read -r line; do
    # line format: "[ ] description" or "[x] description"
    local status="${line:1:1}"
    local desc="${line:4}"
    if [[ "$status" == "x" ]]; then
      printf "%2d. \e[32m[x]\e[0m %s\n" "$i" "$desc"
    else
      printf "%2d. \e[33m[ ]\e[0m %s\n" "$i" "$desc"
    fi
    ((i++))
  done < "$TODO_FILE"
}

mark_done() {
  local idx="$1"
  if ! sed -n "${idx}p" "$TODO_FILE" &>/dev/null; then
    echo "Invalid index: $idx" >&2
    exit 1
  fi

  # Replace leading [ ] with [x] on the specified line
  sed -i "${idx}s/^\[ \]/[x]/" "$TODO_FILE"
  echo "Marked task #$idx as done."
}

# Main dispatch
action="${1:-help}"
case "$action" in
  add)
    [[ $# -ge 2 ]] || { echo "Error: Missing task description." >&2; show_help; exit 1; }
    add_task "$2"
    ;;

  list)
    list_tasks
    ;;

  done)
    [[ $# -ge 2 ]] || { echo "Error: Missing task index." >&2; show_help; exit 1; }
    mark_done "$2"
    ;;

  help|--help|-h)
    show_help
    ;;

  *)
    echo "Unknown command: $action" >&2
    show_help
    exit 1
    ;;

esac
