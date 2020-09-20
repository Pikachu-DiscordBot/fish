from .fish import Fish


def setup(bot):
    bot.add_cog(Fish(bot))
