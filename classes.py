
class JsonOperations:

    @classmethod
    def read(cls, ref):
        """Импортирует JSON в Python, и возвращает его значение.
        Аргументы: ref - ссылка на JSON, который надо присвоить переменной."""
        from json import load
        with open('data/' + ref + '.json') as json_import_data:
            data_file = load(json_import_data)
        return data_file

    @classmethod
    def save(cls, ref, data_file):
        """Сохраняет значение переменной в JSON.
        Аргументы: ref - ссылка на JSON, data_file - переменная,
        значение которой сохраняется в JSON."""
        from json import dump
        with open('data/' + ref + '.json', 'w') as add_info_file:
            dump(data_file, add_info_file)


class Initialization:

    @classmethod
    def do(cls):

        CreationPlayer.do()
        CreationEnemies.do()
        CreationCurrentItems.do()
        CreationItems.do()
        CreationEquipments.do()


class CreationPlayer:

    @classmethod
    def do(cls):
        import os.path

        check_base = os.path.exists('data')
        if not check_base:
            os.mkdir('data')

        check_file = os.path.exists('data/player.json')

        if not check_file:

            player = CreationPlayer.get()
            JsonOperations.save('player', player)

    @classmethod
    def get(cls):
        return {

            'name': '',

            'location': '',

            'character': {

                'strength': '5',
                'dexterity': '5',
                'intellect': '5',
                'constitution': '5',
                'will': '5',

            },

            'skills': {

                'swords': '0',
                'axes': '0',
                'spears': '0',
                'hummers': '0',

            },

            'status': {

                'max_health': '',
                'current_health': '',

                'max_stamina': '',
                'current_stamina': '',

                'focus': '',
                'speed': '',

                'alive': 'False'
            },
        }


class CreationEnemies:

    @classmethod
    def do(cls):
        import os.path

        check_base = os.path.exists('data')
        if not check_base:
            os.mkdir('data')

        check_file = os.path.exists('data/enemies.json')

        if not check_file:
            enemies = {

            }

            JsonOperations.save('enemies', enemies)

    @classmethod
    def get(cls):

        return {
            'name': '',
            'equipment_id': '1',
            'location': '',

            'character': {

                'strength': '5',
                'dexterity': '5',
                'intellect': '5',
                'constitution': '5',
                'will': '5',

            },

            'skills': {

                'swords': '0',
                'axes': '0',
                'spears': '0',
                'hummers': '0',

            },

            'status': {

                'max_health': '',
                'current_health': '',

                'max_stamina': '',
                'current_stamina': '',

                'focus': '',
                'speed': '',

            },
        }


class CreationEquipments:

    @classmethod
    def do(cls):
        import os.path

        check_base = os.path.exists('data')
        if not check_base:
            os.mkdir('data')

        check_file = os.path.exists('data/equipments.json')

        if not check_file:
            equipments = {

                '1': CreationEquipments.get()

            }

            JsonOperations.save('equipments', equipments)

    @classmethod
    def get(cls):

        return {

                    'first_weapon': '',
                    'second_weapon': '',

                    'head': '',
                    'body': '',
                    'arms': '',
                    'legs': '',

                    'first_artifact': '',
                    'second_artifact': '',
                    'third_artifact': ''

                }


class CreationCurrentItems:

    @classmethod
    def do(cls):
        import os.path

        check_base = os.path.exists('data')
        if not check_base:
            os.mkdir('data')

        check_file = os.path.exists('data/current_items.json')

        if not check_file:
            current_items = {}

            JsonOperations.save('current_items', current_items)


class CreationItems:

    @classmethod
    def do(cls):
        import os.path

        check_base = os.path.exists('data')
        if not check_base:
            os.mkdir('data')

        check_file = os.path.exists('data/items.json')

        if not check_file:
            items = {

            }

            JsonOperations.save('items', items)

    @classmethod
    def get(cls):
        return {

                    'type': '',

                    'armor_type': '',
                    'weapon_type': '',

                    'pierce_attack_damage': '',
                    'slash_attack_damage': '',
                    'blunt_attack_damage': '',
                    'mental_attack_damage': '',

                    'pierce_attack_resist': '',
                    'slash_attack_resist': '',
                    'blunt_attack_resist': '',
                    'mental_attack_resist': '',

                    'durability': '',
                    'weight': ''
                }


class MainMenu:

    @classmethod
    def do(cls):
        pass


class CreationCharacter:

    @classmethod
    def do(cls):
        pass


class FightStarter:

    @classmethod
    def do(cls):
        pass


class FightRuler:

    @classmethod
    def do(cls):
        pass
