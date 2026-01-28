# Identity validation between MUN and MUNCSS.
# To verify that a user is an active student
# or staff member, this service will open up
# a prompt to sign into some service using their
# institutional email address. (@mun.ca)
#
# How this is implemented, is beyond me at the moment.

import asyncio
from typing import Dict, List, Optional, Union

import discord
from discord.ext import commands