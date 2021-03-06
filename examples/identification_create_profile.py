""" create profile example """

from __future__ import print_function
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import cognitive_sr  # pylint: disable=wrong-import-position


def create_profile(subscription_key):
    """ creates a user profile """
    speech_identification = cognitive_sr.SpeechIdentification(subscription_key)
    result = speech_identification.create_profile()
    print(result)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python identification_create_profile.py ' +
              '<subscription_key>')
        exit()

    create_profile(sys.argv[1])
