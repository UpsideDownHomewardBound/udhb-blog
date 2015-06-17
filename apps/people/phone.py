from the_comm_app.plumbing import PhoneLine
from the_comm_app.voice.dispositions import ConferenceHoldingPattern, Voicemail
from the_comm_app.voice.features import CallBlast, ConferenceBlast
from settings.secrets import TWILIO_SID, TWILIO_AUTH
from hendrix.experience import crosstown_traffic


class MainCallBlast(ConferenceBlast):

    phones = '+18106233203',
    clients = '1_justin_mobile', '1_web_extn'
    time_to_wait_for_answer = 5


class KayeMylesHoldingPattern(ConferenceHoldingPattern):

    hold_music = "http://kayemyles.com/static/mmariachi.wav"


class PrimaryPhoneLine(PhoneLine):

    name = "primary_phone_line"
    number_to_use_for_outgoing_calls = "+16468462229"
    domain = "kayemyles.com:5555"

    twilio_sid = TWILIO_SID
    twilio_auth = TWILIO_AUTH

    greeting_text = "Thank you for calling Chelsea, Justin, and Notch.  Hold on while I fetch one of them."
    disposition = [KayeMylesHoldingPattern, Voicemail]
    features = [MainCallBlast]

    runner = crosstown_traffic.follow_response()

    voice = "alice"
    language = "en-AU"