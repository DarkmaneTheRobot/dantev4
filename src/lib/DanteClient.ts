import { Client, Collection } from 'discord.js';

import Command from './structures/Command';

export class DanteClient extends Client {
	public commands!: Collection<string, Command>;
	public commandCooldowns!: Collection<string, Collection<string, number>>;
}
