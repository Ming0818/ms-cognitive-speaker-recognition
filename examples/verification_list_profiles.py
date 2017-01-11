""" list profiles example """

from __future__ import print_function
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import cognitive_sr  # pylint: disable=wrong-import-position


def list_profiles(subscription_key):
    """ lists all the currently registered profiles """
    speech_verification = cognitive_sr.SpeechVerification(subscription_key)
    profiles = speech_verification.get_all_profiles()

    for profile in profiles:
        print(profile)

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('Usage: python verification_list_profiles.py ' +
              '<subscription_key>')
        exit()

    list_profiles(sys.argv[1])
