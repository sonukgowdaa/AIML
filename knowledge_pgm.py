class RuleBasedSystem:
    def __init__(self, facts, rules):
        self.facts = set(facts)
        self.rules = rules

    def forward_chain(self):
        while True:
            new_fact_added = False

            for rule in self.rules:
                # Check whether all conditions are present
                if all(condition in self.facts for condition in rule["if"]):

                    # Add conclusion if it is not already present
                    if rule["then"] not in self.facts:
                        print(
                            f"Rule Triggered: IF {rule['if']} "
                            f"THEN {rule['then']}"
                        )

                        self.facts.add(rule["then"])
                        new_fact_added = True

            if not new_fact_added:
                break

        return self.facts


# Main Program
if __name__ == "__main__":

    # Facts represented using predicate-like notation
    initial_facts = [
        "Human(Socrates)",
        "Mortal(Human)"
    ]

    # Rules represented as IF-THEN statements
    production_rules = [
        {
            "if": ["Human(Socrates)", "Mortal(Human)"],
            "then": "Mortal(Socrates)"
        }
    ]

    # Create Rule-Based System
    rbs = RuleBasedSystem(initial_facts, production_rules)

    print("Initial Facts:")
    for fact in initial_facts:
        print(fact)

    print("\nForward Chaining:")

    final_kb = rbs.forward_chain()

    print("\nFinal Knowledge Base:")
    for fact in final_kb:
        print(fact)