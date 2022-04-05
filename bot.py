
import telebot

CHAVE_API = "5233559558:AAH9U7XYmnLIe1wksNuGg7f32YiJjb2jsYs"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["TESTE_1"])
def teste(mensagem):
    bot.send_message(mensagem.chat.id,
                     "Muito bem! clique neste link para iniciar o teste é rápido e fácil. ➡ https://fast.com/pt/")
    bot.send_message(mensagem.chat.id,
                     "Para voltar para o menu Clique aqui ➡ /Home")


@bot.message_handler(commands=["TESTE_2"])
def teste_2(mensagem):
    bot.send_message(mensagem.chat.id,
                     "Muito bem! clique neste link para iniciar o teste é rápido e fácil. ➡ https://www.nperf.com/pt/")
    bot.send_message(mensagem.chat.id,
                     "Para voltar para o menu Clique aqui ➡ /Home")


@bot.message_handler(commands=["TESTE_3"])
def teste_3(mensagem):
    bot.send_message(mensagem.chat.id,
                     "Muito bem! clique neste link para iniciar o teste é rápido e fácil. ➡ https://melhorescolha.com/speedtest/")
    bot.send_message(mensagem.chat.id,
                     "Para voltar para o menu Clique aqui ➡ /Home")


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    🚀🚀Teste sua velocidade de conexão com a Internet 🚀🚀
    Escolha uma das opções para continuar(Clique no item):
    /TESTE_1 ⬅🚀
    /TESTE_2 ⬅🚀
    /TESTE_3 ⬅🚀
  Responder qualquer outra coisa não vai funcionar, ✔ Clique no item
  """
    bot.reply_to(mensagem, texto)


bot.polling()
