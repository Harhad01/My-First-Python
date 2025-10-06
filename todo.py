"""Simple JSON-backed CLI todo list
Usage examples:
  python todo.py add "Buy milk" -n "2 liters"
  python todo.py list
  python todo.py done 3
  python todo.py delete 2
  python todo.py edit 4 --title "New title" --notes "Updated notes"
  python todo.py export mytasks.json
  python todo.py import mytasks.json
"""
import argparse
import json
from pathlib import Path
from datetime import datetime
import sys

DATA_FILE = Path(__file__).with_name("todo.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def next_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


def cmd_add(args):
    tasks = load_tasks()
    tid = next_id(tasks)
    task = {
        "id": tid,
        "title": args.title,
        "notes": args.notes or "",
        "done": False,
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added [{tid}]: {args.title}")


def format_task(t):
    status = "x" if t.get("done") else " "
    return f"[{t['id']}] [{status}] {t['title']}" + (f" - {t.get('notes')}" if t.get("notes") else "")


def cmd_list(args):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    # filter
    if args.all:
        sel = tasks
    else:
        sel = [t for t in tasks if not t.get("done")]
    if not sel:
        print("No matching tasks.")
        return
    for t in sel:
        print(format_task(t))


def find_task(tasks, tid):
    for t in tasks:
        if t["id"] == tid:
            return t
    return None


def cmd_done(args):
    tasks = load_tasks()
    t = find_task(tasks, args.id)
    if not t:
        print("Task not found.")
        return
    t["done"] = True
    save_tasks(tasks)
    print(f"Marked [{t['id']}] done.")


def cmd_delete(args):
    tasks = load_tasks()
    t = find_task(tasks, args.id)
    if not t:
        print("Task not found.")
        return
    tasks = [x for x in tasks if x["id"] != args.id]
    save_tasks(tasks)
    print(f"Deleted [{args.id}].")


def cmd_edit(args):
    tasks = load_tasks()
    t = find_task(tasks, args.id)
    if not t:
        print("Task not found.")
        return
    changed = False
    if args.title:
        t["title"] = args.title
        changed = True
    if args.notes is not None:
        t["notes"] = args.notes
        changed = True
    if args.done is not None:
        t["done"] = bool(args.done)
        changed = True
    if changed:
        save_tasks(tasks)
        print(f"Updated [{t['id']}].")
    else:
        print("No changes provided.")


def cmd_clear(args):
    save_tasks([])
    print("Cleared all tasks.")


def cmd_export(args):
    tasks = load_tasks()
    target = Path(args.file)
    with target.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(tasks)} tasks to {target}")


def cmd_import(args):
    src = Path(args.file)
    if not src.exists():
        print("File not found.")
        return
    try:
        with src.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print("Failed to read file:", e)
        return
    if not isinstance(data, list):
        print("Import file must contain a JSON array of tasks.")
        return
    tasks = load_tasks()
    base = next_id(tasks)
    for i, item in enumerate(data):
        item_id = base + i
        item["id"] = item_id
        tasks.append(item)
    save_tasks(tasks)
    print(f"Imported {len(data)} tasks.")


def main(argv=None):
    parser = argparse.ArgumentParser(prog="todo", description="Simple JSON-backed todo list")
    sub = parser.add_subparsers(dest="cmd")

    p = sub.add_parser("add", help="Add a new task")
    p.add_argument("title", help="Task title")
    p.add_argument("-n", "--notes", help="Optional notes", default="")
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("list", help="List tasks")
    p.add_argument("-a", "--all", action="store_true", help="Show all tasks including done")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("done", help="Mark task done")
    p.add_argument("id", type=int, help="Task id")
    p.set_defaults(func=cmd_done)

    p = sub.add_parser("delete", help="Delete a task")
    p.add_argument("id", type=int, help="Task id")
    p.set_defaults(func=cmd_delete)

    p = sub.add_parser("edit", help="Edit a task")
    p.add_argument("id", type=int, help="Task id")
    p.add_argument("--title", help="New title")
    p.add_argument("--notes", help="New notes (use empty string to clear)")
    p.add_argument("--done", type=int, choices=[0,1], help="Set done flag; 1 for done, 0 for not done")
    p.set_defaults(func=cmd_edit)

    p = sub.add_parser("clear", help="Remove all tasks")
    p.set_defaults(func=cmd_clear)

    p = sub.add_parser("export", help="Export tasks to JSON file")
    p.add_argument("file", help="Target filename")
    p.set_defaults(func=cmd_export)

    p = sub.add_parser("import", help="Import tasks from JSON file")
    p.add_argument("file", help="Source filename")
    p.set_defaults(func=cmd_import)

    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 1
    try:
        args.func(args)
    except Exception as e:
        print("Error:", e)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
