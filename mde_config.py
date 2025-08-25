# mde_config.py
# Configuration and constants for the Moral Decision Engine (MDE)

# Canonical States
DESIRED_STATE = "DS"
UNDESIRED_STATE = "US"
ADAPTIVE_STATE = "AS"
TRANSCENDENT_STATE = "TS"

CANONICAL_STATES = [DESIRED_STATE, UNDESIRED_STATE, ADAPTIVE_STATE, TRANSCENDENT_STATE]

# Canonical Models
WORLD_MODEL = "World"
CONSCIENCE_MODEL = "Conscience"
SOCIAL_MODEL = "Social"
COVENANT_MODEL = "Covenant"

CANONICAL_MODELS = [WORLD_MODEL, CONSCIENCE_MODEL, SOCIAL_MODEL, COVENANT_MODEL]

# Canonical Layers (Cognitive Pipeline)
REACTIVE_LAYER = "Reactive"
PERCEPTUAL_REFLECTIVE_LAYER = "Perceptual-Reflective"
ASPIRATIONAL_LAYER = "Aspirational"
INTEGRATIVE_LAYER = "Integrative"
STATE_EVALUATION_LAYER = "State Evaluation"
TRANSFORMATIVE_LAYER = "Transformative"
GOVERNANCE_LAYER = "Governance"
OUTPUT_LAYER = "Output"

COGNITIVE_LAYERS = [
    REACTIVE_LAYER,
        PERCEPTUAL_REFLECTIVE_LAYER,
            ASPIRATIONAL_LAYER,
                INTEGRATIVE_LAYER,
                    STATE_EVALUATION_LAYER,
                        TRANSFORMATIVE_LAYER,
                            GOVERNANCE_LAYER,
                                OUTPUT_LAYER
                                ]

                                # A list of the core layers that process moralities (i.e., excluding Output)
                                MORALITY_LAYERS = COGNITIVE_LAYERS[:-1]

                                # Default number of moralities per layer
                                MORALITIES_PER_LAYER = 5