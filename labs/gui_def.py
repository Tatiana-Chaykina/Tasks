import random
import string
from kiwisolver import strength
from CRUD import *
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class PasswordStrengthChecker:
    @staticmethod
    def check_strength(password):
        length = len(password)
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in string.punctuation for char in password)

        strength_score = sum([
            length >= 8,
            has_upper,
            has_lower,
            has_digit,
            has_special
        ])

        if strength_score == 5:
            return 2
        elif strength_score >= 3:
            return 1
        else:
            return 0


class Generator:
    @staticmethod
    def generator(length):
        inf_1 = {char: 0 for char in string.ascii_letters}
        inf_2 = {char: 0 for char in "%*)?@#$~"}
        inf_3 = {char: 0 for char in string.digits}
        for password_obj in get_all_passwords_2():
            for char in password_obj.password:
                if char in string.ascii_letters:
                    inf_1[char] += 1
                elif char in "%*)?@#$~":
                    inf_2[char] += 1
                elif char in string.digits:
                    inf_3[char] += 1
        inf_final = []
        for _ in range(length):
            if len(inf_2) > 0 and len(inf_final) < length // 4:
                key = min(inf_2, key=inf_2.get)
                inf_final.append(key)
                del inf_2[key]
            elif len(inf_3) > 0 and len(inf_final) < length // 2:
                key = min(inf_3, key=inf_3.get)
                inf_final.append(key)
                del inf_3[key]
            elif len(inf_1) > 0:
                key = min(inf_1, key=inf_1.get)
                inf_final.append(key)
                del inf_1[key]
        if len(inf_final) < length:
            inf_final += random.choices(
                string.ascii_letters + string.digits + string.punctuation,
                k=length - len(inf_final)
            )
        password = ''.join(random.choices(inf_final, k=length))
        return password