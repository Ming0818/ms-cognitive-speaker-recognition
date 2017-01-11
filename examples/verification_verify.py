""" verify profile example """

from __future__ import print_function
import sys
import os
import io

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import cognitive_sr  # pylint: disable=wrong-import-position


def verify_profile(subscription_key, profile_id, wav_path):
    """ verifies a profile using a wav recording of them speaking """
    with io.open(wav_path, 'rb') as wav_file:
        wav_data = wav_file.read()

    speech_verification = cognitive_sr.SpeechVerification(subscription_key)
    result = speech_verification.verify_profile(profile_id, wav_data)
    print(result)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python verification_verify.py ' +
              '<subscription_key> <profile_id> <wav_path>')
        exit()

    verify_profile(sys.argv[1], sys.argv[2], sys.argv[3])
