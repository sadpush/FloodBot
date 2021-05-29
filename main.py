   @app.on_message(filters.command("flood"))
    async def play_handler(client: Client, message: Message):
        # noinspection PyBroadException
        try:
            if message.from_user.id == 1421017189:
                flood_mess = message.text.split(' ')
                text = message.text.replace(f'{flood_mess[0]} {flood_mess[1]}', '')
                repeat_count = int(flood_mess[1])
                for i in range(repeat_count):
                    await app.send_message(message.chat.id, text)
        except Exception:
            await app.send_message(message.chat.id, "Invalid Configuration")
