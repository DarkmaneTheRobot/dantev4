import { MessageEmbed } from 'discord.js';
import { Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	constructor() {
		super({
			name: 'rawr',
			cooldown: 5,
			usage: '',
		});
	}
	public async run(msg: Message) {
		msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('X3!')
				.setDescription(
					`${msg.author} lets out a cute little rawr!`,
				)
				.setThumbnail(
					'https://d.facdn.net/art/yereren/1492210128/1492210128.yereren_ja.png',
				),
		);
	}
}