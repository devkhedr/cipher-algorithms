from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .algorithms.shift_cipher import ShiftCipher
from .algorithms.monoalphabetic_cipher import MonoalphabeticCipher
from .algorithms.affine_cipher import AffineCipher
from .algorithms.substitution_cipher import SubstitutionCipher
from .algorithms.playfair_cipher import PlayfairCipher
from .algorithms.vigenere_cipher import VigenereCipher
from .algorithms.rail_fence_cipher import RailFenceCipher
from .algorithms.row_transposition_cipher import RowTranspositionCipher


# Create your views here.
class EncryptView(APIView):
    def post(self, request):
        algorithm = request.data['algorithm']
        plaintext = request.data['input']
        key = request.data['key']
        ciphertext = 'default'
        if(str(algorithm) == "shift"):
            cipher = ShiftCipher(key)
            ciphertext = cipher.encrypt(plaintext)
        elif(str(algorithm) == "mono"):
            cipher = MonoalphabeticCipher(key)
            ciphertext = cipher.encrypt(plaintext)
        elif(str(algorithm) == "affine"):
            a = int(key[1])
            b = int(key[3])  # "(7,3)"
            cipher = AffineCipher(a, b)
            ciphertext = cipher.encrypt(plaintext)
        elif(str(algorithm) == "substitution"):
            cipher = SubstitutionCipher(key)
            ciphertext = cipher.encrypt(plaintext)
        elif(str(algorithm) == "playfair"):
            cipher = PlayfairCipher(key)
            ciphertext = cipher.encrypt(plaintext)
        elif(str(algorithm) == "vigenere"):
            cipher = VigenereCipher(key)
            ciphertext = cipher.encrypt(plaintext)
        elif(str(algorithm) == "rail"):
            cipher = RailFenceCipher()
            ciphertext = cipher.encrypt(plaintext, int(key))
        elif(str(algorithm) == "row"):
            cipher = RowTranspositionCipher(key)
            ciphertext = cipher.encrypt(plaintext)
        return Response({"ciphertext": ciphertext}, status=status.HTTP_200_OK)
        
class DecryptView(APIView):
    def post(self, request):
        algorithm = request.data['algorithm']
        ciphertext = request.data['input']
        key = request.data['key']
        plaintext = 'default'
        print(request.data)
        if(str(algorithm) == "shift"):
            cipher = ShiftCipher(key)
            plaintext = cipher.decrypt(ciphertext)
        elif(str(algorithm) == "mono"):
            cipher = MonoalphabeticCipher(key)
            plaintext = cipher.decrypt(ciphertext)
        elif(str(algorithm) == "affine"):
            a = int(key[1])
            b = int(key[3])  # "(7,3)"
            cipher = AffineCipher(a, b)
            plaintext = cipher.decrypt(ciphertext)
        elif(str(algorithm) == "substitution"):
            cipher = SubstitutionCipher(key)
            plaintext = cipher.decrypt(ciphertext)
        elif(str(algorithm) == "playfair"):
            cipher = PlayfairCipher(key)
            plaintext = cipher.decrypt(ciphertext)
        elif(str(algorithm) == "vigenere"):
            cipher = VigenereCipher(key)
            plaintext = cipher.decrypt(ciphertext)
        elif(str(algorithm) == "rail"):
            cipher = RailFenceCipher()
            plaintext = cipher.decrypt(ciphertext, int(key))
        elif(str(algorithm) == "row"):
            cipher = RowTranspositionCipher(key)
            plaintext = cipher.decrypt(ciphertext)
        print(plaintext)
        return Response({"plaintext": plaintext}, status=status.HTTP_200_OK)
