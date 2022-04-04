from cmath import pi
from distutils.command import upload
from cv2 import DECOMP_QR
import telebot

CHAVE_API = "5233559558:AAH9U7XYmnLIe1wksNuGg7f32YiJjb2jsYs"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["teste"])
def teste(mensagem):
    import speedtest
    r = speedtest.Speedtest()
    servers = r.get_servers()
    r.get_best_server()
    dow = r.download(threads=None)
    upl = r.upload(threads=None, pre_allocate=True)
    download_mbs = round(dow / (10**6), 2)
    upload_mbs = round(upl / (10**6), 2)
    ping = r.results.ping
    bot.send_message(mensagem.chat.id, "🚀 Velocidade de Download mbps✅:⬇")
    bot.send_message(mensagem.chat.id, download_mbs)
    bot.send_message(mensagem.chat.id, "🚀 Velocidade de Upload mbps✅:⬇")
    bot.send_message(mensagem.chat.id, upload_mbs)
    bot.send_message(mensagem.chat.id, "🚀 Ping ms✅:⬇")
    bot.send_message(mensagem.chat.id, ping)


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
        Teste sua velocidade de conexão com a Internet 🚀🚀🚀🚀🚀
  Escolha a opção teste para continuar(Clique no item):
    /teste Iniciar teste de velocidade de conexão ⬅🚀
  Responder qualquer outra coisa não vai funcionar, ✔ Clique no item
  """
    bot.reply_to(mensagem, texto)


bot.polling()
