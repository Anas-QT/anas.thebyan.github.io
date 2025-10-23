import os
import asyncio
from telegram import Bot

async def send_message(message_text):
    bot_token = os.environ.get('BOT_TOKEN')
    chat_id = os.environ.get('CHAT_ID')
    
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message_text)
    print(f"Message sent: {message_text[:50]}...")

if __name__ == "__main__":
    # Get which message to send from environment variable
    message_type = os.environ.get('MESSAGE_TYPE', 'default')
    
    messages = {
        'message': "[[وَأَن لَّیۡسَ لِلۡإِنسَـٰنِ إِلَّا مَا سَعَىٰ﴿ ٣٩ ﴾ وَأَنَّ سَعۡیَهُۥ سَوۡفَ یُرَىٰ﴿ ٤٠ ﴾ ثُمَّ یُجۡزَىٰهُ ٱلۡجَزَاۤءَ ٱلۡأَوۡفَىٰ﴿ ٤١ ﴾ وَأَنَّ إِلَىٰ رَبِّكَ ٱلۡمُنتَهَىٰ﴿ ٤٢ ﴾]] [سورة النجم]",
        'message': "‫[[مِن أَجۡلِ ذَ ٰ⁠لِكَ كَتَبۡنَا عَلَىٰ بَنِیۤ إِسۡرَ ٰ⁠ۤءِیلَ أَنَّهُۥ مَن قَتَلَ نَفۡسَۢا بِغَیۡرِ نَفۡسٍ أَوۡ فَسَادࣲ فِی ٱلۡأَرۡضِ فَكَأَنَّمَا قَتَلَ ٱلنَّاسَ جَمِیعࣰا وَمَنۡ أَحۡیَاهَا فَكَأَنَّمَاۤ أَحیَا ٱلنَّاسَ جَمِیعࣰاۚ وَلَقَدۡ جَاۤءَتۡهُمۡ رُسُلُنَا بِٱلۡبَیِّنَـٰتِ ثُمَّ إِنَّ كَثِیرࣰا مِّنۡهُم بَعۡدَ ذَ ٰ⁠لِكَ فِی ٱلۡأَرۡضِ لَمُسۡرِفُونَ﴿ ٣٢ ﴾‬]] [سورة المائدة]",
        'message': "‫[[أَمَّنۡ هُوَ قَـٰنِتٌ ءَانَاۤءَ ٱلَّیۡلِ سَاجِدࣰا وَقَاۤىِٕمࣰا یَحۡذَرُ ٱلۡـَٔاخِرَةَ وَیَرۡجُوا۟ رَحۡمَةَ رَبِّهِۦۗ قُل هَلۡ یَسۡتَوِی ٱلَّذِینَ یَعۡلَمُونَ وَٱلَّذِینَ لَا یَعۡلَمُونَۗ إِنَّمَا یَتَذَكَّرُ أُو۟لُوا۟ ٱلۡأَلۡبَـٰبِ﴿ ٩ ﴾‬]] [سورة الزمر]",
        'message': "يقول النبي ﷺ: (المؤمن القوي خير وأحب إلى الله من المؤمن الضعيف، وفي كل خير). رواه مسلم في الصحيح.",
    }
    
    message = messages.get(message_type, "Default reminder message")
    asyncio.run(send_message(message))
