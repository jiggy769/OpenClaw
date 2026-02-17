from openclaw_bridge import OpenClawBridge

oc = OpenClawBridge()

print(oc.run_task("greet"))
print(oc.run_task("farewell", "Theresa"))
print(oc.run_task("add", 12, 8))
print(oc.run_task("unknown"))

