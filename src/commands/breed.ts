import { MessageEmbed } from 'discord.js';
import { Message } from 'discord.js';

import Command from '../lib/structures/Command';

export default class extends Command {
	constructor() {
		super({
			name: 'breed',
			cooldown: 5,
			usage: '<member>',
		});
	}
	public async run(msg: Message) {
      // @ts-ignore
    if(msg.channel.nsfw === false){
      msg.channel.send(
  			new MessageEmbed()
  				.setColor(0x00ff00)
  				.setTitle('Not A NSFW Channel')
  				.setDescription(
  					`The channel you just ran the command in is not NSFW!`,
  				)
  				.setThumbnail(
  					'https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png',
  				),
  		);
    }
		msg.channel.send(
			new MessageEmbed()
				.setColor(0x00ff00)
				.setTitle('GIVE ME YOUR CUBS!')
				.setDescription(
					`${msg.author} has impregnated ${msg.mentions.users.first()}, giving them a healthy litter!`,
				)
				.setThumbnail(
					'https://us.rule34.xxx//images/364/3db9b8b409f5100aafc62f6352d31db1c60f3c64.png',
				),
		);
	}
}