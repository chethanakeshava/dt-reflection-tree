import json
import sys
import os
import re

# Load the tree from Part A
def load_tree(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Create a dictionary for instant node lookup
            return {node['id']: node for node in data['nodes']}, data.get('meta', {})
    except Exception as e:
        print(f"Error loading tree: {e}")
        sys.exit(1)

def get_dominant(state, axis):
    """Calculates which side of the axis the user leaned toward."""
    if axis == "axis1":
        return "internal" if state["signals"].get("axis1:internal", 0) >= state["signals"].get("axis1:external", 0) else "external"
    elif axis == "axis2":
        return "contribution" if state["signals"].get("axis2:contribution", 0) >= state["signals"].get("axis2:entitlement", 0) else "entitlement"
    elif axis == "axis3":
        return "wide" if state["signals"].get("axis3:wide", 0) >= state["signals"].get("axis3:self", 0) else "self"
    return ""

def interpolate_text(text, state, templates=None):
    """Replaces placeholders like {A0_OPEN.answer} or {axis1.dominant} with actual state data."""
    if not text: return ""
    
    # Replace previous answers
    matches = re.findall(r'\{([A-Za-z0-9_]+)\.answer\}', text)
    for match in matches:
        answer = state["answers"].get(match, "")
        text = text.replace(f"{{{match}.answer}}", answer)
        
    # Replace summary template logic
    if templates:
        for axis in ["axis1", "axis2", "axis3"]:
            dom = get_dominant(state, axis)
            text = text.replace(f"{{{axis}.dominant}}", dom)
            if dom in templates.get(axis, {}):
                text = text.replace(f"{{{axis}.summary}}", templates[axis][dom])
                
        # Closing reflection combination
        combo_key = f"{get_dominant(state, 'axis1')}_{get_dominant(state, 'axis2')}_{get_dominant(state, 'axis3')}"
        if combo_key in templates.get("closingReflections", {}):
            text = text.replace("{closing_reflection}", templates["closingReflections"][combo_key])
            
    return text

def run_agent():
    # Make sure we are reading from the correct directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tree_path = os.path.join(base_dir, 'tree', 'reflection-tree.json')
    
    nodes, meta = load_tree(tree_path)
    
    state = {
        "answers": {},
        "signals": {}
    }
    
    current_node_id = "START"
    print(f"\n=== {meta.get('title', 'Reflection Tool')} ===\n")
    
    while current_node_id:
        node = nodes.get(current_node_id)
        if not node:
            break
            
        node_type = node.get("type")
        
        # 1. Handle Questions
        if node_type == "question":
            text = interpolate_text(node.get("text", ""), state)
            print(f"\n{text}")
            options = node.get("options", [])
            for i, opt in enumerate(options):
                print(f"  {i+1}. {opt}")
                
            while True:
                try:
                    choice = int(input("\nSelect an option (1-4): ")) - 1
                    if 0 <= choice < len(options):
                        selected_answer = options[choice]
                        state["answers"][current_node_id] = selected_answer
                        break
                    print("Invalid choice. Try again.")
                except ValueError:
                    print("Please enter a number.")
            
            # Process signals attached to the node itself
            signal = node.get("signal")
            if signal:
                state["signals"][signal] = state["signals"].get(signal, 0) + 1
                
            current_node_id = node.get("next")

        # 2. Handle Decisions (Routing logic)
        elif node_type == "decision":
            rules = node.get("rules", [])
            next_node = None
            
            for rule in rules:
                # Match based on parent question's answer
                if "match" in rule:
                    parent_answer = state["answers"].get(node["parentId"])
                    if parent_answer in rule["match"]:
                        next_node = rule["next"]
                        if "signal" in rule:
                            state["signals"][rule["signal"]] = state["signals"].get(rule["signal"], 0) + 1
                        break
                # Match based on dominant axis condition
                elif "condition" in rule:
                    condition = rule["condition"]
                    axis = condition.split(".")[0]
                    expected_dom = condition.split("'")[1]
                    if get_dominant(state, axis) == expected_dom:
                        next_node = rule["next"]
                        break
            
            current_node_id = next_node or node.get("next")

        # 3. Handle Reflections & Bridges
        elif node_type in ["reflection", "bridge"]:
            text = interpolate_text(node.get("text", ""), state)
            print(f"\n--- {text} ---")
            
            signal = node.get("signal")
            if signal:
                state["signals"][signal] = state["signals"].get(signal, 0) + 1
                
            if node_type == "reflection":
                input("\n[Press Enter to continue...]")
            current_node_id = node.get("next")
            
        # 4. Handle Summary & End
        elif node_type == "summary":
            text = interpolate_text(node.get("text", ""), state, node.get("summaryTemplates"))
            print("\n===============================")
            print(text)
            print("===============================\n")
            current_node_id = node.get("next")
            
        elif node_type in ["start", "end"]:
            if node.get("text"):
                print(f"\n{node.get('text')}")
            current_node_id = node.get("next")

if __name__ == "__main__":
    run_agent()