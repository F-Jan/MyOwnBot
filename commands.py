import hikari
import lightbulb


def init_commands(bot):

    @bot.command
    @lightbulb.option("member", "User to find info about", required=False, type=hikari.Member)
    @lightbulb.command("user_info", "Get info about a User")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def user_info(ctx: lightbulb.Context) -> None:
        member: hikari.Member = ctx.options.member

        if member is None:
            member = ctx.member

        embed = hikari.Embed(title="Info [" + member.username + "]")

        embed.add_field("Name", member.user.mention, inline=True)
        embed.add_field("Tag", str(member), inline=True)
        embed.add_field("Id", str(member.user.id))
        embed.add_field("Join-Date", str(member.joined_at.strftime("%b %d %Y %H:%M:%S")))

        await ctx.respond(embed=embed)
