from __future__ import annotations
from typing import Any
from datetime import datetime
from ..http import Payload


class Profile(object):
    def __init__(self, data: Payload) -> None:
        self.data = data
        self.user: dict = data.get("user")

    @property
    def id(self) -> int:
        return int(self.data.get("ID"))

    @property
    def badges(self) -> list[str]:
        return self.data.get("badges")

    @property
    def bio(self) -> str:
        return self.data.get("bio")
    
    @property
    def bots(self) -> list[int]:
        return [int(bot) for bot in self.data.get("bots")]
    
    @property
    def connections(self) -> list[dict]:
        return self.data.get("connections")

    @property
    def emails(self) -> list[str]:
        return self.data.get("emails")

    @property
    def favorites(self) -> list[str]:
        return [f"https://devlist.dev/p/{i}" for i in self.data.get("favorites")]

    @property
    def languages(self) -> dict:
        return self.data.get("languages")

    @property
    def npm_packages(self) -> list[str]:
        return [f"https://www.npmjs.com/package/{i}" for i in self.data.get("npm_packages")]
    
    @property
    def pip_packages(self) -> list[str]:
        return self.data.get("pip_packages")
    
    @property
    def servers(self) -> list[str]:
        return [f"https://discord.gg/{i}" for i in self.data.get("servers")]

    @property
    def websites(self) -> list[str]:
        return self.data.get("websites")

    @property
    def widgets(self) -> dict:
        return self.data.get("widgets")
    
    @property
    def slug(self) -> str:
        return self.data.get("slug")
    
    @property
    def vanity_url(self) -> str:
        return self.data.get("vanity_url")
    
    @property
    def theme(self) -> Any:
        return self.data.get("theme")
    
    @property
    def tags(self) -> str:
        return self.data.get("tags")
    
    @property
    def views(self) -> int:
        return self.data.get("views")
    
    @property
    def xp(self) -> dict:
        return self.data.get("xp")

    @property
    def blog(self) -> list[dict]:
        return self.data.get("blog")
    
    @property
    def projects(self) -> list[dict]:
        return self.data.get("projects")
    
    @property
    def contributed_projects(self) -> list[dict]:
        return self.data.get("contributed_projects")
    
    @property
    def comments(self) -> list[dict]:
        return self.data.get("comments")
    
    @property
    def configuration(self) -> dict:
        return self.data.get("configuration")
    
    @property
    def banner(self) -> str:
        return self.data.get("banner")

    @property
    def system(self) -> None | bool:
        return self.user.get("system")

    @property
    def flags(self) -> int:
        return self.user.get("flags")
    
    @property
    def username(self) -> str:
        return self.user.get("username")
        
    @property
    def is_bot(self) -> bool:
        return self.user.get("bot")
    
    @property
    def discriminator(self) -> int:
        return int(self.user.get("discriminator"))
    
    @property
    def avatar(self) -> str:
        avatar_hash: str = self.user.get("avatar")
        ext = "png"
        if avatar_hash.startswith("a_"):
            ext = "gif"
        return f"https://cdn.discordapp.com/avatars/{self.id}/{avatar_hash}.{ext}"
    
    @property
    def create_at(self) -> datetime:
        return datetime.fromtimestamp(float(self.user.get("createdTimestamp")))

    @property
    def tag(self) -> str:
        return self.user.get("tag")
    
    def __repr__(self) -> str:
        attrs = (
            ('id', self.id),
            ('name', self.username),
            ('tag', self.tag),
        )
        inner = ' '.join('%s=%r' % t for t in attrs)
        return f"<Profile {inner}>"
