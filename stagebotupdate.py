import os
import json
import discord
import requests
import re
from functools import reduce

client = discord.Client()
PATH_STAGEDATA = './stage_data.json'
REGULAR_IMG = 'https://cdn.discordapp.com/attachments/593485514301243413/593485875250331660/battle_regular.png'
GACHI_IMG = 'https://cdn.discordapp.com/attachments/593485514301243413/593485870452178945/battle_gachi.png'
LEAGUE_IMG = 'https://cdn.discordapp.com/attachments/593485514301243413/593485873320820746/battle_league.png'
game = discord.Game("アプデ楽しみ")

@client.event
async def on_ready(reconnect=True):
    print('Logged in as')
    print('name = ' + client.user.name)
    print('>>>>>>>>>>>>>>>>')
    await client.change_presence(activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("nwtf"):
        if message.author != client.user:
            with open(PATH_STAGEDATA, 'r') as f:
                jsondata = json.load(f)
                now_turf_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["regular"][0]["maps"])
                end_time_of_now_turf = re.search(r'T.*', jsondata["result"]["regular"][0]["end"]).group()[1:]
                now_turf_stage_image1 = jsondata["result"]["regular"][0]["maps_ex"][0]["image"]
                now_turf_stage_image2 = jsondata["result"]["regular"][0]["maps_ex"][1]["image"]
                embed = discord.Embed(title="現在のナワバリ", color=0x00ff00)
                embed.set_thumbnail(url=REGULAR_IMG)
                embed.add_field(name="ステージ", value=now_turf_stage, inline=True)
                embed.add_field(name="終了時間", value=end_time_of_now_turf, inline=True)
                embed.set_image(url=now_turf_stage_image1)
                embed.set_image(url=now_turf_stage_image2)
                await message.channel.send(embed=embed)

    if message.content.startswith("schelp"):
        if message.author != client.user:
            embed = discord.Embed(title="ステージお知らせHELP", color=0x00ff00)
            embed.add_field(name="直近のスケジュール", value="schedule", inline=True)
            embed.add_field(name="現在のナワバリ", value="nwtf", inline=True)
            embed.add_field(name="次回のナワバリ", value="nxtf", inline=True)
            embed.add_field(name="現在のガチマッチ", value="nwrk", inline=True)
            embed.add_field(name="次回のガチマッチ", value="nxrk", inline=True)
            embed.add_field(name="現在のリーグマッチ", value="nwlg", inline=True)
            embed.add_field(name="次回のリーグマッチ", value="nxlg", inline=True)
            embed.add_field(name="次のエリアリグマ", value="ner", inline=True)
            embed.add_field(name="次のホコリグマ", value="ngr", inline=True)
            embed.add_field(name="次のガチマエリア", value="nge", inline=True)
            await message.channel.send(embed=embed)

    if message.content.startswith("nxtf"):
        if message.author != client.user:
            with open(PATH_STAGEDATA, 'r') as f:
                jsondata = json.load(f)
                next_turf_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["regular"][1]["maps"])
                end_time_of_next_turf = re.search(r'T.*', jsondata["result"]["regular"][1]["end"]).group()[1:]
                next_turf_stage_image1 = jsondata["result"]["regular"][1]["maps_ex"][0]["image"]
                next_turf_stage_image2 = jsondata["result"]["regular"][1]["maps_ex"][1]["image"]
                embed = discord.Embed(title="次のナワバリ", color=0x00ff00)
                embed.set_thumbnail(url=REGULAR_IMG)
                embed.add_field(name="ステージ", value=next_turf_stage, inline=True)
                embed.add_field(name="終了時間", value=end_time_of_next_turf, inline=True)
                embed.set_image(url=next_turf_stage_image1)
                embed.set_image(url=next_turf_stage_image2)
                await message.channel.send(embed=embed)

    if message.content.startswith("nwrk"):
        if message.author != client.user:
            with open(PATH_STAGEDATA, 'r') as f:
                jsondata = json.load(f)
                now_ranked_rule = jsondata["result"]["gachi"][0]["rule"]
                now_ranked_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["gachi"][0]["maps"])
                end_time_of_now_ranked = re.search(r'T.*', jsondata["result"]["gachi"][0]["end"]).group()[1:]
                now_ranked_stage_image1 = jsondata["result"]["gachi"][0]["maps_ex"][0]["image"]
                now_ranked_stage_image2 = jsondata["result"]["gachi"][0]["maps_ex"][1]["image"]
                embed = discord.Embed(title="現在のガチマッチ", color=0xFF8C00)
                embed.set_thumbnail(url=GACHI_IMG)
                embed.add_field(name="ルール", value=now_ranked_rule, inline=True)
                embed.add_field(name="ステージ", value=now_ranked_stage, inline=True)
                embed.add_field(name="終了時間", value=end_time_of_now_ranked, inline=True)
                embed.set_image(url=now_ranked_stage_image1)
                embed.set_image(url=now_ranked_stage_image2)
                await message.channel.send(embed=embed)

    if message.content.startswith("nxrk"):
        if message.author != client.user:
            with open(PATH_STAGEDATA, 'r') as f:
                jsondata = json.load(f)
                next_ranked_rule = jsondata["result"]["gachi"][1]["rule"]
                next_ranked_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["gachi"][1]["maps"])
                end_time_of_next_ranked = re.search(r'T.*', jsondata["result"]["gachi"][1]["end"]).group()[1:]
                next_ranked_stage_image1 = jsondata["result"]["gachi"][1]["maps_ex"][0]["image"]
                next_ranked_stage_image2 = jsondata["result"]["gachi"][1]["maps_ex"][1]["image"]
                embed = discord.Embed(title="次のガチマッチ", color=0xFF8C00)
                embed.set_thumbnail(url=GACHI_IMG)
                embed.add_field(name="ルール", value=next_ranked_rule, inline=True)
                embed.add_field(name="ステージ", value=next_ranked_stage, inline=True)
                embed.add_field(name="終了時間", value=end_time_of_next_ranked, inline=True)
                embed.set_image(url=next_ranked_stage_image1)
                embed.set_image(url=next_ranked_stage_image2)
                await message.channel.send(embed=embed)

    if message.content.startswith("nwlg"):
        if message.author != client.user:
            with open(PATH_STAGEDATA, 'r') as f:
                jsondata = json.load(f)
                now_league_rule = jsondata["result"]["league"][0]["rule"]
                now_league_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["league"][0]["maps"])
                end_time_of_now_league = re.search(r'T.*', jsondata["result"]["league"][0]["end"]).group()[1:]
                now_league_stage_image1 = jsondata["result"]["league"][0]["maps_ex"][0]["image"]
                now_league_stage_image2 = jsondata["result"]["league"][0]["maps_ex"][1]["image"]
                embed = discord.Embed(title="現在のリーグマッチ", color=0xff69B4)
                embed.set_thumbnail(url=LEAGUE_IMG)
                embed.add_field(name="ルール", value=now_league_rule, inline=True)
                embed.add_field(name="ステージ", value=now_league_stage, inline=True)
                embed.add_field(name="終了時間", value=end_time_of_now_league, inline=True)
                embed.set_image(url=now_league_stage_image1)
                embed.set_image(url=now_league_stage_image2)
                await message.channel.send(embed=embed)

    if message.content.startswith("nxlg"):
        if message.author != client.user:
            with open(PATH_STAGEDATA, 'r') as f:
                jsondata = json.load(f)
                next_league_rule = jsondata["result"]["league"][1]["rule"]
                next_league_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["league"][1]["maps"])
                end_time_of_next_league = re.search(r'T.*', jsondata["result"]["league"][1]["end"]).group()[1:]
                next_league_stage_image1 = jsondata["result"]["league"][1]["maps_ex"][0]["image"]
                next_league_stage_image2 = jsondata["result"]["league"][1]["maps_ex"][1]["image"]
                embed = discord.Embed(title="次のリーグマッチ", color=0xff69B4)
                embed.set_thumbnail(url=LEAGUE_IMG)
                embed.add_field(name="ルール", value=next_league_rule, inline=True)
                embed.add_field(name="ステージ", value=next_league_stage, inline=True)
                embed.add_field(name="終了時間", value=end_time_of_next_league, inline=True)
                embed.set_image(url=next_league_stage_image1)
                embed.set_image(url=next_league_stage_image2)
                await message.channel.send(embed=embed)

    if message.content.startswith("ner"):
        if message.author != client.user:
            with open(PATH_STAGEDATA, 'r') as f:
                jsondata = json.load(f)
                if jsondata["result"]["league"][0]["rule"] == "ガチエリア":
                    now_splatzone_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["league"][0]["maps"])
                    now_splatzone_start = re.search(r'T.*', jsondata["result"]["league"][0]["start"]).group()[1:]
                    now_splatzone_end = re.search(r'T.*', jsondata["result"]["league"][0]["end"]).group()[1:]
                    embed = discord.Embed(title="次のエリアリグマ", description="エリアリグマは現在開催中です！", color=0xff69B4)
                    embed.set_thumbnail(url=LEAGUE_IMG)
                    embed.add_field(name="ステージ", value=now_splatzone_stage, inline=True)
                    embed.add_field(name="開始時間", value=now_splatzone_start, inline=True)
                    embed.add_field(name="終了時間", value=now_splatzone_end, inline=True)
                    await message.channel.send(embed=embed)
                    return
                if jsondata["result"]["league"][1]["rule"] == "ガチエリア":
                    next_splatzone_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["league"][1]["maps"])
                    next_splatzone_start = re.search(r'T.*', jsondata["result"]["league"][1]["start"]).group()[1:]
                    next_splatzone_end = re.search(r'T.*', jsondata["result"]["league"][1]["end"]).group()[1:]
                    embed = discord.Embed(title="次のエリアリグマ", description="エリアリグマは次のスケジュール更新後です！", color=0xff69B4)
                    embed.set_thumbnail(url=LEAGUE_IMG)
                    embed.add_field(name="ステージ", value=next_splatzone_stage, inline=True)
                    embed.add_field(name="開始時間", value=next_splatzone_start, inline=True)
                    embed.add_field(name="終了時間", value=next_splatzone_end, inline=True)
                    await message.channel.send(embed=embed)
                    return
                if jsondata["result"]["league"][2]["rule"] == "ガチエリア":
                    next_next_splatzone_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["league"][2]["maps"])
                    next_next_splatzone_start = re.search(r'T.*', jsondata["result"]["league"][2]["start"]).group()[1:]
                    next_next_splatzone_end = re.search(r'T.*', jsondata["result"]["league"][2]["end"]).group()[1:]
                    embed = discord.Embed(title="次のエリアリグマ", description="エリアリグマは次の次のスケジュール更新後です！", color=0xff69B4)
                    embed.set_thumbnail(url=LEAGUE_IMG)
                    embed.add_field(name="ステージ", value=next_next_splatzone_stage, inline=True)
                    embed.add_field(name="開始時間", value=next_next_splatzone_start, inline=True)
                    embed.add_field(name="終了時間", value=next_next_splatzone_end, inline=True)
                    await message.channel.send(embed=embed)
                    return
                if jsondata["result"]["league"][0]["rule"] and jsondata["result"]["league"][1]["rule"] and jsondata["result"]["league"][2]["rule"] != "ガチエリア":
                    embed = discord.Embed(title="次のエリアリグマ", description="次の次のスケジュール更新までにエリアリグマは無いようだ...", color=0xff69B4)
                    embed.set_thumbnail(url=LEAGUE_IMG)
                    await message.channel.send(embed=embed)

    if message.content.startswith("ngr"):
        if message.author != client.user:
            with open(PATH_STAGEDATA, 'r') as f:
                jsondata = json.load(f)
                if jsondata["result"]["league"][0]["rule"] == "ガチホコバトル":
                    now_splatzone_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["league"][0]["maps"])
                    now_splatzone_start = re.search(r'T.*', jsondata["result"]["league"][0]["start"]).group()[1:]
                    now_splatzone_end = re.search(r'T.*', jsondata["result"]["league"][0]["end"]).group()[1:]
                    embed = discord.Embed(title="次のホコリグマ", description="ホコリグマは現在開催中です！", color=0xff69B4)
                    embed.set_thumbnail(url=LEAGUE_IMG)
                    embed.add_field(name="ステージ", value=now_splatzone_stage, inline=True)
                    embed.add_field(name="開始時間", value=now_splatzone_start, inline=True)
                    embed.add_field(name="終了時間", value=now_splatzone_end, inline=True)
                    await message.channel.send(embed=embed)
                    return
                if jsondata["result"]["league"][1]["rule"] == "ガチホコバトル":
                    next_splatzone_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["league"][1]["maps"])
                    next_splatzone_start = re.search(r'T.*', jsondata["result"]["league"][1]["start"]).group()[1:]
                    next_splatzone_end = re.search(r'T.*', jsondata["result"]["league"][1]["end"]).group()[1:]
                    embed = discord.Embed(title="次のホコリグマ", description="ホコリグマは次のスケジュール更新後です！", color=0xff69B4)
                    embed.set_thumbnail(url=LEAGUE_IMG)
                    embed.add_field(name="ステージ", value=next_splatzone_stage, inline=True)
                    embed.add_field(name="開始時間", value=next_splatzone_start, inline=True)
                    embed.add_field(name="終了時間", value=next_splatzone_end, inline=True)
                    await message.channel.send(embed=embed)
                    return
                if jsondata["result"]["league"][2]["rule"] == "ガチホコバトル":
                    next_next_splatzone_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["league"][2]["maps"])
                    next_next_splatzone_start = re.search(r'T.*', jsondata["result"]["league"][2]["start"]).group()[1:]
                    next_next_splatzone_end = re.search(r'T.*', jsondata["result"]["league"][2]["end"]).group()[1:]
                    embed = discord.Embed(title="次のホコリグマ", description="ホコリグマは次の次のスケジュール更新後です！", color=0xff69B4)
                    embed.set_thumbnail(url=LEAGUE_IMG)
                    embed.add_field(name="ステージ", value=next_next_splatzone_stage, inline=True)
                    embed.add_field(name="開始時間", value=next_next_splatzone_start, inline=True)
                    embed.add_field(name="終了時間", value=next_next_splatzone_end, inline=True)
                    await message.channel.send(embed=embed)
                    return
                if jsondata["result"]["league"][0]["rule"] and jsondata["result"]["league"][1]["rule"] and jsondata["result"]["league"][2]["rule"] != "ガチホコバトル":
                    embed = discord.Embed(title="次のホコリグマ", description="次の次のスケジュール更新までにホコリグマは無いようだ...", color=0xff69B4)
                    embed.set_thumbnail(url=LEAGUE_IMG)
                    await message.channel.send(embed=embed)

    if message.content.startswith("nge"):
        if message.author != client.user:
            with open(PATH_STAGEDATA, 'r') as f:
                jsondata = json.load(f)
                if jsondata["result"]["gachi"][0]["rule"] == "ガチエリア":
                    now_splatzone_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["gachi"][0]["maps"])
                    now_splatzone_start = re.search(r'T.*', jsondata["result"]["gachi"][0]["start"]).group()[1:]
                    now_splatzone_end = re.search(r'T.*', jsondata["result"]["gachi"][0]["end"]).group()[1:]
                    embed = discord.Embed(title="次のガチマエリア", description="ガチマエリアは現在開催中です！", color=0xFF8C00)
                    embed.set_thumbnail(url=GACHI_IMG)
                    embed.add_field(name="ステージ", value=now_splatzone_stage, inline=True)
                    embed.add_field(name="開始時間", value=now_splatzone_start, inline=True)
                    embed.add_field(name="終了時間", value=now_splatzone_end, inline=True)
                    await message.channel.send(embed=embed)
                    return
                if jsondata["result"]["gachi"][1]["rule"] == "ガチエリア":
                    next_splatzone_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["gachi"][1]["maps"])
                    next_splatzone_start = re.search(r'T.*', jsondata["result"]["gachi"][1]["start"]).group()[1:]
                    next_splatzone_end = re.search(r'T.*', jsondata["result"]["gachi"][1]["end"]).group()[1:]
                    embed = discord.Embed(title="次のガチマエリア", description="ガチマエリアは次のスケジュール更新後です！", color=0xFF8C00)
                    embed.set_thumbnail(url=GACHI_IMG)
                    embed.add_field(name="ステージ", value=next_splatzone_stage, inline=True)
                    embed.add_field(name="開始時間", value=next_splatzone_start, inline=True)
                    embed.add_field(name="終了時間", value=next_splatzone_end, inline=True)
                    await message.channel.send(embed=embed)
                    return
                if jsondata["result"]["gachi"][2]["rule"] == "ガチエリア":
                    next_next_splatzone_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["gachi"][2]["maps"])
                    next_next_splatzone_start = re.search(r'T.*', jsondata["result"]["gachi"][2]["start"]).group()[1:]
                    next_next_splatzone_end = re.search(r'T.*', jsondata["result"]["gachi"][2]["end"]).group()[1:]
                    embed = discord.Embed(title="次のガチマエリア", description="ガチマエリアは次の次のスケジュール更新後です！", color=0xFF8C00)
                    embed.set_thumbnail(url=GACHI_IMG)
                    embed.add_field(name="ステージ", value=next_next_splatzone_stage, inline=True)
                    embed.add_field(name="開始時間", value=next_next_splatzone_start, inline=True)
                    embed.add_field(name="終了時間", value=next_next_splatzone_end, inline=True)
                    await message.channel.send(embed=embed)
                    return
                if jsondata["result"]["gachi"][0]["rule"] and jsondata["result"]["gachi"][1]["rule"] and jsondata["result"]["gachi"][2]["rule"] != "ガチエリア":
                    embed = discord.Embed(title="次のガチマエリア", description="次の次のスケジュール更新までにガチマエリアは無いようだ...", color=0xFF8C00)
                    embed.set_thumbnail(url=GACHI_IMG)
                    await message.channel.send(embed=embed)

    if message.content.startswith("schedule"):
        if message.author != client.user:
            with open(PATH_STAGEDATA, 'r') as f:
                jsondata = json.load(f)
                now_regular_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["regular"][0]["maps"])
                next_regular_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["regular"][1]["maps"])
                now_gachi_rule = jsondata["result"]["gachi"][0]["rule"]
                now_gachi_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["gachi"][0]["maps"])
                next_gachi_rule = jsondata["result"]["gachi"][1]["rule"]
                next_gachi_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["gachi"][1]["maps"])
                now_league_rule = jsondata["result"]["league"][0]["rule"]
                now_league_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["league"][0]["maps"])
                end_time_of_now_league = re.search(r'T.*', jsondata["result"]["league"][0]["end"]).group()[1:]
                next_league_rule = jsondata["result"]["league"][1]["rule"]
                next_league_stage = reduce(lambda x, y: x + ", " + y, jsondata["result"]["league"][1]["maps"])
                end_time_of_next_league = re.search(r'T.*', jsondata["result"]["league"][1]["end"]).group()[1:]
                embed = discord.Embed(title="直近のスケジュール", color=0x00ff00)
                embed.set_thumbnail(url=REGULAR_IMG)
                embed.add_field(name="現在のナワバリステージ", value=now_regular_stage, inline=False)
                embed.add_field(name="次のナワバリステージ", value=next_regular_stage, inline=False)
                embed.add_field(name="現在のガチルール", value=now_gachi_rule, inline=True)
                embed.add_field(name="次のガチルール", value=next_gachi_rule, inline=True)
                embed.add_field(name="現在のガチマステージ", value=now_gachi_stage, inline=False)
                embed.add_field(name="次のガチマステージ", value=next_gachi_stage, inline=False)
                embed.add_field(name="現在のリグマルール", value=now_league_rule, inline=True)
                embed.add_field(name="次のリグマルール", value=next_league_rule, inline=True)
                embed.add_field(name="現在のリグマステージ", value=now_league_stage, inline=False)
                embed.add_field(name="次のリグマステージ", value=next_league_stage, inline=False)
                embed.add_field(name="終了時間", value=end_time_of_now_league, inline=True)
                embed.add_field(name="次の終了時間", value=end_time_of_next_league, inline=True)
                await message.channel.send(embed=embed)

client.run("ここにbotのtokenをいれてね")
