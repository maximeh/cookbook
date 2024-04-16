import os

ROOT_DIR = "recipes"
OUTPUT_FILE = "recipes.md"


def get_category_name(category_path):
    category_mapping = {
        "drinks": "🍹 Drinks",
        "main": "🍝 Main Dishes",
        "sides": "🥗 Sides",
        "snack": "🥨 Snacks",
        "snack/cookies": "🍪 Cookies",
        "dessert": "🍰 Desserts",
    }
    for category, category_name in category_mapping.items():
        if category == category_path:
            return category_name
    return "📜 Other"


def generate_recipes_md():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Recipes\n\n")
        for root, _, files in os.walk(ROOT_DIR):
            relative_dir = os.path.relpath(root, ROOT_DIR)
            if files:
                category_name = get_category_name(relative_dir)
                f.write(f"## {category_name}\n\n")
                for file in files:
                    if file.endswith(".md"):
                        recipe_name = file[:-3].replace("_", " ").title()
                        recipe_path = os.path.join(relative_dir, file[:-3])
                        f.write(f"- [{recipe_name}](/cookbook/?recipe={recipe_path})\n")
                f.write("\n")


generate_recipes_md()
print(f"The file '{OUTPUT_FILE}' has been successfully generated.")
