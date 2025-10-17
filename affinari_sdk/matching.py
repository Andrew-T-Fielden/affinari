import math

def weighted_manhattan(user_traits, item_traits, weights):
    total_diff = 0.0
    total_weight = 0.0

    for trait, user_val in user_traits.items():
        if trait in item_traits and trait in weights:
            total_diff += abs(user_val - item_traits[trait]) * weights[trait]
            total_weight += weights[trait]

    if total_weight == 0:
        return 0.0

    score = 1 - (total_diff / total_weight)
    return max(0.0, min(1.0, score))  # normalised [0,1]


def cosine_similarity(vec1, vec2):
    shared = set(vec1.keys()) & set(vec2.keys())
    if not shared:
        return 0.0

    dot = sum(vec1[t] * vec2[t] for t in shared)
    mag1 = math.sqrt(sum(vec1[t]**2 for t in shared))
    mag2 = math.sqrt(sum(vec2[t]**2 for t in shared))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return dot / (mag1 * mag2)
