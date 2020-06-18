

def synthesize_ssml(name, wordlist):

    """Synthesizes speech from the input string of ssml.
    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    Example: <speak>Hello there.</speak>
    """

    ssml_string = "<speak><prosody rate='slow' pitch='-2st'>"          # This can be modified to change the prosody

    for word in wordlist:
        ssml_string += word + "<break strength='strong'/>"

    ssml_string += "</prosody></speak>"                                # the closing tag has to match of course

    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient.from_service_account_json(
        '/Users/lovebook/PycharmProjects/Text_to_speech_mp3/lmo_key.json')  # if you want to try you have to get your
                                                                            # own key.

    input_text = texttospeech.types.SynthesisInput(ssml=ssml_string)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='sv-SE',                                         # They have most languages to choose from
        name='sv-SE-Wavenet-A',                                        # Make sure its wavenet if you want natural sound
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open(name + '.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file ' + name + ".mp3")


list_1 = ["Astrofysiker. ", "Begå. ", "Geografi. ", "Latin. ", "Besökare. ", "Beundrad. ", "Återskapa. ", "Arrogant. ",
          "Väsentlig. ", "Förmedla. ", "Utsträckning. ", "Fängelse. "]


synthesize_ssml("lista1", list_1)  # this will create a mp3 file with an artificial voice reading the words in the list

