import json

with open("sample.json", "r") as file:
    data = json.load(file)

print("=" * 50)
print("JSON Data")
print("=" * 50)

print(f"Name       : {data['name']}")
print(f"Role       : {data['role']}")
print(f"Goal       : {data['goal']}")
print(f"Experience : {data['experience']} years")

print("\nSkills:")
for skill in data["skills"]:
    print(f"- {skill}")