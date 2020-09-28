const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log('I am ready!');
});

client.on('message', message => {
    if (!message.content.startsWith('!') && message.channel.name === 'jukebox' && !message.author.bot) {
        message.delete();
        message.reply('Please use #general for general chat.');
    }
    else if (message.content.startsWith('!') && !message.author.bot) {
        message.delete();
        message.reply('Please use #jukebox to play music.');
    }
});

client.login(process.env.BOT_TOKEN);