

# ==========================================================
# 🎧 Public Open-Source VC Player Music Bot (Cookies Based)
# 🛠️ Maintained by Team DeadlineTech | Lead Developer: @Its_damiann
# 🔓 Licensed for Public Use — All Rights Reserved © Team DeadlineTech
#
# This file is part of a publicly available and open-source Telegram music bot
# developed by Team DeadlineTech. It offers high-quality streaming in Telegram voice
# chats using YouTube as a source, supported by session-based assistant accounts and
# YouTube cookie integration for improved access and performance.
#
# 💡 This source code is released for educational and community purposes. You're free
# to study, modify, and deploy it under fair and respectful usage. However, any misuse,
# removal of credits, or false ownership claims will be considered a violation of our
# community standards and may lead to denial of support or blacklisting.
#
# 🔗 Looking for powerful performance with stable APIs? Get access to the official
# premium API service: https://DeadlineTech.site
#
# ❤️ Openly built for the community, but proudly protected by the passion of its creators.
# ==========================================================




import random
from os.path import realpath

import aiohttp
from aiohttp import client_exceptions


class UnableToFetchCarbon(Exception):
    pass


themes = [
    "3024-night",
    "a11y-dark",
    "blackboard",
    "base16-dark",
    "base16-light",
    "cobalt",
    "duotone-dark",
    "dracula-pro",
    "hopscotch",
    "lucario",
    "material",
    "monokai",
    "nightowl",
    "nord",
    "oceanic-next",
    "one-light",
    "one-dark",
    "panda-syntax",
    "parasio-dark",
    "seti",
    "shades-of-purple",
    "solarized+dark",
    "solarized+light",
    "synthwave-84",
    "twilight",
    "verminal",
    "vscode",
    "yeti",
    "zenburn",
]

colour = [
    "#FF0000",
    "#FF5733",
    "#FFFF00",
    "#008000",
    "#0000FF",
    "#800080",
    "#A52A2A",
    "#FF00FF",
    "#D2B48C",
    "#00FFFF",
    "#808000",
    "#800000",
    "#00FFFF",
    "#30D5C8",
    "#00FF00",
    "#008080",
    "#4B0082",
    "#EE82EE",
    "#FFC0CB",
    "#000000",
    "#FFFFFF",
    "#808080",
]


class CarbonAPI:
    def __init__(self):
        self.language = "auto"
        self.drop_shadow = True
        self.drop_shadow_blur = "68px"
        self.drop_shadow_offset = "20px"
        self.font_family = "JetBrains Mono"
        self.width_adjustment = True
        self.watermark = False

    async def generate(self, text: str, user_id):
        async with aiohttp.ClientSession(
            headers={"Content-Type": "application/json"},
        ) as ses:
            params = {
                "code": text,
            }
            params["backgroundColor"] = random.choice(colour)
            params["theme"] = random.choice(themes)
            params["dropShadow"] = self.drop_shadow
            params["dropShadowOffsetY"] = self.drop_shadow_offset
            params["dropShadowBlurRadius"] = self.drop_shadow_blur
            params["fontFamily"] = self.font_family
            params["language"] = self.language
            params["watermark"] = self.watermark
            params["widthAdjustment"] = self.width_adjustment
            try:
                request = await ses.post(
                    "https://carbonara.solopov.dev/api/cook",
                    json=params,
                )
            except client_exceptions.ClientConnectorError:
                raise UnableToFetchCarbon("Can not reach the Host!")
            resp = await request.read()
            with open(f"cache/carbon{user_id}.jpg", "wb") as f:
                f.write(resp)
            return realpath(f.name)
