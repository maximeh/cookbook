from pathlib import Path

ROOT_DIR = Path("recipes")
OUTPUT_FILE = "recipes.md"


def get_category_name(category_name):
    category_mapping = {
        "drinks": "🍹 Drinks",
        "main": "🍝 Main Dishes",
        "sides": "🥗 Sides",
        "snack": "🥨 Snacks",
        "snack/cookies": "🍪 Cookies",
        "dessert": "🍰 Desserts",
    }
    for category, category_title in category_mapping.items():
        if category == category_name:
            return category_title
    return "📜 Other"


def generate_recipes_md():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Recipes\n\n")
        for category in sorted(ROOT_DIR.rglob("*"), key=lambda x: x.stem):
            if not category.is_dir():
                continue
            category_name = category.relative_to(ROOT_DIR)
            category_title = get_category_name(str(category_name))
            f.write(f"## {category_title}\n\n")
            for recipe in sorted(category.rglob("*.md")):
                recipe_name = recipe.stem.replace("_", " ").title()
                recipe_path = category_name / recipe.stem
                f.write(f"- [{recipe_name}](/cookbook/?recipe={recipe_path})\n")
            f.write("\n")


generate_recipes_md()
print(f"The file '{OUTPUT_FILE}' has been successfully generated.")
