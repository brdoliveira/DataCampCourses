world = {
    "afghanistan":30.55,
    "albania":2.77,
    "algeria":39.21}

print(world)
print("*" * 30)

# Add sealand
world["sealand"] = 0.000027
print(world)
print("*" * 30)

print("sealand" in world)
print("*" * 30)

# Remove sealand
del(world["sealand"])
print(world)