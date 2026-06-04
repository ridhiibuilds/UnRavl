# UnRavl — Upcycle Suggestions Database
# Ridhi Garg | June 2 2026
# Base of UnRavl
# Every garment type and its transformation possibilities

UPCYCLE_SUGGESTIONS = {
    "tshirt": {
        "transformations": [
            {
                "name": "Crop Top",
                "description": "Cut the hem to crop length, raw edge or hemmed",
                "difficulty": "easy",
                "tools": ["scissors"],
                "vibe": ["casual", "Y2K", "minimal"]
            },
            {
                "name": "Off Shoulder Top",
                "description": "Cut the neckline wide, elastic through the hem",
                "difficulty": "easy",
                "tools": ["scissors", "elastic", "needle", "thread"],
                "vibe": ["feminine", "casual", "summer"]
            },
            {
                "name": "Backless Top",
                "description": "Cut the back open, add ties or lace detail",
                "difficulty": "medium",
                "tools": ["scissors", "needle", "thread"],
                "vibe": ["edgy", "going out", "Y2K"]
            },
            {
                "name": "Corset Style",
                "description": "Add ribbon lacing down the back or front",
                "difficulty": "medium",
                "tools": ["scissors", "ribbon", "needle", "thread"],
                "vibe": ["dark feminine", "edgy", "going out"]
            },
            {
                "name": "Bleach Dye",
                "description": "Bleach pattern for a distressed editorial look",
                "difficulty": "easy",
                "tools": ["bleach", "gloves", "water"],
                "vibe": ["edgy", "grunge", "streetwear"]
            }
        ]
    },
    "jeans": {
        "transformations": [
            {
                "name": "Shorts",
                "description": "Cut at desired length, distress the hem",
                "difficulty": "easy",
                "tools": ["scissors"],
                "vibe": ["casual", "summer", "streetwear"]
            },
            {
                "name": "Distressed",
                "description": "Slash knees and thighs for a worn look",
                "difficulty": "easy",
                "tools": ["scissors", "sandpaper"],
                "vibe": ["grunge", "casual", "streetwear"]
            },
            {
                "name": "Embroidered",
                "description": "Add floral or graphic embroidery on pockets or hem",
                "difficulty": "hard",
                "tools": ["embroidery needle", "thread", "hoop"],
                "vibe": ["bohemian", "vintage", "feminine"]
            },
            {
                "name": "Patchwork",
                "description": "Add fabric patches over rips or as design detail",
                "difficulty": "medium",
                "tools": ["fabric scraps", "needle", "thread"],
                "vibe": ["Y2K", "vintage", "bohemian"]
            }
        ]
    },
    "dress": {
        "transformations": [
            {
                "name": "Mini Skirt",
                "description": "Cut the top off, add elastic waistband",
                "difficulty": "medium",
                "tools": ["scissors", "elastic", "needle", "thread"],
                "vibe": ["feminine", "going out", "Y2K"]
            },
            {
                "name": "Two Piece",
                "description": "Cut into crop top and skirt set",
                "difficulty": "medium",
                "tools": ["scissors", "needle", "thread"],
                "vibe": ["going out", "summer", "feminine"]
            },
            {
                "name": "Shorter Hem",
                "description": "Cut and hem to a shorter length",
                "difficulty": "easy",
                "tools": ["scissors", "needle", "thread"],
                "vibe": ["casual", "feminine", "minimal"]
            }
        ]
    },
    "jacket": {
        "transformations": [
            {
                "name": "Cropped Jacket",
                "description": "Cut the body shorter for a cropped silhouette",
                "difficulty": "medium",
                "tools": ["scissors", "needle", "thread"],
                "vibe": ["streetwear", "Y2K", "edgy"]
            },
            {
                "name": "Sleeveless Vest",
                "description": "Remove the sleeves completely",
                "difficulty": "easy",
                "tools": ["scissors", "needle", "thread"],
                "vibe": ["casual", "streetwear", "minimal"]
            },
            {
                "name": "Painted Jacket",
                "description": "Add fabric paint design on the back",
                "difficulty": "medium",
                "tools": ["fabric paint", "brushes"],
                "vibe": ["streetwear", "artistic", "edgy"]
            }
        ]
    }
}


def get_suggestions(garment_type):
    """
    Takes a garment type and returns all transformation ideas
    """
    garment_type = garment_type.lower()
    
    if garment_type in UPCYCLE_SUGGESTIONS:
        return UPCYCLE_SUGGESTIONS[garment_type]["transformations"]
    else:
        return print("no such garment found")


def get_suggestions_by_vibe(garment_type, vibe):
    """
    Filters suggestions by aesthetic vibe
    """
    all_suggestions = get_suggestions(garment_type)
    
    filtered = []
    for suggestion in all_suggestions:
        if vibe.lower() in suggestion["vibe"]:
            filtered.append(suggestion)
    
    return filtered


def get_easy_suggestions(garment_type):
    """
    Returns only easy transformations
    Perfect for beginners
    """
    all_suggestions = get_suggestions(garment_type)
    
    easy = []
    for suggestion in all_suggestions:
        if suggestion["difficulty"] == "easy":
            easy.append(suggestion)
    
    return easy


# TEST — run this file to see it working
if __name__ == "__main__":
    
    print("=== Testing UnRavl Suggestions Database ===\n")
    
    # Test 1 — get all tshirt suggestions
    print("All tshirt transformations:")
    tshirt_ideas = get_suggestions("tshirt")
    for idea in tshirt_ideas:
        print(f"  → {idea['name']} ({idea['difficulty']})")
    
    print()
    
    # Test 2 — filter by vibe
    print("Edgy tshirt transformations:")
    edgy_ideas = get_suggestions_by_vibe("tshirt", "edgy")
    for idea in edgy_ideas:
        print(f"  → {idea['name']}")
    
    print()
    
    # Test 3 — easy only
    print("Easy jeans transformations:")
    easy_jeans = get_easy_suggestions("jeans")
    for idea in easy_jeans:
        print(f"  → {idea['name']} — tools: {idea['tools']}")