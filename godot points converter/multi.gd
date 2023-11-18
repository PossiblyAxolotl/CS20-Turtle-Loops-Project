extends Node2D

func _ready():
	var output = "["
	for child in get_children():
		if not child is Camera2D:
			output += "["
			for grandchild in child.get_children():
				output += '{"x":' + str(grandchild.global_position.x) + ', "y":' + str(-grandchild.global_position.y) + "},"
			output = output.erase(output.length()-1)
			output += "],"

	output = output.erase(output.length()-1)
	output += "]"
	
	print(output)
	DisplayServer.clipboard_set(output)
	print("Copied to clipboard")
	
	get_tree().quit()
