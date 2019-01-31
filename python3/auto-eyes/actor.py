from api_model import ApiModel


class Actor(ApiModel):
    """
    Any human or humans outside of the Vehicle.  Typically pedestrians, bicyclists or other mobility users in the scene.
    
    """

    def __init__(self, actor_id: str, bearing: float):
        self._actor_id = actor_id
        """A unique identifier, provided by the client, to uniquely identify this actor across calls."""
        self._bearing = bearing
        """The degrees clockwise from the forward direction of a vehicle to the location of the actor."""

    @property
    def actor_id(self) -> str:
        return self._actor_id

    @property
    def bearing(self) -> float:
        return self._bearing

    def api_json(self):
        return {
            "actorId": self.actor_id,
            "bearing": self.bearing
        }