#!/usr/bin/env python3
"""
Todo Manager - Simple command-line todo list manager
Stores todos in a JSON file in the user's home directory
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

# Default location for todos file
TODOS_FILE = Path.home() / ".claude_todos.json"


def load_todos() -> List[Dict]:
    """Load todos from the JSON file"""
    if not TODOS_FILE.exists():
        return []

    try:
        with open(TODOS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_todos(todos: List[Dict]) -> None:
    """Save todos to the JSON file"""
    with open(TODOS_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def add_todo(description: str) -> None:
    """Add a new todo item"""
    todos = load_todos()

    # Find the next available ID
    next_id = max([todo.get('id', 0) for todo in todos], default=0) + 1

    new_todo = {
        'id': next_id,
        'description': description,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }

    todos.append(new_todo)
    save_todos(todos)

    print(f"✅ Added todo #{next_id}: {description}")


def list_todos(show_completed: bool = False) -> None:
    """List all todos"""
    todos = load_todos()

    if not todos:
        print("No todos found. Add one with: add <description>")
        return

    # Filter completed if needed
    if not show_completed:
        todos = [t for t in todos if not t.get('completed', False)]

    if not todos:
        print("No pending todos! 🎉")
        return

    print(f"\n{'ID':<6} {'Status':<12} {'Description'}")
    print("-" * 60)

    for todo in todos:
        status = "✓ Completed" if todo.get('completed', False) else "○ Pending"
        print(f"#{todo['id']:<5} {status:<12} {todo['description']}")

    print()


def complete_todo(todo_id: int) -> None:
    """Mark a todo as completed"""
    todos = load_todos()

    for todo in todos:
        if todo['id'] == todo_id:
            if todo.get('completed', False):
                print(f"Todo #{todo_id} is already completed")
            else:
                todo['completed'] = True
                todo['completed_at'] = datetime.now().isoformat()
                save_todos(todos)
                print(f"✅ Completed todo #{todo_id}: {todo['description']}")
            return

    print(f"❌ Todo #{todo_id} not found")


def delete_todo(todo_id: int) -> None:
    """Delete a todo item"""
    todos = load_todos()

    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            description = todo['description']
            del todos[i]
            save_todos(todos)
            print(f"🗑️  Deleted todo #{todo_id}: {description}")
            return

    print(f"❌ Todo #{todo_id} not found")


def update_todo(todo_id: int, new_description: str) -> None:
    """Update a todo's description"""
    todos = load_todos()

    for todo in todos:
        if todo['id'] == todo_id:
            old_description = todo['description']
            todo['description'] = new_description
            todo['updated_at'] = datetime.now().isoformat()
            save_todos(todos)
            print(f"✏️  Updated todo #{todo_id}")
            print(f"   Old: {old_description}")
            print(f"   New: {new_description}")
            return

    print(f"❌ Todo #{todo_id} not found")


def clear_completed() -> None:
    """Remove all completed todos"""
    todos = load_todos()
    completed_count = sum(1 for t in todos if t.get('completed', False))

    if completed_count == 0:
        print("No completed todos to clear")
        return

    todos = [t for t in todos if not t.get('completed', False)]
    save_todos(todos)
    print(f"🗑️  Cleared {completed_count} completed todo(s)")


def show_usage() -> None:
    """Display usage information"""
    print("""
Todo Manager - Simple command-line todo list

Usage:
  python todo_manager.py add <description>        Add a new todo
  python todo_manager.py list [--all]             List todos (--all shows completed)
  python todo_manager.py complete <id>            Mark todo as completed
  python todo_manager.py delete <id>              Delete a todo
  python todo_manager.py update <id> <description> Update todo description
  python todo_manager.py clear                    Clear all completed todos

Examples:
  python todo_manager.py add "Write documentation"
  python todo_manager.py list
  python todo_manager.py complete 1
  python todo_manager.py delete 2
  python todo_manager.py update 3 "Write better documentation"
  python todo_manager.py clear
""")


def main():
    if len(sys.argv) < 2:
        show_usage()
        return

    command = sys.argv[1].lower()

    if command == 'add':
        if len(sys.argv) < 3:
            print("❌ Error: Please provide a description")
            print("Usage: python todo_manager.py add <description>")
            return
        description = ' '.join(sys.argv[2:])
        add_todo(description)

    elif command == 'list':
        show_all = '--all' in sys.argv or '-a' in sys.argv
        list_todos(show_completed=show_all)

    elif command == 'complete':
        if len(sys.argv) < 3:
            print("❌ Error: Please provide a todo ID")
            print("Usage: python todo_manager.py complete <id>")
            return
        try:
            todo_id = int(sys.argv[2])
            complete_todo(todo_id)
        except ValueError:
            print("❌ Error: ID must be a number")

    elif command == 'delete':
        if len(sys.argv) < 3:
            print("❌ Error: Please provide a todo ID")
            print("Usage: python todo_manager.py delete <id>")
            return
        try:
            todo_id = int(sys.argv[2])
            delete_todo(todo_id)
        except ValueError:
            print("❌ Error: ID must be a number")

    elif command == 'update':
        if len(sys.argv) < 4:
            print("❌ Error: Please provide a todo ID and new description")
            print("Usage: python todo_manager.py update <id> <description>")
            return
        try:
            todo_id = int(sys.argv[2])
            new_description = ' '.join(sys.argv[3:])
            update_todo(todo_id, new_description)
        except ValueError:
            print("❌ Error: ID must be a number")

    elif command == 'clear':
        clear_completed()

    else:
        print(f"❌ Unknown command: {command}")
        show_usage()


if __name__ == '__main__':
    main()
