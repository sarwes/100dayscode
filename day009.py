level_10_code = """while (notDone()) {
  if (isPathRight()) {
    turnRight();
    moveForward();
  } else {
    if (isPathForward()) {
      moveForward();
    } else {
      if (isPathLeft()) {
        turnLeft();
        moveForward();
      } else {
        turnRight();
      }
    }
  }
} """




# Transfer the value from Level 10 "blocks remaining"
# to the variable below 

remaining_blocks = 0


print("JavaScript code for Level 10")
print(level_10_code)

print("Number of blocks remaining", remaining_blocks)
