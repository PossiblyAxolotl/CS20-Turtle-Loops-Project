extends Node2D

func _ready():
	var output = "["
	for child in get_children():
		if not child is Camera2D:
			output += '{"x":' + str(int(child.position.x)) + ', "y":' + str(int(-child.position.y)) + "},"
	
	output = output.erase(output.length()-1)
	output += "]"

	print(output)
	DisplayServer.clipboard_set(output)
	print("Copied to clipboard")

	get_tree().quit()
