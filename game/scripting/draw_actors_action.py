from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        tanks = cast.get_actors("tanks")
        items = cast.get_actors("items")
        missiles = cast.get_actors("missiles1")
        missiles.extend(cast.get_actors("missiles2"))
        healths = cast.get_actors("healths")

        self._video_service.clear_buffer()
        
        for missile in missiles:
            self._video_service.draw_actor(missile)
        
        for tank in tanks:
            self._video_service.draw_actor(tank)

        for health in healths:
            self._video_service.draw_actor(health)

        self._video_service.draw_actors(items)

        self._video_service.flush_buffer()