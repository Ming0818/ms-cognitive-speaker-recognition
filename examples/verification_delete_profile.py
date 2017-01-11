""" delete profile example """

from __future__ import print_function
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import cognitive_sr  # pylint: disable=wrong-import-position


def delete_profile(subscription_key, profile_id):
    """ creates a user profile """
    speech_verification = cognitive_sr.SpeechVerification(subscription_key)
    result = speech_verification.delete_profile(profile_id)
    print('Deleted:', result)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python verification_delete_profile.py ' +
              '<subscription_key> <profile_id>')
        exit()

    delete_profile(sys.argv[1], sys.argv[2])
