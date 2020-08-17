import { MessageEmbed } from 'discord.js';
import { Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	constructor() {
		super({
			name: 'slap',
			cooldown: 5,
			usage: '<member>',
		});
	}
	public async run(msg: Message) {
		msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('Trout Slap!')
				.setDescription(
					`${msg.author} slaps ${msg.mentions.users.first()} around a bit with a wet trout!`,
				)
				.setThumbnail(
					'https://i.pinimg.com/600x315/c7/eb/77/c7eb77dfaa7628a6c3438cd0139bcb78.jpg',
				),
		);
	}
}