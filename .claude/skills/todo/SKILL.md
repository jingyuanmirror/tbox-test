---
name: todo
description: Manage personal todo items with create, read, update, delete operations. Use when the user wants to manage their personal tasks, such as adding new todos ("add a todo to write documentation"), viewing their todo list ("show my todos"), marking tasks as complete ("complete todo 1"), updating task descriptions, deleting tasks, or clearing completed items. Stores todos locally in JSON format.
---

# Todo Manager

Manage personal todo items through a simple command-line interface with persistent local storage.

## Quick Start

The todo manager stores all tasks in `~/.claude_todos.json` and supports these operations:

**Add a new todo:**
```bash
python scripts/todo_manager.py add "Write documentation"
```

**List pending todos:**
```bash
python scripts/todo_manager.py list
```

**Complete a todo:**
```bash
python scripts/todo_manager.py complete 1
```

## Core Operations

### Add Todo

Add a new todo item with a description:

```bash
python scripts/todo_manager.py add <description>
```

**Examples:**
- `python scripts/todo_manager.py add "Review pull request"`
- `python scripts/todo_manager.py add "Fix bug in authentication"`
- `python scripts/todo_manager.py add "Update README with new features"`

The script automatically assigns a unique ID to each todo.

### List Todos

View all pending todos:

```bash
python scripts/todo_manager.py list
```

View all todos including completed ones:

```bash
python scripts/todo_manager.py list --all
```

Output format:
```
ID     Status       Description
------------------------------------------------------------
#1     ○ Pending    Write documentation
#2     ✓ Completed  Review pull request
```

### Complete Todo

Mark a todo as completed by its ID:

```bash
python scripts/todo_manager.py complete <id>
```

**Examples:**
- `python scripts/todo_manager.py complete 1`
- `python scripts/todo_manager.py complete 5`

### Update Todo

Update the description of an existing todo:

```bash
python scripts/todo_manager.py update <id> <new_description>
```

**Examples:**
- `python scripts/todo_manager.py update 1 "Write comprehensive documentation"`
- `python scripts/todo_manager.py update 3 "Fix critical bug in authentication"`

### Delete Todo

Permanently delete a todo by its ID:

```bash
python scripts/todo_manager.py delete <id>
```

**Examples:**
- `python scripts/todo_manager.py delete 1`
- `python scripts/todo_manager.py delete 7`

### Clear Completed

Remove all completed todos from the list:

```bash
python scripts/todo_manager.py clear
```

This helps keep the todo list clean by removing finished tasks.

## Usage Workflow

**Typical workflow when the user asks to manage todos:**

1. **Understand the request** - Identify what operation the user wants (add, list, complete, etc.)
2. **Run the appropriate command** - Execute the todo_manager.py script with the correct arguments
3. **Show the output** - Display the result to the user
4. **Confirm completion** - Verify the operation succeeded

**Example interaction patterns:**

| User Request | Action |
|-------------|--------|
| "Add a todo to write tests" | Run `add "Write tests"` |
| "Show my todos" / "What's on my todo list?" | Run `list` |
| "Mark todo 3 as done" / "Complete todo 3" | Run `complete 3` |
| "Delete todo 2" / "Remove todo 2" | Run `delete 2` |
| "Update todo 1 to say 'Write unit tests'" | Run `update 1 "Write unit tests"` |
| "Clean up my completed todos" | Run `clear` |

## Storage Details

- **Location**: `~/.claude_todos.json` in the user's home directory
- **Format**: JSON array of todo objects
- **Fields**:
  - `id`: Unique integer identifier
  - `description`: Text description of the todo
  - `completed`: Boolean status (true/false)
  - `created_at`: ISO timestamp of creation
  - `completed_at`: ISO timestamp when completed (if applicable)
  - `updated_at`: ISO timestamp of last update (if applicable)

## Error Handling

The script handles common errors gracefully:

- Missing todo file: Automatically creates a new one
- Invalid ID: Shows error message "Todo #X not found"
- Missing arguments: Shows usage information
- Invalid commands: Displays help text

Always check the script's output for confirmation messages (✅) or error indicators (❌).
