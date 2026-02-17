class OpenClawBridge:
    def run_task(self, task_name: str, *args):
        if task_name == "greet":
            return "Hello!"
        elif task_name == "farewell":
            name = args[0] if args else "friend"
            return f"Goodbye, {name}!"
        elif task_name == "add":
            return sum(args)
        else:
            return f"Unknown task: {task_name}"
