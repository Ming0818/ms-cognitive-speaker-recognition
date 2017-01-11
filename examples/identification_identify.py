""" identify profile example """

from __future__ import print_function
import sys
import os
import io

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import cognitive_sr  # pylint: disable=wrong-import-position


def identify_profile(subscription_key, profile_ids, wav_path):
    """ identifies a profile using a wav recording of them speaking """
    with io.open(wav_path, 'rb') as wav_file:
        wav_data = wav_file.read()

    speech_identification = cognitive_sr.SpeechIdentification(subscription_key)
    result = speech_identification.identify_profile(
        profile_ids.split(','), wav_data, short_audio=True)
    print(result)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python identification_identify.py ' +
              '<subscription_key> <profile_ids,> <wav_path>')
        exit()

    identify_profile(sys.argv[1], sys.argv[2], sys.argv[3])
