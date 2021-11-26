const Discord = require('discord.js');
const ytdl = require('ytdl-core')

const client = new Discord.Client();
const prefix = "-"
const queue = new Map();

client.on('ready', () => {
    console.log('I am ready!');
});

client.on('message', message => {
    const serverQueue = queue.get(message.guild.id);

    if (message.author.bot) {
        return;
    }
    else if (!message.content.startsWith('!') && !message.content.startsWith('-') && !message.content.startsWith('>>') && message.channel.name === 'jukebox') {
        message.delete();
        message.reply('please use ' + message.guild.channels.cache.find(channel => channel.name === "general").toString() + ' for general chat.');
    }
    else if ((message.content.startsWith('!') || message.content.startsWith('-')) && message.channel.name !== 'jukebox') {
        message.delete();
        message.reply('please use ' + message.guild.channels.cache.find(channel => channel.name === "jukebox").toString() + ' to play music.');
    }
    else if (message.content.startsWith(`${prefix}play`)) {
        execute(message, serverQueue);
        return;
    }
    else if (message.content.startsWith(`${prefix}skip`)) {
        skip(message, serverQueue);
        return;
    }
    else if (message.content.startsWith(`${prefix}stop`)){
        stop(message,serverQueue);
        return;
    }
});

async function execute(message, serverQueue) {
    const args = message.content.split(" ");

    const voiceChannel = message.member.voice.channel;
    if (!voiceChannel)
        return message.channel.send(
            "You need to be in a voice channel to play music."
        );
    const permissions = voiceChannel.permissionsFor(message.client.user);
    if (!permissions.has("CONNECT") || !permissions.has("SPEAK")) {
        return message.channel.send(
            "I need permissions to join and speak in your channel!"
        );
    }

    const songInfo = await ytdl.getInfo(args[1]);
    const song = {
        title: songInfo.videoDetails.title,
        url: songInfo.videoDetails.video_url,
    };

    if (!serverQueue) {
      const queueConstruct = {
        textChannel: message.channel,
        voiceChannel: voiceChannel,
        connection: null,
        songs: [],
        volume: 5,
        playing: true
      };

      queue.set(message.guild.id, queueConstruct);

      queueConstruct.songs.push(song);

      try {
        console.log("here 1");
        var connection = await voiceChannel.join();
        console.log("here 2");
        queueConstruct.connection = connection;
        console.log("here 3");
        play(message.guild, queueConstruct.songs[0]);
      } catch (err) {
        console.log(err);
        queue.delete(message.guild.id);
        return message.channel.send(err);
      }
    } else {
      serverQueue.songs.push(song);
      return message.channel.send(`${song.title} has been added to the queue!`);
    }
}

function play(guild, song){
    console.log("here play");
    const serverQueue = queue.get(guild.id);
    if (!song) {
        serverQueue.voiceChannel.leave()
        queue.delete(guild.id)
        return
    }
    const dispatcher = serverQueue.connection.play(ytdl(song.url)).on("finish", () => {
        serverQueue.songs.shift();
        play(guild, serverQueue.songs[0]);
    })
    .on("error", error => console.error(error))
    dispatcher.setVolumeLogarithmic(serverQueue.volume / 5)
    serverQueue.textChannel.send(`Now Playing **${song.title}**`)
}

function skip(message, serverQueue) {
    if (!message.member.voice.channel)
      return message.channel.send(
        "You have to be in a voice channel to stop the music!"
      );
    if (!serverQueue)
      return message.channel.send("There is no song that I could skip!");
    serverQueue.connection.dispatcher.end();
}

function stop(message, serverQueue) {
  if (!message.member.voice.channel)
    return message.channel.send(
      "You have to be in a voice channel to stop the music!"
    );
  
  if (!serverQueue)
    return message.channel.send("There is no song that I could stop!");
    
  serverQueue.songs = [];
  serverQueue.connection.dispatcher.end();
}

client.login(process.env.BOT_TOKEN);
