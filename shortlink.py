import os
import asyncio
from os import getenv, environ
from asyncio import TimeoutError
from Adarsh.vars import Var

SHORTENER_API = str(getenv('URL_SHORTNER_WEBSITE_API', 'e0867ce24e2238645541bf7651be2217b4cd5dd1'))
SHORTENER_WEBSITE = str(getenv('URL_SHORTENR_WEBSITE', 'shorturllink.in'))

async def get_shortlink(link):
    https = link.split(":")[0]
    if "http" == https:
        https = "https"
        link = link.replace("http", https)
    url = f'https://{URL_SHORTENR_WEBSITE}/api'
    params = {'api': URL_SHORTNER_WEBSITE_API,
              'url': link,
              }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                data = await response.json()
                if data["status"] == "success":
                    return data['shortenedUrl']
                else:
                    logger.error(f"Error: {data['message']}")
                    return f'https://{URL_SHORTENR_WEBSITE}/api?api={URL_SHORTNER_WEBSITE_API}&link={link}'

    except Exception as e:
        logger.error(e)
        return f'{URL_SHORTENR_WEBSITE}/api?api={URL_SHORTNER_WEBSITE_API}&link={link}'

