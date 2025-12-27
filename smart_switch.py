#!/usr/bin/env python3
import i3ipc
import sys
import os

def get_focused_output(i3):
    tree = i3.get_tree()
    focused = tree.find_focused()
    workspace = focused.workspace()
    if workspace:
        return workspace.ipc_data['output']
    for output in i3.get_outputs():
        if output.active:
            for ws in i3.get_workspaces():
                if ws.focused and ws.output == output.name:
                    return output.name
    return None

def get_monitor_index(output_name, outputs):
    output_names = [o.name for o in outputs if o.active]
    try:
        return output_names.index(output_name)
    except ValueError:
        return 0

def switch_workspace(workspace_num):
    try:
        i3 = i3ipc.Connection()
        
        focused_output = get_focused_output(i3)
        if not focused_output:
            return
        
        outputs = i3.get_outputs()
        
        monitor_index = get_monitor_index(focused_output, outputs)
        actual_workspace = workspace_num + (monitor_index * 10)
        
        i3.command(f'workspace number {actual_workspace}')
        i3.main_quit()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def move_to_workspace(workspace_num):
    try:
        i3 = i3ipc.Connection()
        
        focused_output = get_focused_output(i3)
        if not focused_output:
            return
        
        outputs = i3.get_outputs()
        
        monitor_index = get_monitor_index(focused_output, outputs)
        
        actual_workspace = workspace_num + (monitor_index * 10)
        
        i3.command(f'move container to workspace number {actual_workspace}')
        i3.main_quit()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: script.py [switch|move] <workspace_number>")
        sys.exit(1)
    
    action = sys.argv[1]
    workspace_num = int(sys.argv[2])
    
    if action == 'switch':
        switch_workspace(workspace_num)
    elif action == 'move':
        move_to_workspace(workspace_num)
    else:
        print("Action must be 'switch' or 'move'")
        sys.exit(1)