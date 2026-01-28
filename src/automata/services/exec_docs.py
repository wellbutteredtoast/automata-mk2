# Service for handling new and old Executive Documents
# This also handles posting new docs to the `exec-docs` channel
#

import asyncio
from datetime import datetime
from typing import Any

import discord
from discord.ext import tasks

EXECUTIVE_DOCS_BASE_URI = "https://www.cs.mun.ca/~csclub/executive-documents"
EXECUTIVE_DOCS_JSON_URI = f"{EXECUTIVE_DOCS_BASE_URI}/docs.json"