from mde.core import MDE

def main():
    mde = MDE()
    # a single cycle with sample perception
    perception = {
        "text": "large replication set",
        "physical": {"items": 2, "sets": 2},
        "social": {"trust": 0.7},
    }
    result = mde.run_cycle(perception)
    print("\nSemantic summary:")
    print(" ", result["semantic_summary"])
    
    print("\nSemantic rules:")
    for rule in result["semantic_rules"]:
        print("  -" + rule)

if __name__ == "__main__":
    main()