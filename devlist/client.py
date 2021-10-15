from .http import Rout
from .objects.profile import Profile

class UserNotFound(Exception):
    ...


class Client:
    
    def get_profile(self, user_id: int, /) -> Profile:
        if not self.is_exists(user_id):
            raise UserNotFound("User Not found")
        r = Rout("GET", f"/profile/{user_id}")
        return Profile(r.request())

    def is_exists(self, user_id: int, /) -> bool:
        return Rout("GET", f"/profile/{user_id}/exists").request()
