from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
        for friend in friends:
            Cafe.visit_cafe(cafe, visitor=friend)
    except VaccineError:
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        mask_to_buy = sum([1 for friend in friends
                           if friend.get("wearing_a_mask") is False])
        return f"Friends should buy {mask_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
