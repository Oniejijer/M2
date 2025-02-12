import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')

@bot.command()
async def reciclable(ctx, *, item: str):
    """Verifica si un objeto es reciclable o no."""
    reciclables = {"papel", "carton", "vidrio", "plastico", "metal"}
    no_reciclables = {"pañales", "papel higienico", "ceramica", "espejos", "colillas de cigarro"}
    item = item.lower()
    if item in reciclables:
        await ctx.send(f'{item.capitalize()} es reciclable. Depositalo en el contenedor adecuado.')
    elif item in no_reciclables:
        await ctx.send(f'{item.capitalize()} no es reciclable. Busca alternativas para reducir su uso.')
    else:
        await ctx.send(f'No estoy seguro sobre {item}. Investiga antes de desecharlo.')

@bot.command()
async def clasificar(ctx, *, item: str):
    """Clasifica un objeto en organico, reciclable o basura."""
    organicos = {"cascaras", "restos de comida", "hojas", "cesped"}
    reciclables = {"papel", "carton", "vidrio", "plastico", "metal"}
    if item.lower() in organicos:
        await ctx.send(f'{item.capitalize()} es organico y puedes compostarlo.')
    elif item.lower() in reciclables:
        await ctx.send(f'{item.capitalize()} es reciclable. Usa el contenedor adecuado.')
    else:
        await ctx.send(f'{item.capitalize()} es basura comun. Desechalo correctamente.')

@bot.command()
async def organizar(ctx):
    """Consejos para organizar residuos en casa."""
    consejos = (
        "1 Usa contenedores separados para cada tipo de residuo.\n"
        "2 Lava los materiales reciclables antes de depositarlos.\n"
        "3 Compacta botellas y cajas para ahorrar espacio.\n"
        "4 Evita mezclar residuos reciclables con desechos organicos.\n"
        "5 Identifica puntos de reciclaje en tu comunidad."
    )
    await ctx.send(consejos)

@bot.command()
async def reutilizar(ctx, *, item: str):
    """Sugerencias para reutilizar objetos en lugar de desecharlos."""
    ideas = {
        "botella de plastico": "Puedes convertirla en una maceta, dispensador de agua o decoracion.",
        "ropa vieja": "Usala para hacer trapos de limpieza o personalizala para darle una segunda vida.",
        "papel": "Haz libretas recicladas o manualidades."
    }
    await ctx.send(ideas.get(item.lower(), "No tengo ideas para reutilizar eso, pero puedes investigar mas opciones."))

@bot.command()
async def limpiar(ctx):
    """Instrucciones basicas para limpiar y manejar residuos correctamente."""
    pasos = (
        "1 Separa los residuos antes de desecharlos.\n"
        "2 Lava los envases reciclables.\n"
        "3 No mezcles materiales reciclables con basura comun.\n"
        "4 Reduce el uso de plasticos de un solo uso.\n"
        "5 Lleva residuos electronicos a centros especializados."
    )
    await ctx.send(pasos)

TOKEN = "TU_TOKEN_AQUI"
bot.run(TOKEN)
